# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEinops(PythonPackage):
    """Flexible and powerful tensor operations for readable and reliable code.

    Supports numpy, pytorch, tensorflow, and others."""

    homepage = "https://github.com/arogozhnikov/einops"
    pypi = "einops/einops-0.3.2.tar.gz"

    version("0.5.0", sha256="8b7a83cffc1ea88e306df099b7cbb9c3ba5003bd84d05ae44be5655864abb8d3")
    version("0.3.2", sha256="5200e413539f0377f4177ef00dc019968f4177c49b1db3e836c7883df2a5fe2e")

    depends_on("python@3.7:", when="@0.5:", type=("build", "run"))
    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-hatchling@1.10:", when="@0.5:", type="build")
    depends_on("py-setuptools", when="@:0.4", type="build")
