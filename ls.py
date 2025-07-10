#!/usr/bin/env python3
import os
import stat
import pwd
import grp
import time
import click

@click.command()
@click.option('-l', 'long', is_flag=True, help='use a long listing format')
@click.option('-a', 'show_all', is_flag=True, help='do not ignore entries starting with .')
@click.argument('paths', nargs=-1, type=click.Path(exists=True))
def cli(long, show_all, paths):
    """List information about the FILEs (the current directory by default)."""
    if not paths:
        paths = ['.']

    multiple = len(paths) > 1
    for path in paths:
        if multiple:
            click.echo(f"{path}:")
        if os.path.isdir(path):
            try:
                entries = sorted(os.listdir(path))
            except OSError as e:
                click.echo(f"ls: cannot access '{path}': {e.strerror}", err=True)
                continue
            entries = [e for e in entries if show_all or not e.startswith('.')]
            if long:
                for e in entries:
                    full = os.path.join(path, e)
                    try:
                        st = os.lstat(full)
                    except OSError as e:
                        click.echo(f"ls: cannot access '{full}': {e.strerror}", err=True)
                        continue
                    mode = stat.filemode(st.st_mode)
                    nlink = st.st_nlink
                    owner = pwd.getpwuid(st.st_uid).pw_name
                    group = grp.getgrgid(st.st_gid).gr_name
                    size = st.st_size
                    mtime = time.strftime('%b %d %H:%M', time.localtime(st.st_mtime))
                    click.echo(f"{mode} {nlink:>2} {owner} {group} {size:>6} {mtime} {e}")
            else:
                for e in entries:
                    click.echo(e)
        else:
            name = os.path.basename(path)
            if long:
                try:
                    st = os.lstat(path)
                except OSError as e:
                    click.echo(f"ls: cannot access '{path}': {e.strerror}", err=True)
                    continue
                mode = stat.filemode(st.st_mode)
                nlink = st.st_nlink
                owner = pwd.getpwuid(st.st_uid).pw_name
                group = grp.getgrgid(st.st_gid).gr_name
                size = st.st_size
                mtime = time.strftime('%b %d %H:%M', time.localtime(st.st_mtime))
                click.echo(f"{mode} {nlink:>2} {owner} {group} {size:>6} {mtime} {name}")
            else:
                click.echo(name)
        if multiple:
            click.echo()

if __name__ == '__main__':
    cli()
