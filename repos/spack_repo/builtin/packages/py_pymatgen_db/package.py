# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPymatgenDb(PythonPackage):
    """Pymatgen-db is a database add-on for the Python Materials Genomics (pymatgen)
    materials analysis library. It enables the creation of Materials Project-style
    MongoDB databases for management of materials data. A query engine is also
    provided to enable the easy translation of MongoDB docs to useful pymatgen
    objects for analysis purposes."""

    homepage = "https://github.com/materialsproject/pymatgen-db"
    pypi     = "pymatgen-db/pymatgen-db-2022.5.20.tar.gz"

    maintainers = ["meyersbs"]

    version("2022.5.20", sha256="1a4d8391bbfdb5093e54feb27ce44b4cc60289da971e340c4347a36fb7188f8a")

    # From setup.py:
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy", type="build")
    depends_on("py-pymatgen@2022.0.3:", type=("build", "run"))
    depends_on("py-monty@0.9.6:", type=("build", "run"))
    depends_on("py-pymongo@2.8:", type=("build", "run"))
