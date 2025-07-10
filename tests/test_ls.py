import grp
import pwd
import stat
import time
from pathlib import Path

import pytest
from click.testing import CliRunner

from ls import cli


def test_default_and_show_all(tmp_path, monkeypatch):
    # Setup directory with visible and hidden files
    monkeypatch.chdir(tmp_path)
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "b.txt").write_text("b")
    (tmp_path / ".hidden").write_text("h")

    runner = CliRunner()
    # Default: only non-hidden, sorted
    result = runner.invoke(cli, [])
    assert result.exit_code == 0
    assert result.output.splitlines() == ["a.txt", "b.txt"]

    # Show all: include hidden files
    result = runner.invoke(cli, ["-a"])
    assert result.exit_code == 0
    assert result.output.splitlines() == [".hidden", "a.txt", "b.txt"]


def test_multiple_paths_prints_headers(tmp_path, monkeypatch):
    # Create two files
    monkeypatch.chdir(tmp_path)
    (tmp_path / "one").write_text("x")
    (tmp_path / "two").write_text("y")

    runner = CliRunner()
    result = runner.invoke(cli, ["one", "two"])
    assert result.exit_code == 0
    lines = result.output.splitlines()
    # Expect headers and names with blank lines after each
    assert lines == [
        "one:",
        "one",
        "",
        "two:",
        "two",
        "",
    ]


def test_invalid_path_shows_error():
    runner = CliRunner()
    result = runner.invoke(cli, ["no_such_path"])
    assert result.exit_code != 0
    assert "Error" in result.output


class DummyStat:
    def __init__(self, mode, nlink, uid, gid, size, mtime):
        self.st_mode = mode
        self.st_nlink = nlink
        self.st_uid = uid
        self.st_gid = gid
        self.st_size = size
        self.st_mtime = mtime


@pytest.fixture(autouse=True)
def fixed_metadata(monkeypatch):
    # Use fixed metadata for long listing
    monkeypatch.setattr(stat, "filemode", lambda m: "drwxr-xr-x")
    monkeypatch.setattr(
        pwd, "getpwuid", lambda uid: type("u", (), {"pw_name": "owner"})()
    )
    monkeypatch.setattr(
        grp, "getgrgid", lambda gid: type("g", (), {"gr_name": "group"})()
    )
    monkeypatch.setattr(time, "strftime", lambda fmt, tm: "Jan 01 00:00")


def test_long_single_file(tmp_path, monkeypatch):
    # Create a file and test long listing output
    monkeypatch.chdir(tmp_path)
    file_path = tmp_path / "file.txt"
    file_path.write_text("content")

    # Ensure lstat returns fixed dummy - mock the Path.lstat method
    dummy = DummyStat(mode=0, nlink=3, uid=1000, gid=1000, size=7, mtime=0)
    monkeypatch.setattr(Path, "lstat", lambda self: dummy)

    runner = CliRunner()
    result = runner.invoke(cli, ["-l", "file.txt"])
    assert result.exit_code == 0
    expected = "drwxr-xr-x  3 owner group      7 Jan 01 00:00 file.txt\n"
    assert result.output == expected


def test_long_directory(tmp_path, monkeypatch):
    # Create a directory with two entries
    monkeypatch.chdir(tmp_path)
    d = tmp_path / "d"
    d.mkdir()
    (d / "a").write_text("x")
    (d / "b").write_text("y")

    # Dummy stat for each entry - mock the Path.lstat method
    dummy = DummyStat(mode=0, nlink=1, uid=1000, gid=1000, size=1, mtime=0)
    monkeypatch.setattr(Path, "lstat", lambda self: dummy)

    runner = CliRunner()
    result = runner.invoke(cli, ["-l", "d"])
    assert result.exit_code == 0
    # Two entries sorted: a, b
    out_lines = result.output.splitlines()
    assert out_lines == [
        "drwxr-xr-x  1 owner group      1 Jan 01 00:00 a",
        "drwxr-xr-x  1 owner group      1 Jan 01 00:00 b",
    ]
