#!/usr/bin/env python
#
# MIT License
#
# Copyright (c) 2021 SCons Project
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
from pathlib import Path
from setuptools import setup

def package_files(directory, packagedir=None):
    """ Scans the given 'directory' for subfolders that should get packaged too,
        and returns a list of all those folders.
        If additionally a 'packagedir' is specified, the search
        for the folders starts within this packagedir, and its
        path gets stripped from the resulting folders.
        @warning Only a single folder name is allowed as 'packagedir', no paths!
    """
    paths = [os.path.join(directory, '*')]
    startdir = directory
    if packagedir:
        startdir = os.path.join(packagedir, directory)
    for (path, directories, filenames) in os.walk(startdir):
        for d in directories:
            if packagedir:
                # Strip packagedir from the path
                p = Path(path) / d / '*'
                if p.parts[0] == packagedir:
                    dpath = os.path.join(*p.parts[1:])
                else:
                    dpath = str(p)
            else:
                dpath = os.path.join(path, d, '*')
                
            if dpath not in paths:
                paths.append(dpath)
    return paths

setup(name='scons_docbook_xsl',
      version='1.1',
      description='Docbook XSLT code and stylesheets for SCons (documentation/build/test).',
      author='SCons Project',
      author_email='scons-dev@scons.org',
      url='https://github.com/SCons/scons-docbook',
      packages=['scons_docbook_xsl'],
      package_data={'' : package_files('docbook-xsl-1.79.1', 'scons_docbook_xsl') +
                         package_files('docbook-slides-3.4.0', 'scons_docbook_xsl')},
      license='MIT',
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: X11 Applications',
                   'Intended Audience :: End Users/Desktop',
                   'Topic :: Utilities',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3'
                  ],
      keywords='docbook scons xsl stylesheets slides',
      )

