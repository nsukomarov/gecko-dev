# -*- Mode: python; c-basic-offset: 4; indent-tabs-mode: nil; tab-width: 40 -*-
# vim: set filetype=python:
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys

from mozprocess import ProcessHandler

from mozlint import result

FLOW_ERROR_MESSAGE = """
An error occurred running flow. Please check the following error messages:

{}
""".strip()

FLOW_NOT_FOUND_MESSAGE = """
Could not find flow!  We looked at the --binary option, at the FLOW
environment variable, and then at your local node_modules path. Please Install
eslint and needed plugins with:

mach flow --setup

and try again.
""".strip()


def lint(paths, config, binary=None, fix=None, setup=None, **lintargs):
    """Run eslint."""
    print("TODO flow")
    

    return "flow results here"
