#!/usr/bin/env python3
import grp
import pwd
import stat
import time
from os import stat_result
from pathlib import Path

import click


def format_file_info(file_stat: stat_result, file_name: str) -> str:
    """Format file information for long listing display."""
    mode: str = stat.filemode(file_stat.st_mode)
    nlink: int = file_stat.st_nlink
    owner: str = pwd.getpwuid(file_stat.st_uid).pw_name
    group: str = grp.getgrgid(file_stat.st_gid).gr_name
    size: int = file_stat.st_size
    mtime: str = time.strftime(
        "%b %d %H:%M",
        time.localtime(file_stat.st_mtime),
    )
    return f"{mode} {nlink:>2} {owner} {group} {size:>6} {mtime} {file_name}"


def list_directory_entries(
    path_obj: Path, show_all: bool, long_format: bool
) -> None:
    """List entries in a directory."""
    try:
        entries: list[Path] = sorted(path_obj.iterdir())
    except OSError as os_error:
        click.echo(
            f"ls: cannot access '{path_obj}': {os_error.strerror}",
            err=True,
        )
        return
    
    # Filter hidden files unless show_all is True
    entries = [
        entry for entry in entries if show_all or not entry.name.startswith(".")
    ]
    
    if long_format:
        for entry_path in entries:
            try:
                file_stat: stat_result = entry_path.lstat()
            except OSError as os_error:
                click.echo(
                    f"ls: cannot access '{entry_path}': {os_error.strerror}",
                    err=True,
                )
                continue
            formatted_info = format_file_info(file_stat, entry_path.name)
            click.echo(formatted_info)
    else:
        for entry_path in entries:
            click.echo(entry_path.name)


def list_single_file(path_obj: Path, long_format: bool) -> None:
    """List information for a single file."""
    if long_format:
        try:
            file_info: stat_result = path_obj.lstat()
        except OSError as os_error:
            click.echo(
                f"ls: cannot access '{path_obj}': {os_error.strerror}", err=True
            )
            return
        formatted_info = format_file_info(file_info, path_obj.name)
        click.echo(formatted_info)
    else:
        click.echo(path_obj.name)


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
def cli(
    long: bool,
    show_all: bool,
    paths: tuple[str, ...],
) -> None:
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
            list_directory_entries(path_obj, show_all, long)
        else:
            list_single_file(path_obj, long)
        
        if multiple_paths:
            click.echo()


if __name__ == "__main__":
    cli()
