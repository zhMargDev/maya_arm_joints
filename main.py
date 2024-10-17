import pymel.core as pm

from PyQt5 import QtCore, QtWidgets

from joints import arms

class RiggingTool(QtWidgets.QDialog):
    """docstring for RiggingTool"""
    def __init__(self):
        super(RiggingTool, self).__init__()

        self.build_ui()
        self.resize(300, 100)

    def build_ui(self):
        """
        building ui using QT widgets
        connecting button commands
        """
        self.setWindowTitle('Rigging Tool')
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.master_layout = QtWidgets.QVBoxLayout(self)

        # checkboxes
        self.chbLayout = QtWidgets.QHBoxLayout()

        self.leftArm = QtWidgets.QCheckBox('Left Arm')
        self.leftArm.setChecked(True)
        self.rightArm = QtWidgets.QCheckBox('Right Arm')

        self.chbLayout.addWidget(self.leftArm)
        self.chbLayout.addWidget(self.rightArm)

        # buttons
        self.btnLayout = QtWidgets.QHBoxLayout()

        self.createJointsBtn = QtWidgets.QPushButton('Create Arm Joints')
        self.createJointsBtn.clicked.connect(self.createJoints)
        self.orientJointsBtn = QtWidgets.QPushButton('Orient Joints')
        self.orientJointsBtn.clicked.connect(self.orientJoints)
        self.createRigBtn = QtWidgets.QPushButton('Create Rig')
        self.createRigBtn.clicked.connect(self.createRig)
        self.cancelBtn = QtWidgets.QPushButton('Cancel')
        self.cancelBtn.clicked.connect(self.close)

        self.btnLayout.addWidget(self.createJointsBtn)
        self.btnLayout.addWidget(self.orientJointsBtn)
        self.btnLayout.addWidget(self.createRigBtn)
        self.btnLayout.addWidget(self.cancelBtn)

        # ui master
        self.master_layout.addLayout(self.chbLayout)
        self.master_layout.addLayout(self.btnLayout)

    def createJoints(self):
        """
        create joints based on checkboxes
        """
        if self.leftArm.isChecked():
            self.createLeftArmJoints()
        if self.rightArm.isChecked():
            self.createRightArmJoints()

    def orientJoints(self):
        """
        orient joints based on checkboxes
        """
        if self.leftArm.isChecked():
            self.orientLeftArmJoints()
        if self.rightArm.isChecked():
            self.orientRightArmJoints()

    def createRig(self):
        """
        create rig based on checkboxes
        """
        if self.leftArm.isChecked():
            self.createLeftArmRig()
        if self.rightArm.isChecked():
            self.createRightArmRig()

    def createLeftArmJoints(self):
        # Implementation here
        leftArm = arms.LeftArm
        pass

    def createRightArmJoints(self):
        # Implementation here
        pass

    def orientLeftArmJoints(self):
        # Implementation here
        pass

    def orientRightArmJoints(self):
        # Implementation here
        pass

    def createLeftArmRig(self):
        # Implementation here
        pass

    def createRightArmRig(self):
        # Implementation here
        pass

ui = RiggingTool()
ui.show()