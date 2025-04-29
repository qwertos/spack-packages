# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyNir(PythonPackage):
    """Neuromorphic Intermediate Representation"""

    homepage = "https://github.com/neuromorphs/nir"
    pypi = "nir/nir-1.0.4.tar.gz"

    license("BSD-3-Clause")

    version("1.0.4", sha256="2f864b089cf1daf4147ab6613f24d515d8181e5479940efedb76faff743ad62c")

    depends_on("py-setuptools@60:", type=("build", "run"))
    depends_on("py-setuptools-scm@8:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
