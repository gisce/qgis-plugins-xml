# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestPlugin4
                                 A QGIS plugin
 This is my third awesome plugin for testing.
                              -------------------
        begin                : 2016-02-29
        git sha              : $Format:%H$
        copyright            : (C) 2016 by Larry Shaffer (Boundless)
        email                : lshaffer@boundlessgeo.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# noinspection PyPackageRequirements
from PyQt4.QtGui import QAction, QIcon, QMessageBox
import os.path


class TestPlugin4:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.name = u'Test Plugin 4'
        self.action = None
        self.icon_path = os.path.join(
            self.plugin_dir, 'images', 'test_plugin_4.png')

    # noinspection PyPep8Naming
    def initGui(self):
        icon = QIcon(self.icon_path)
        self.action = QAction(icon, u'Run', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.action.setEnabled(True)

        self.iface.addPluginToMenu(self.name, self.action)

    def unload(self):
        self.iface.removePluginMenu(self.name, self.action)

    def run(self):
        QMessageBox.information(None, 'Testing',
                                "Test information dialog from plugin: \n\n{0}"
                                .format(self.name))
