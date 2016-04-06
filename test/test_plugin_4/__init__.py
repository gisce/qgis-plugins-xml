# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestPlugin4
                                 A QGIS plugin
 This is my fourth awesome plugin for testing.
                             -------------------
        begin                : 2016-04-06
        copyright            : (C) 2016 by Larry Shaffer (Boundless)
        email                : lshaffer@boundlessgeo.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):
    from .test_plugin_4 import TestPlugin4
    return TestPlugin4(iface)
