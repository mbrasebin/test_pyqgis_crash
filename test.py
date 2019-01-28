from qgis.core import *

# supply path to qgis install location
QgsApplication.setPrefixPath("/usr/", True)

# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI
qgs = QgsApplication([], True)

# load providers
qgs.initQgis()


qgs.exitQgis()
