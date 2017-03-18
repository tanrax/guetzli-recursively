#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import path, walk, remove, rename
from subprocess import call
from sys import argv
top_dir = argv[1]
TEMP_FILE = 'temp.jpg'
extensions = ('jpeg', 'jpg')

for dirpath, dirnames, files in walk(top_dir):
    for name in files:
        for extension in extensions:
            if name.lower().endswith(extension):
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
                # Remove source
                try:
                    remove(url)
                except:
                    pass
                if size_acurate < 100:
                    # Move temp to source
                    rename(url_out, url)
                    print('Save ' + str(100 - size_acurate) + '%')
                else:
                    print('It is not necessary to optimize')
