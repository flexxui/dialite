# -*- coding: utf-8 -*-

"""
Dialite setup script.
"""

import os

try:
    import setuptools  # noqa, analysis:ignore
except ImportError:
    pass  # setuptools allows for "develop", but it's not essential

from distutils.core import setup


# %% Functions we need


def get_version_and_doc(filename):
    ns = dict(__version__="", __doc__="")
    docstatus = 0  # Not started, in progress, done
    for line in open(filename, "rb").read().decode().splitlines():
        if line.startswith("__version__"):
            exec(line.strip(), ns, ns)
        elif line.startswith('"""'):
            if docstatus == 0:
                docstatus = 1
                line = line.lstrip('"')
            elif docstatus == 1:
                docstatus = 2
        if docstatus == 1:
            ns["__doc__"] += line.rstrip() + "\n"
    if not ns["__version__"]:
        raise RuntimeError("Could not find __version__")
    return ns["__version__"], ns["__doc__"]


def package_tree(pkgroot):
    subdirs = [
        os.path.relpath(i[0], THIS_DIR).replace(os.path.sep, ".")
        for i in os.walk(os.path.join(THIS_DIR, pkgroot))
        if "__init__.py" in i[2]
    ]
    return subdirs


# %% Collect info for setup()

THIS_DIR = os.path.dirname(__file__)

# Define name and description
name = "dialite"
description = "Lightweight Python library to show simple dialogs."

# Get version and docstring (i.e. long description)
version, doc = get_version_and_doc(os.path.join(THIS_DIR, name, "__init__.py"))


# %% Setup

setup(
    name=name,
    version=version,
    author="Almar Klein and contributors",
    author_email="almar.klein@gmail.com",
    license="(new) BSD",
    url="http://dialite.readthedocs.io",
    download_url="https://pypi.python.org/pypi/dialite",
    keywords="GUI, dialog, lightweight",
    description=description,
    long_description=doc,
    platforms="any",
    provides=[name],
    install_requires=[],
    packages=package_tree(name),
    package_dir={name: name},
    zip_safe=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
