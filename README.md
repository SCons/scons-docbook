# scons-docbook
This repo holds the 'scons_docbook_xsl' package for SCons. It's an optional package that
contains the Docbook XSLT stylesheets for creating the documentation of an SCons release. It works
closely together with the "docbook" Tool and happened to be an integral part of its
directory for quite a while.

However, it was finally decided to move these files out of the main repo, because

* not every SCons user needs them, and
* some online tools would falsely recognize and list SCons as an XSLT project.
