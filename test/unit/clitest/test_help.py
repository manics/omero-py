#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2015 University of Dundee & Open Microscopy Environment.
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import pytest
from omero.cli import CLI, NonZeroReturnCode

cli = CLI()
cli.loadplugins()
commands = cli.controls.keys()
topics = cli.topics.keys()


class TestHelp(object):

    def setup_method(self, method):
        self.args = ["help"]

    def testHelp(self):
        self.args += ["-h"]
        cli.invoke(self.args, strict=True)

    @pytest.mark.parametrize('recursive', [None, "--recursive"])
    def testAll(self, recursive):
        self.args += ["--all"]
        if recursive:
            self.args.append(recursive)
        cli.invoke(self.args, strict=True)

    @pytest.mark.parametrize('recursive', [None, "--recursive"])
    @pytest.mark.parametrize('command', commands)
    def testCommand(self, command, recursive):
        self.args += [command]
        if recursive:
            self.args.append(recursive)
        cli.invoke(self.args, strict=True)

    @pytest.mark.parametrize('topic', topics)
    def testTopic(self, topic):
        self.args += [topic, "-h"]
        cli.invoke(self.args, strict=True)
