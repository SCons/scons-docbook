#!/usr/bin/env python

from setuptools import setup

setup(name='scons_docbook_xsl',
      version='1.0',
      description='Docbook XSLT code and stylesheets for SCons (documentation/build/test).',
      author='SCons Project',
      author_email='scons-dev@scons.org',
      url='https://github.com/SCons/scons-docbook',
      packages=['scons_docbook_xsl'],
      package_dir={'': ''},
      package_data={'scons_docbook_xsl' : ['docbook-xsl-1.76.1/*', 'docbook-slides-3.4.0/*']},
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

