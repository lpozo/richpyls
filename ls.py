#!/usr/bin/env python3
import grp
import pwd
import stat
import time
from os import stat_result
from pathlib import Path

import click


@click.command()
@click.option(
    "-l",
    "long",
    is_flag=True,
    help="use a long listing format",
)
@click.option(
    "-a",
    "show_all",
    is_flag=True,
    help="do not ignore entries starting with .",
)
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(exists=True),
)
def cli(long: bool, show_all: bool, paths: tuple[str, ...]) -> None:
    """List information about the FILEs (the current directory by default)."""
    if not paths:
        paths_list: list[str] = ["."]
    else:
        paths_list = list(paths)

    # Convert string paths to Path objects
    path_objects: list[Path] = [Path(p) for p in paths_list]
    multiple_paths: bool = len(path_objects) > 1

    for path_obj in path_objects:
        if multiple_paths:
            click.echo(f"{path_obj}:")
        if path_obj.is_dir():
            try:
                entries: list[Path] = sorted(path_obj.iterdir())
            except OSError as os_error:
                click.echo(
                    f"ls: cannot access '{path_obj}': {os_error.strerror}", err=True
                )
                continue
            entries = [
                entry for entry in entries if show_all or not entry.name.startswith(".")
            ]
            if long:
                for entry_path in entries:
                    try:
                        file_stat: stat_result = entry_path.lstat()
                    except OSError as os_error:
                        click.echo(
                            f"ls: cannot access '{entry_path}': {os_error.strerror}",
                            err=True,
                        )
                        continue
                    mode: str = stat.filemode(file_stat.st_mode)
                    nlink: int = file_stat.st_nlink
                    owner: str = pwd.getpwuid(file_stat.st_uid).pw_name
                    group: str = grp.getgrgid(file_stat.st_gid).gr_name
                    size: int = file_stat.st_size
                    mtime: str = time.strftime(
                        "%b %d %H:%M", time.localtime(file_stat.st_mtime)
                    )
                    click.echo(
                        f"{mode} {nlink:>2} {owner} {group} {size:>6} {mtime} {entry_path.name}"
                    )
            else:
                for entry_path in entries:
                    click.echo(entry_path.name)
        else:
            if long:
                try:
                    file_info: stat_result = path_obj.lstat()
                except OSError as os_error:
                    click.echo(
                        f"ls: cannot access '{path_obj}': {os_error.strerror}", err=True
                    )
                    continue
                file_mode: str = stat.filemode(file_info.st_mode)
                link_count: int = file_info.st_nlink
                file_owner: str = pwd.getpwuid(file_info.st_uid).pw_name
                file_group: str = grp.getgrgid(file_info.st_gid).gr_name
                file_size: int = file_info.st_size
                mod_time: str = time.strftime("%b %d %H:%M", time.localtime(file_info.st_mtime))
                click.echo(
                    f"{file_mode} {link_count:>2} {file_owner} {file_group} {file_size:>6} {mod_time} {path_obj.name}"
                )
            else:
                click.echo(path_obj.name)
        if multiple_paths:
            click.echo()


if __name__ == "__main__":
    cli()
