# -*- Mode: python; c-basic-offset: 4; indent-tabs-mode: nil; tab-width: 40 -*-
# vim: set filetype=python:
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import sys
import os
import json

from mozprocess import ProcessHandler

from mozlint import result

FLOW_ERROR_MESSAGE = """
An error occurred running flow. Please check the following error messages:

{}
""".strip()

FLOW_NOT_FOUND_MESSAGE = """
Could not find flow!  We looked at the --binary option, at the flow
environment variable, and then at your local node_modules path. Please Install
flow:

$npm install --global flow-bin
and pass path to binary or just use
$mach flow --setup

and try again.
""".strip()


def lint(paths, config, binary=None, fix=None, setup=None, **lintargs):
    """Run FLOW."""

    # TODO(komarov) add check that `$ flow` exitst

    proc = ProcessHandler(["flow", "check", "--json", "--pretty"], env=os.environ, stream=None, shell=False)
    proc.run()

    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.kill()
        return [] # "FLOW was killed"

    output = ''.join(proc.output)

    if not output:
        return [] # "FLOW has silently quit"

    try:
        jsonresult = json.loads(output)
    except ValueError:
        print(FLOW_ERROR_MESSAGE.format(output))
        return 1

    results = []
    errors = jsonresult['errors']
    for err in errors:
        for msg in err.get('message'):
            formattedError = {
                'rule': err.get('kind'),
                'level': err.get('level'),
                'lineno': msg.get('line'),
                'path': msg.get('path'),
                'message': msg.get('descr'),
            }
            results.append(result.from_config(config, **formattedError))

    return results
