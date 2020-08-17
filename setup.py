#!/usr/bin/env python

import os
from setuptools import setup

def package_files(directory):
    paths = [os.path.join(directory, '*')]
    for (path, directories, filenames) in os.walk(directory):
        for d in directories:
            paths.append(os.path.join(path, d, '*'))
    return paths

setup(name='scons_docbook_xsl',
      version='1.0',
      description='Docbook XSLT code and stylesheets for SCons (documentation/build/test).',
      author='SCons Project',
      author_email='scons-dev@scons.org',
      url='https://github.com/SCons/scons-docbook',
      packages=['scons_docbook_xsl'],
      package_data={'' : package_files('docbook-xsl-1.76.1') +
                         package_files('docbook-slides-3.4.0')},
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

