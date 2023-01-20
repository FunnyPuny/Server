# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "src"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="OpenAPI FunnyPuny",
    author_email="",
    url="",
    keywords=["OpenAPI", "OpenAPI FunnyPuny"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['src=src.__main__:main']},
    long_description="""\
    This is api for server FunnyPuny
    """
)
