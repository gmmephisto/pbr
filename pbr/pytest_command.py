# Copyright 2011 OpenStack Foundation
# Copyright 2012-2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""setuptools/distutils commands to run py.test via setup.py"""

from distutils import cmd
from distutils.errors import DistutilsError


class _PyTestDummy(cmd.Command):
    """PyTest command class with empty handler."""

    description = "Run unit tests using py.test"

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print("Install 'pytest' package to run 'pytest' command properly.")


class _PyTest(_PyTestDummy):

    user_options = [
        ("pytest-args=", "t", "Run py.test command with specified arguments"),
    ]

    def initialize_options(self):
        self.pytest_args = None

    def finalize_options(self):
        if self.pytest_args is None:
            self.pytest_args = []
        else:
            self.pytest_args = self.pytest_args.split()

    def run(self):
        result = pytest.main(self.pytest_args)
        if result:
            raise DistutilsError("py.test failed (%d)" % result)


try:
    import pytest
except ImportError:
    have_pytest = False
    PyTest = _PyTestDummy
else:
    have_pytest = True
    PyTest = _PyTest
