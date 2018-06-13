#encoding:UTF-8
#author:justry

#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

setup(
    name="adam",
    version="0.1",
    packages=find_packages(exclude=["adam.test.*"]),

    install_requires=['tensorflow>=1.3',
                      'Pillow>=4.3.0',
                      #'numpy>=1.13.1+mkl;platform_system=="Windows"',
                      #'numpy>=1.13.3;platform_system=="Linux"',
                      'Shapely>=1.6.1',
                      'opencv-contrib-python>=3.3.0',
                      'Keras>=2.0.8',
                      'h5py>=2.7.1',
                      'matplotlib>=2.1.0',
                      'web.py>=0.40.dev0'],
    extras_require={':sys_platform=="win32"': ['numpy>=1.13.1+mkl'],
                    ':"linux" in sys_platform': ['numpy>=1.13.3']
    },
    include_package_data=True,
    package_data={
        'adam':["adam/tmp/*"],
    },
)