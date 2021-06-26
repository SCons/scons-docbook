# MIT License
#
# Copyright The SCons Foundation
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

import pkg_resources

# Local folder for the collection of DocBook XSLs
db_xsl_folder = pkg_resources.resource_filename('scons_docbook_xsl', 'docbook-xsl-1.79.1')

# Local folder for the Docbook slides package
db_slides_folder = pkg_resources.resource_filename('scons_docbook_xsl', 'docbook-slides-3.4.0')


def getXslDir():
    """ Return the path to the local installation
        of the Docbook XSL stylesheets.
    """
    return db_xsl_folder

def getSlidesDir():
    """ Return the path to the local installation
        of the Docbook slides stylesheets.
    """
    return db_slides_folder

