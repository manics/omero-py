#!/usr/bin/env python
"""
   download plugin

   Plugin read by omero.cli.Cli during initialization. The method(s)
   defined here will be added to the Cli class for later use.

   Copyright 2007 Glencoe Software, Inc. All rights reserved.
   Use is subject to license terms supplied in LICENSE.txt

"""

from omero.cli import BaseControl

class DownloadControl(BaseControl):

    def _name(self):
        return "download"

    def help(self):
        return \
        """
        Syntax: download <id> <filename>
        Download the given file id to the given file name
        """

    def _run(self, *args):
        id = 1
        file = "foo"

        client = self.event.conn()
        session = client.getSession()
        filePrx = session.createRawFileStore()
        filePrx.setFileId(id)
        fileSize = filePrx.getSize()

c = DownloadControl(None, None)
try:
    register(c)
except NameError:
    c._main()
