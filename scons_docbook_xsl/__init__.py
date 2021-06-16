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

