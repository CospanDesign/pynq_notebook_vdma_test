from setuptools import setup, find_packages
import subprocess
import sys
import shutil
import overlay

setup(
    name = "vdma_test_overlay",
    version = overlay.__version__,
    url = 'https://github.com/CospanDesign/pynq_notebook_vdma_test',
    license = 'All rights reserved.',
    author = "Dave McCoy",
    author_email = "dave.mccoy@cospandesign.com",
    packages = ['overlay'],
    package_data = {
    '' : ['*.bit','*.tcl','*.py','*.so','*.jpg'],
    },
    description = "Overlay that demonstrates VDMA Test"
)
