# This Python file uses the following encoding: utf-8
"""
contact: software@cbica.upenn.edu
Copyright (c) 2018 University of Pennsylvania. All rights reserved.
Use of this source code is governed by license located in license file: https://github.com/CBICA/BrainChart/blob/main/LICENSE
"""

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from yapsy.PluginManager import PluginManager
from yapsy.IPlugin import IPlugin
import os, sys
#from BrainChart.dataio import DataIO
from QtBrainChartGUI.core.model.datamodel import DataModel
from .aboutdialog import AboutDialog
from QtBrainChartGUI.resources import resources
from PyQt5.QtWidgets import QAction
import pandas as pd

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, dataFile=None, harmonizationModelFile=None, SPAREModelFile=None):
        super(MainWindow,self).__init__()
        self.SetupUi()
        self.SetupConnections()

        #instantiate data model
        self.datamodel = DataModel()

        # Create plugin manager
        self.manager = PluginManager(categories_filter={ "UI": IPlugin})
        root = os.path.dirname(__file__)
        self.manager.setPluginPlaces([os.path.join(root, 'plugins')])
        #self.manager.setPluginPlaces(["plugins"])

        # Load plugins
        self.manager.locatePlugins()
        p = self.manager.loadPlugins()

        self.Plugins = {}
        for plugin in self.manager.getPluginsOfCategory("UI"):
            # plugin.plugin_object is an instance of the plugin
            po = plugin.plugin_object
            po.datamodel = self.datamodel
            po.SetupConnections()
            self.Plugins[plugin.name] = po
            print("plugins: ", plugin.name)
            #self.ui.tabWidget.addTab(po.getUI(),plugin.name)
            self.ui.tabWidget.addTab(po,plugin.name)

        if dataFile is not None:
            # if datafile provided on cmd line, load it
            self.Plugins['data'].ReadData(dataFile)

        if harmonizationModelFile is not None:
            pass
            #if harmonization model file provided on cmd line, load it
            #self.OnHarmonizationModelFileOpenClicked(harmonizationModelFile)
        if SPAREModelFile is not None:
            pass
            #if SPARE model file provided on cmd line, load it
            #self.OnSPAREModelFileOpenClicked(SPAREModelFile)
        
        # Include Mac menu bar
        self.ui.actionHelp.setMenuRole(QAction.NoRole)
        self.ui.actionAbout.setMenuRole(QAction.NoRole)

    def SetupConnections(self):
        self.actionAbout.triggered.connect(self.OnAboutClicked)
        self.actionHelp.triggered.connect(self.OnHelpClicked)
 
    def SetupUi(self):
        root = os.path.dirname(__file__)
        self.ui = uic.loadUi(os.path.join(root, 'mainwindow.ui'), self)
        self.ui.setWindowTitle('NiBAx')
        self.setWindowIcon(QtGui.QIcon(":/images/NiBAX Logo.png"))
        self.aboutdialog = AboutDialog(self)

    def OnAboutClicked(self):
        self.aboutdialog.show()

    def OnHelpClicked(self):
        url = QtCore.QUrl('https://github.com/CBICA/iSTAGING-Tools')
        QtGui.QDesktopServices.openUrl(url)

    def OnCloseClicked(self):
        #close currently loaded data and model
        QtWidgets.QApplication.quit()

    def ResetUI(self):
        #reset all UI
        pass
