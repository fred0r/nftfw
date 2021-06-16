"""nftfw tests
"""
# Ini file for nftfw tests
#
import os
import sys
# get the path of this file
install = os.path.dirname(__file__) # pylint: disable=invalid-name
# change into the directory
os.chdir(install)
# add it at the start of path
sys.path.insert(0, install)
#
# check version of python
# this code has been tested on 3.6 and is really
# aimed at running on 3.7
assert sys.version_info >= (3, 6)

# pylint: disable=wrong-import-position
import init_tests
init_tests.init_tests()
