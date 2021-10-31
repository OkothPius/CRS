#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="django_crime",
    description="An application used to report crime in Mandera county"
    "for Django.",
    version='3.2.5',
    url="https://orukopius",
    author="Oruko Pius",
    author_email="test@user.com",
    license="MIT",
    packages=find_packages(),
    install_requires=("Django>=3",),
)
