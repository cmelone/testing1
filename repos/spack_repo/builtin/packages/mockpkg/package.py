# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Mockpkg(Package):
    """A mock package used to test the PR title renamer."""

    homepage = "https://example.com/mockpkg"
    url = "https://example.com/mockpkg-1.0.0.tar.gz"

    version("1.0.0", sha256="0000000000000000000000000000000000000000000000000000000000000000")

    def install(self, spec, prefix):
        pass
