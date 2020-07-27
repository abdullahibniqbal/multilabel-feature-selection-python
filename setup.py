# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:33:16 2020

@author: Mustehssun
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multilabel-feature-selection", 
    version="0.0.1",
    author="Mustehssun Iqbal",
    author_email="k173073@nu.edu.pk",
    description="Thesis project for multilabel feature selection",
    long_description="Thesis project for multilabel feature selection",
    long_description_content_type="text/markdown",
    url="https://github.com/Mustehssun/multilabel-feature-selection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
