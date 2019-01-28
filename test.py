from qgis.core import *
from sys import exit
import time

import os
import signal

def sig_handler(signum, frame):
    print("segfault")
signal.signal(signal.SIGSEGV, sig_handler)

os.kill(os.getpid(), signal.SIGSEGV)


# supply path to qgis install location
QgsApplication.setPrefixPath("/usr", True)

# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI
qgs = QgsApplication([], False)

# load providers
qgs.initQgis()


qgs.exitQgis()


exit()
