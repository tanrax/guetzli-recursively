#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Libraries
import click
from os import path, walk, remove, rename
from imghdr import what
from subprocess import call

# Variables
TEMP_FILE = 'temp.jpg'
TYPES = ('jpeg',)
LIMIT_QUALITY = 84


@click.command()
@click.option(
        '--quality',
        default=100,
        help='Quality >= {quality} [default 100].'.format(
            quality=LIMIT_QUALITY
        )
)
@click.argument('folder', type=click.Path(exists=True))
def run(quality, folder):
    for dirpath, dirnames, files in walk(folder):
        for name in files:
            url = path.join(dirpath, name)
            # Check type
            if what(url) in TYPES or quality >= LIMIT_QUALITY:
                # Get urls
                click.echo(url)
                url_out = path.join(folder, TEMP_FILE)
                # Remove temp image
                try:
                    remove(url_out)
                except:
                    pass
                # Execute guetzli
                call(['guetzli', '--quality', str(quality), url, url_out])
                # Print your have saved
                size_source = path.getsize(url)
                try:
                    size_out = path.getsize(url_out)
                except:
                    size_out = size_source
                size_acurate = 100 * size_out / size_source
                # Check if it is cost effective to replace it
                if size_acurate < 100:
                    # Remove source
                    try:
                        remove(url)
                    except:
                        pass
                    # Move temp to source
                    rename(url_out, url)
                    click.echo(
                            'Save ' + str(round(100 - size_acurate, 2)) + '%')
                else:
                    click.echo('It is not necessary to optimize')


if __name__ == '__main__':
    run()
