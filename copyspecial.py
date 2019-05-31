#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
# import subprocess
import commands
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "jontaylor224"


# +++your code here+++

def get_special_paths(from_dir):
    """returns a list of all special files in a given directory"""
    return [os.path.abspath(os.path.join(from_dir, fname))
            for fname in os.listdir(from_dir)
            if re.search(r'__(\w+)__', fname)]


def copy_to(paths, to_dir):
    """copies files to a destination directory, creating it if needed"""
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    for path in paths:
        fname = os.path.basename(path)
        shutil.copy(path, os.path.join(to_dir, fname))


def zip_to(paths, zipfile):
    """compresses all given files into a zip file with given name"""
    cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    print "Command I'm going to do:" + cmd
    (status, output) = commands.getstatusoutput(cmd)
    # print to stderr if subprocess throws an error
    if status:
        sys.stderr.write(output)
        sys.exit(1)


def main():
    """Finds all special files in the given directory target(s). Special
        files are defined as those having __xxxx__ in the filename.
        If given argument flags of --todir, will copy all special files
        to the given directory.  If given argument flag of --tozip,
        will compress all special files into a zipfile with the
        specified name.
        """
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='source dir for special files',
                        nargs='+')
    args = parser.parse_args()

    paths = []
    for dirname in args.from_dir:
        paths.extend(get_special_paths(dirname))

    if args.todir:
        copy_to(paths, args.todir)
    elif args.tozip:
        zip_to(paths, args.tozip)
    else:
        print '\n'.join(paths)


if __name__ == "__main__":
    main()
