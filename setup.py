#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name="pv211_utils",
    version='2.0.0',
    description="Utilities for PV211 project",
    long_description="",
    classifiers=[],
    author="Michal Stefanik",
    author_email="stefanik.m@fi.muni.cz",
    url="https://gitlab.fi.muni.cz",
    license="MIT",
    packages=find_packages(exclude=['test.*']),
    package_dir={"pv211_utils": "pv211_utils"},
    include_package_data=True,
    zip_safe=True,
    setup_requires=[
        "pip",
        "setuptools",
    ],
    install_requires=requirements,
    extras_require={
        "notebooks": [
            "jupyterhub==3.0.0",
            "jupyterlab",
        ],
        "google_drive": [
            "gdown",
        ],
    },
    package_data={
        "pv211_utils": [
            "data/*",
        ],
    },
)

# vim: set cin et ts=4 sw=4 ft=python :11
