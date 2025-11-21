from setuptools import setup, find_packages
import os, sys, glob, fnmatch

setup(name="pysentech",
      version='0.3.0',
      description="pysentech is a python wrapper for the Sentech USB Camera SDK",
      long_description=""" pysentech is a python wrapper for the Sentech USB Camera SDK.
        It features a low-level interface for interacting with the C dll directly, and a high-level
        interface with more pythonic camera and frame objects.
      """,
      author='derricw',
      author_email='derricw@gmail.com',
      url='https://github.com/derricw/pysentech',
      license='MIT',
      packages=['pysentech'],
      zip_safe=False,
)