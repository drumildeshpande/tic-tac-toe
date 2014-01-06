# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

import gettext
from gettext import gettext as _
gettext.textdomain('tic-tac-toe')

import logging
logger = logging.getLogger('tic_tac_toe')

from tic_tac_toe_lib.AboutDialog import AboutDialog

# See tic_tac_toe_lib.AboutDialog.py for more details about how this class works.
class AboutTicTacToeDialog(AboutDialog):
    __gtype_name__ = "AboutTicTacToeDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutTicTacToeDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

