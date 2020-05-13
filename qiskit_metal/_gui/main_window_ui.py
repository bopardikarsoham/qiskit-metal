# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 776)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/metal_logo"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks|QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.GroupedDragging)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.mainViewTab = QtWidgets.QWidget()
        self.mainViewTab.setObjectName("mainViewTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainViewTab)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main_view"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.tabWidget.addTab(self.mainViewTab, icon1, "")
        self.tabElements = QtWidgets.QWidget()
        self.tabElements.setObjectName("tabElements")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabElements)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/elements"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabElements, icon2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 22))
        self.menubar.setBaseSize(QtCore.QSize(0, 0))
        self.menubar.setObjectName("menubar")
        self.menuDesign = QtWidgets.QMenu(self.menubar)
        self.menuDesign.setTearOffEnabled(False)
        self.menuDesign.setSeparatorsCollapsible(True)
        self.menuDesign.setToolTipsVisible(True)
        self.menuDesign.setObjectName("menuDesign")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuStylesheet = QtWidgets.QMenu(self.menuView)
        self.menuStylesheet.setObjectName("menuStylesheet")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuRender = QtWidgets.QMenu(self.menubar)
        self.menuRender.setObjectName("menuRender")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setMinimumSize(QtCore.QSize(0, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/help"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.menuHelp.setIcon(icon3)
        self.menuHelp.setToolTipsVisible(True)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPlot = QtWidgets.QMenu(self.menubar)
        self.menuPlot.setObjectName("menuPlot")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBarDesign = QtWidgets.QToolBar(MainWindow)
        self.toolBarDesign.setOrientation(QtCore.Qt.Horizontal)
        self.toolBarDesign.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBarDesign.setObjectName("toolBarDesign")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarDesign)
        self.toolBarView = QtWidgets.QToolBar(MainWindow)
        self.toolBarView.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBarView.setObjectName("toolBarView")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBarView)
        self.dockDesign = QtWidgets.QDockWidget(MainWindow)
        self.dockDesign.setMinimumSize(QtCore.QSize(310, 196))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/design"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dockDesign.setWindowIcon(icon4)
        self.dockDesign.setFloating(False)
        self.dockDesign.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockDesign.setObjectName("dockDesign")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(-1, 2, -1, 2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_comp_zoom = QtWidgets.QToolButton(self.dockWidgetContents)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/plot/point"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comp_zoom.setIcon(icon5)
        self.btn_comp_zoom.setObjectName("btn_comp_zoom")
        self.gridLayout.addWidget(self.btn_comp_zoom, 0, 3, 1, 1)
        self.btn_comp_actions = QtWidgets.QToolButton(self.dockWidgetContents)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/_imgs/support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comp_actions.setIcon(icon6)
        self.btn_comp_actions.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.btn_comp_actions.setObjectName("btn_comp_actions")
        self.gridLayout.addWidget(self.btn_comp_actions, 0, 1, 1, 1)
        self.btn_comp_del = QtWidgets.QToolButton(self.dockWidgetContents)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/delete"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comp_del.setIcon(icon7)
        self.btn_comp_del.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_comp_del.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_comp_del.setObjectName("btn_comp_del")
        self.gridLayout.addWidget(self.btn_comp_del, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filter_text_design = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.filter_text_design.setText("")
        self.filter_text_design.setClearButtonEnabled(True)
        self.filter_text_design.setObjectName("filter_text_design")
        self.horizontalLayout.addWidget(self.filter_text_design)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tableComponents = TableComponents(self.dockWidgetContents)
        self.tableComponents.setAlternatingRowColors(True)
        self.tableComponents.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableComponents.setSortingEnabled(True)
        self.tableComponents.setObjectName("tableComponents")
        self.tableComponents.horizontalHeader().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.tableComponents)
        self.dockDesign.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockDesign)
        self.dockNewComponent = QtWidgets.QDockWidget(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/component"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dockNewComponent.setWindowIcon(icon8)
        self.dockNewComponent.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockNewComponent.setObjectName("dockNewComponent")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filter_text_component = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.filter_text_component.setClearButtonEnabled(True)
        self.filter_text_component.setObjectName("filter_text_component")
        self.horizontalLayout_2.addWidget(self.filter_text_component)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents_2)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.dockNewComponent.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockNewComponent)
        self.dockComponent = QtWidgets.QDockWidget(MainWindow)
        self.dockComponent.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockComponent.setObjectName("dockComponent")
        self.dockComponentCental = QtWidgets.QWidget()
        self.dockComponentCental.setObjectName("dockComponentCental")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockComponentCental)
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dockComponent.setWidget(self.dockComponentCental)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockComponent)
        self.dockLog = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockLog.sizePolicy().hasHeightForWidth())
        self.dockLog.setSizePolicy(sizePolicy)
        self.dockLog.setMinimumSize(QtCore.QSize(100, 100))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/log"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dockLog.setWindowIcon(icon9)
        self.dockLog.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockLog.setObjectName("dockLog")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.log_text = LoggingWindowWidget(self.dockWidgetContents_4)
        self.log_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.log_text.setObjectName("log_text")
        self.verticalLayout_4.addWidget(self.log_text)
        self.dockLog.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockLog)
        self.dockConnectors = QtWidgets.QDockWidget(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/connectors"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.dockConnectors.setWindowIcon(icon10)
        self.dockConnectors.setObjectName("dockConnectors")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.text_filter_connectors = QtWidgets.QLineEdit(self.dockWidgetContents_5)
        self.text_filter_connectors.setClearButtonEnabled(True)
        self.text_filter_connectors.setObjectName("text_filter_connectors")
        self.horizontalLayout_3.addWidget(self.text_filter_connectors)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tableConnectors = QtWidgets.QTableView(self.dockWidgetContents_5)
        self.tableConnectors.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableConnectors.setAlternatingRowColors(False)
        self.tableConnectors.setObjectName("tableConnectors")
        self.verticalLayout_6.addWidget(self.tableConnectors)
        self.dockConnectors.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockConnectors)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon11)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/load"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon12)
        self.actionLoad.setAutoRepeat(False)
        self.actionLoad.setObjectName("actionLoad")
        self.actionDesign = QtWidgets.QAction(MainWindow)
        self.actionDesign.setCheckable(True)
        self.actionDesign.setChecked(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/design"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDesign.setIcon(icon13)
        self.actionDesign.setObjectName("actionDesign")
        self.actionComponent = QtWidgets.QAction(MainWindow)
        self.actionComponent.setCheckable(True)
        self.actionComponent.setChecked(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/component"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionComponent.setIcon(icon14)
        self.actionComponent.setObjectName("actionComponent")
        self.actionElements = QtWidgets.QAction(MainWindow)
        self.actionElements.setCheckable(True)
        self.actionElements.setChecked(False)
        self.actionElements.setIcon(icon2)
        self.actionElements.setObjectName("actionElements")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setCheckable(True)
        self.actionLog.setChecked(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/log"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog.setIcon(icon15)
        self.actionLog.setObjectName("actionLog")
        self.actionNewComponent = QtWidgets.QAction(MainWindow)
        self.actionNewComponent.setCheckable(True)
        self.actionNewComponent.setChecked(True)
        self.actionNewComponent.setIcon(icon6)
        self.actionNewComponent.setObjectName("actionNewComponent")
        self.actionDelete_All = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/delete_all"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete_All.setIcon(icon16)
        self.actionDelete_All.setPriority(QtWidgets.QAction.LowPriority)
        self.actionDelete_All.setObjectName("actionDelete_All")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/plot/zoom"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon17)
        self.actionZoom.setObjectName("actionZoom")
        self.actionPan = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/plot/pan"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPan.setIcon(icon18)
        self.actionPan.setObjectName("actionPan")
        self.actionConnectors = QtWidgets.QAction(MainWindow)
        self.actionConnectors.setCheckable(True)
        self.actionConnectors.setChecked(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/connectors"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnectors.setIcon(icon19)
        self.actionConnectors.setObjectName("actionConnectors")
        self.actionStyleOpen = QtWidgets.QAction(MainWindow)
        self.actionStyleOpen.setObjectName("actionStyleOpen")
        self.actionStyleDefault = QtWidgets.QAction(MainWindow)
        self.actionStyleDefault.setObjectName("actionStyleDefault")
        self.actionStyleDark = QtWidgets.QAction(MainWindow)
        self.actionStyleDark.setObjectName("actionStyleDark")
        self.actionScreenshot = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/screenshot"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScreenshot.setIcon(icon20)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.action_full_refresh = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/force_refresh"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_full_refresh.setIcon(icon21)
        self.action_full_refresh.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        self.action_full_refresh.setAutoRepeat(False)
        self.action_full_refresh.setPriority(QtWidgets.QAction.HighPriority)
        self.action_full_refresh.setObjectName("action_full_refresh")
        self.actionRebuild = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/rebuild"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRebuild.setIcon(icon22)
        self.actionRebuild.setPriority(QtWidgets.QAction.HighPriority)
        self.actionRebuild.setObjectName("actionRebuild")
        self.actionFull_Screen = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/plot/autozoom"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFull_Screen.setIcon(icon23)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionMetal_Dark = QtWidgets.QAction(MainWindow)
        self.actionMetal_Dark.setObjectName("actionMetal_Dark")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setIcon(icon11)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.menuDesign.addAction(self.actionLoad)
        self.menuDesign.addSeparator()
        self.menuDesign.addAction(self.actionSave)
        self.menuDesign.addAction(self.actionSaveAs)
        self.menuDesign.addSeparator()
        self.menuDesign.addAction(self.actionDelete_All)
        self.menuStylesheet.addAction(self.actionMetal_Dark)
        self.menuStylesheet.addAction(self.actionStyleDark)
        self.menuStylesheet.addSeparator()
        self.menuStylesheet.addAction(self.actionStyleDefault)
        self.menuStylesheet.addAction(self.actionStyleOpen)
        self.menuView.addAction(self.actionScreenshot)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionDesign)
        self.menuView.addAction(self.actionComponent)
        self.menuView.addAction(self.actionElements)
        self.menuView.addAction(self.actionConnectors)
        self.menuView.addAction(self.actionLog)
        self.menuView.addAction(self.actionNewComponent)
        self.menuView.addSeparator()
        self.menuView.addAction(self.menuStylesheet.menuAction())
        self.menuAnalysis.addSeparator()
        self.menuRender.addSeparator()
        self.menuPlot.addAction(self.actionPan)
        self.menuPlot.addAction(self.actionZoom)
        self.menubar.addAction(self.menuDesign.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuRender.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBarDesign.addAction(self.actionSave)
        self.toolBarDesign.addAction(self.actionLoad)
        self.toolBarDesign.addAction(self.action_full_refresh)
        self.toolBarDesign.addAction(self.actionRebuild)
        self.toolBarDesign.addAction(self.actionDelete_All)
        self.toolBarView.addAction(self.actionDesign)
        self.toolBarView.addAction(self.actionNewComponent)
        self.toolBarView.addAction(self.actionComponent)
        self.toolBarView.addAction(self.actionConnectors)
        self.toolBarView.addAction(self.actionLog)
        self.toolBarView.addAction(self.actionElements)
        self.toolBarView.addSeparator()
        self.toolBarView.addAction(self.actionScreenshot)
        self.toolBarView.addAction(self.actionFull_Screen)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.actionElements.toggled['bool'].connect(MainWindow._set_element_tab)
        self.actionDelete_All.triggered.connect(MainWindow.delete_all_components)
        self.actionLoad.triggered.connect(MainWindow.load_design)
        self.actionSave.triggered.connect(MainWindow.save_design)
        self.actionStyleDark.triggered.connect(MainWindow.load_stylesheet_dark)
        self.actionStyleDefault.triggered.connect(MainWindow.load_stylesheet_default)
        self.actionScreenshot.triggered.connect(MainWindow._screenshot)
        self.actionStyleOpen.triggered.connect(MainWindow.load_stylesheet_open)
        self.action_full_refresh.triggered.connect(MainWindow.full_refresh)
        self.actionRebuild.triggered.connect(MainWindow.rebuild)
        self.actionFull_Screen.triggered.connect(MainWindow.showFullScreen)
        self.actionMetal_Dark.triggered.connect(MainWindow.load_stylesheet_metal_dark)
        self.dockDesign.visibilityChanged['bool'].connect(self.actionDesign.setChecked)
        self.actionDesign.triggered['bool'].connect(self.dockDesign.setVisible)
        self.actionComponent.triggered['bool'].connect(self.dockComponent.setVisible)
        self.dockConnectors.visibilityChanged['bool'].connect(self.actionConnectors.setChecked)
        self.dockLog.visibilityChanged['bool'].connect(self.actionLog.setChecked)
        self.dockComponent.visibilityChanged['bool'].connect(self.actionComponent.setChecked)
        self.dockNewComponent.visibilityChanged['bool'].connect(self.actionNewComponent.setChecked)
        self.actionNewComponent.triggered['bool'].connect(self.dockNewComponent.setVisible)
        self.actionLog.triggered['bool'].connect(self.dockLog.setVisible)
        self.actionConnectors.triggered['bool'].connect(self.dockConnectors.setVisible)
        self.actionDesign.triggered.connect(self.dockDesign.raise_)
        self.actionConnectors.triggered.connect(self.dockConnectors.raise_)
        self.actionNewComponent.triggered.connect(self.dockNewComponent.raise_)
        self.actionComponent.triggered.connect(self.dockComponent.raise_)
        self.actionElements.triggered.connect(self.tabWidget.setFocus)
        self.actionLog.triggered.connect(self.dockLog.raise_)
        self.actionSaveAs.toggled['bool'].connect(MainWindow.save_design_as)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Qiskit Metal: Quantum Creator"))
        MainWindow.setToolTip(_translate("MainWindow", "Qiskit Metal: Quantum Creator"))
        MainWindow.setStatusTip(_translate("MainWindow", "Qiskit Metal: Quantum Creator"))
        MainWindow.setWhatsThis(_translate("MainWindow", "Qiskit Metal: Quantum Creator"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mainViewTab), _translate("MainWindow", "Main View"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabElements), _translate("MainWindow", "Elements"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabElements), _translate("MainWindow", "Shoe the tables of elements of the the design"))
        self.menuDesign.setToolTip(_translate("MainWindow", "Design Menu"))
        self.menuDesign.setStatusTip(_translate("MainWindow", "Design Menu"))
        self.menuDesign.setWhatsThis(_translate("MainWindow", "Design Menu"))
        self.menuDesign.setTitle(_translate("MainWindow", "Design"))
        self.menuView.setTitle(_translate("MainWindow", "Window"))
        self.menuStylesheet.setTitle(_translate("MainWindow", "Theme"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.menuRender.setTitle(_translate("MainWindow", "Render"))
        self.menuHelp.setToolTip(_translate("MainWindow", "Open Metal Help"))
        self.menuHelp.setStatusTip(_translate("MainWindow", "Open Metal Help"))
        self.menuHelp.setWhatsThis(_translate("MainWindow", "Open Metal Help"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot"))
        self.toolBarDesign.setWindowTitle(_translate("MainWindow", "Design toolbar"))
        self.toolBarDesign.setStatusTip(_translate("MainWindow", "Design toolbar"))
        self.toolBarDesign.setWhatsThis(_translate("MainWindow", "Design toolbar"))
        self.toolBarView.setWindowTitle(_translate("MainWindow", "View Toolbar"))
        self.toolBarView.setToolTip(_translate("MainWindow", "View Toolbar"))
        self.toolBarView.setStatusTip(_translate("MainWindow", "View Toolbar"))
        self.toolBarView.setWhatsThis(_translate("MainWindow", "View Toolbar"))
        self.dockDesign.setToolTip(_translate("MainWindow", "Design Dock"))
        self.dockDesign.setStatusTip(_translate("MainWindow", "Design Dock"))
        self.dockDesign.setWhatsThis(_translate("MainWindow", "Design Dock"))
        self.dockDesign.setAccessibleName(_translate("MainWindow", "Design Dock"))
        self.dockDesign.setAccessibleDescription(_translate("MainWindow", "Design Dock"))
        self.dockDesign.setWindowTitle(_translate("MainWindow", "Components in design"))
        self.btn_comp_zoom.setToolTip(_translate("MainWindow", "Focus on component in drawing window"))
        self.btn_comp_zoom.setStatusTip(_translate("MainWindow", "Focus on component in drawing window"))
        self.btn_comp_zoom.setText(_translate("MainWindow", "Focus on component in drawing window"))
        self.btn_comp_actions.setText(_translate("MainWindow", "Actions"))
        self.btn_comp_del.setToolTip(_translate("MainWindow", "Delete a selected component"))
        self.btn_comp_del.setStatusTip(_translate("MainWindow", "Delete a selected component"))
        self.btn_comp_del.setWhatsThis(_translate("MainWindow", "Delete a selected component"))
        self.btn_comp_del.setText(_translate("MainWindow", "Delete"))
        self.filter_text_design.setPlaceholderText(_translate("MainWindow", "Filter"))
        self.dockNewComponent.setToolTip(_translate("MainWindow", "Library of components"))
        self.dockNewComponent.setStatusTip(_translate("MainWindow", "Library design components"))
        self.dockNewComponent.setWhatsThis(_translate("MainWindow", "Library design components"))
        self.dockNewComponent.setWindowTitle(_translate("MainWindow", "Library design components"))
        self.filter_text_component.setPlaceholderText(_translate("MainWindow", "Filter"))
        self.treeWidget.setSortingEnabled(True)
        self.dockComponent.setWindowTitle(_translate("MainWindow", "Edit component"))
        self.dockLog.setToolTip(_translate("MainWindow", "Log window"))
        self.dockLog.setStatusTip(_translate("MainWindow", "Log window"))
        self.dockLog.setWhatsThis(_translate("MainWindow", "Log window"))
        self.dockLog.setWindowTitle(_translate("MainWindow", "Log"))
        self.log_text.setDocumentTitle(_translate("MainWindow", "Log"))
        self.dockConnectors.setWindowTitle(_translate("MainWindow", "Connectors"))
        self.text_filter_connectors.setPlaceholderText(_translate("MainWindow", "Filter"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Save design to file"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save design to file"))
        self.actionSave.setWhatsThis(_translate("MainWindow", "Save design to file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionLoad.setToolTip(_translate("MainWindow", "Load design from file"))
        self.actionLoad.setStatusTip(_translate("MainWindow", "Load design from file"))
        self.actionLoad.setWhatsThis(_translate("MainWindow", "Load design from file"))
        self.actionLoad.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionDesign.setText(_translate("MainWindow", "Design"))
        self.actionComponent.setText(_translate("MainWindow", "Edit"))
        self.actionComponent.setToolTip(_translate("MainWindow", "Edit a cdesign component"))
        self.actionComponent.setStatusTip(_translate("MainWindow", "Edit a cdesign component"))
        self.actionComponent.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionElements.setText(_translate("MainWindow", "Elements"))
        self.actionLog.setText(_translate("MainWindow", "Log"))
        self.actionNewComponent.setText(_translate("MainWindow", "Create"))
        self.actionNewComponent.setToolTip(_translate("MainWindow", "Create new component: Library of new design components you can create"))
        self.actionNewComponent.setStatusTip(_translate("MainWindow", "Create new component: Library of new design components you can create"))
        self.actionNewComponent.setWhatsThis(_translate("MainWindow", "Create new component: Library of new design components you can create"))
        self.actionDelete_All.setText(_translate("MainWindow", "Delete all"))
        self.actionDelete_All.setToolTip(_translate("MainWindow", "Delete All Component Objects and Elements"))
        self.actionDelete_All.setStatusTip(_translate("MainWindow", "Delete All Component Objects and Elements"))
        self.actionDelete_All.setWhatsThis(_translate("MainWindow", "Delete All Component Objects and Elements"))
        self.actionZoom.setText(_translate("MainWindow", "Zoom"))
        self.actionZoom.setToolTip(_translate("MainWindow", "Zoom control"))
        self.actionZoom.setShortcut(_translate("MainWindow", "Z"))
        self.actionPan.setText(_translate("MainWindow", "Pan"))
        self.actionPan.setShortcut(_translate("MainWindow", "P"))
        self.actionConnectors.setText(_translate("MainWindow", "Connectors"))
        self.actionConnectors.setToolTip(_translate("MainWindow", "Show connectors"))
        self.actionConnectors.setShortcut(_translate("MainWindow", "C"))
        self.actionStyleOpen.setText(_translate("MainWindow", "Open File"))
        self.actionStyleDefault.setText(_translate("MainWindow", "System default"))
        self.actionStyleDark.setText(_translate("MainWindow", "Q Dark"))
        self.actionScreenshot.setText(_translate("MainWindow", "Screenshot"))
        self.actionScreenshot.setToolTip(_translate("MainWindow", "Take a screenshot of the window"))
        self.action_full_refresh.setText(_translate("MainWindow", "Refresh"))
        self.action_full_refresh.setToolTip(_translate("MainWindow", "Force a full refresh of all plots and widgets"))
        self.action_full_refresh.setStatusTip(_translate("MainWindow", "Force a full refresh of all plots and widgets"))
        self.action_full_refresh.setWhatsThis(_translate("MainWindow", "Force a full refresh of all plots and widgets"))
        self.action_full_refresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionRebuild.setText(_translate("MainWindow", "Rebuild"))
        self.actionRebuild.setToolTip(_translate("MainWindow", "Force rebuild all components"))
        self.actionRebuild.setStatusTip(_translate("MainWindow", "Force rebuild all components"))
        self.actionRebuild.setWhatsThis(_translate("MainWindow", "Force rebuild all components"))
        self.actionRebuild.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.actionFull_Screen.setText(_translate("MainWindow", "Full Screen"))
        self.actionFull_Screen.setToolTip(_translate("MainWindow", "Go to full screen"))
        self.actionMetal_Dark.setText(_translate("MainWindow", "Metal Dark"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save as"))
        self.actionSaveAs.setToolTip(_translate("MainWindow", "Save design to new file"))
        self.actionSaveAs.setStatusTip(_translate("MainWindow", "Save design to file"))
        self.actionSaveAs.setWhatsThis(_translate("MainWindow", "Save design to file"))
        self.actionSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
from .widgets.log_metal import LoggingWindowWidget
from .widgets.table_components import TableComponents
from . import main_window_rc_rc
