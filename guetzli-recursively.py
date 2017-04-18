#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path, walk, remove, rename
from imghdr import what
from subprocess import call
from sys import argv
top_dir = argv[1]
TEMP_FILE = 'temp.jpg'
TYPES = ('jpeg',)

for dirpath, dirnames, files in walk(top_dir):
    for name in files:
        if what(path.join(dirpath, name)) in TYPES:
            # Get urls
            url = path.join(dirpath, name)
            print(url)
            url_out = path.join(top_dir, TEMP_FILE)
            # Remove temp image
            try:
                remove(url_out)
            except:
                pass
            # Execute guetzli
            call(['guetzli', url, url_out])
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
                print('Save ' + str(round(100 - size_acurate, 2)) + '%')
            else:
                print('It is not necessary to optimize')
