# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfvis(RPackage):
    """Interactive visualizations for profiling R code."""

    cran = "profvis"

    version("0.3.7", sha256="43974863cb793f81dbea4b94096343c321f7739c9038980405c9b16b04a906b9")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
