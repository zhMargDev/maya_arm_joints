import pymel.core as pm

from PySide2 import QtCore, QtWidgets


class CreateArm:
    def __init__(self, arm_type_req):
        # Cleare all selections
        cmds.select(clear=True)
        self.arm_type = arm_type_req
        self.first_joint_name = self.arm_type + "Arm"

        self.joints = [self.arm_type + "ForeArm", self.arm_type + "Hand"]

        self.keys = ['pinkies', 'rings', 'middls', 'indexes', 'thumbs']

        self.values = {
                'pinkies': [
                    {
                        "name": self.arm_type + "HandPinky",
                        "x_pos": 2.747,
                        "y_pos": -0.018,
                        "z_pos": -2.523
                    },
                    {
                        "name": self.arm_type + "HandPinky1",
                        "x_pos": 5.53,
                        "y_pos": 0.612,
                        "z_pos": 0.115
                    },
                    {
                        "name": self.arm_type + "HandPinky2",
                        "x_pos": 2.92,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandPinky3",
                        "x_pos": 2.245,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandPinky4",
                        "x_pos": 2.207,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'rings': [
                    {
                        "name": self.arm_type + "HandRing",
                        "x_pos": 3.096,
                        "y_pos": 0.12,
                        "z_pos": -1.182
                    },
                    {
                        "name": self.arm_type + "HandRing1",
                        "x_pos": 6.003,
                        "y_pos": 0.516,
                        "z_pos": -0.005
                    },
                    {
                        "name": self.arm_type + "HandRing2",
                        "x_pos": 3.958,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandRing3",
                        "x_pos": 2.718,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandRing4",
                        "x_pos": 2.583,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'middls': [
                    {
                        "name": self.arm_type + "HandMiddle",
                        "x_pos": 3.282,
                        "y_pos": 0.127,
                        "z_pos": 0.169
                    },
                    {
                        "name": self.arm_type + "HandMiddle1",
                        "x_pos": 6.395,
                        "y_pos": -0.045,
                        "z_pos": 0.186
                    },
                    {
                        "name": self.arm_type + "HandMiddle2",
                        "x_pos": 4.415,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandMiddle3",
                        "x_pos": 2.985,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandMiddle4",
                        "x_pos": 2.666,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'indexes': [
                    {
                        "name": self.arm_type + "HandIndex",
                        "x_pos": 3.056,
                        "y_pos": -0.338,
                        "z_pos": 1.505
                    },
                    {
                        "name": self.arm_type + "HandIndex1",
                        "x_pos": 5.356,
                        "y_pos": -0.102,
                        "z_pos": 0.241
                    },
                    {
                        "name": self.arm_type + "HandIndex2",
                        "x_pos": 4.368,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandIndex3",
                        "x_pos": 2.499,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandIndex4",
                        "x_pos": 2.468,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'thumbs': [
                    {
                        "name": self.arm_type + "HandThumbs",
                        "x_pos": 1.26,
                        "y_pos": -2.188,
                        "z_pos": 2.094
                    },
                    {
                        "name": self.arm_type + "HandThumbs1",
                        "x_pos": 4.467,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandThumbs2",
                        "x_pos": 3.825,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": self.arm_type + "HandThumbs3",
                        "x_pos": 3.358,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ]
            }

        check_joints_exists = self.check_joints_names()

        if not check_joints_exists:
            self.create_main_joints()
        else:
            print(check_joints_exists + ' joints already exist.')
            cmds.warning(check_joints_exists + ' joints already exist.')

    def create_main_joints(self):
        self.first_joint_name = cmds.joint(name=self.first_joint_name)

        # Set arm position by left or right

        if self.arm_type == 'Left':
            self.setArmPositions(0, 30)
        elif self.arm_type == 'Right':
            self.setArmPositions(180, -30)

        # Ciret all joints
        for el in self.joints:
            cmds.joint(name=el)

        #Set tranlate X to els
        cmds.setAttr(self.first_joint_name + "|" + self.arm_type + "ForeArm.translateX", 28)
        cmds.setAttr(self.first_joint_name + "|" + self.arm_type + "ForeArm|" + self.arm_type + "Hand.translateX", 25)

        for key in self.keys:
            self.create_joints(key)

    def create_joints(self, key):
        path = self.first_joint_name + "|" + self.arm_type + "ForeArm|" + self.arm_type + "Hand"

        #Create rings
        for value in self.values[key]:
            cmds.joint(name=value["name"])
            #Set value parent
            if path == self.first_joint_name + "|" + self.arm_type + "ForeArm|" + self.arm_type + "Hand" and value["name"] != self.arm_type + "HandPinky" :
                cmds.parent(value["name"], path)
            # Set X pos
            cmds.setAttr(path + '|' + value["name"] + '.translateX', value["x_pos"])
            cmds.setAttr(path + '|' + value["name"] + '.translateY', value["y_pos"])
            cmds.setAttr(path + '|' + value["name"] + '.translateZ', value["z_pos"])

            path = path + '|' + value["name"]
    
    def setArmPositions(self, rotate_z, translate_x):
        # Set arm left position if arm is exists
        if cmds.objExists(self.first_joint_name):
            cmds.setAttr(self.first_joint_name + ".rotateZ", rotate_z)
            cmds.setAttr(self.first_joint_name + ".translateX", translate_x)

    def check_joints_names(self):
        if cmds.objExists(self.first_joint_name):
            return self.first_joint_name
        
        for joint in self.joints:
            if cmds.objExists(joint):
                return joint
        
        for key in keys:
            for value in self.values[key]:
                if cmds.objExists(value):
                    return value
        
        return  False

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

        self.leftArmCheckbox = QtWidgets.QCheckBox('Left Arm')
        self.leftArmCheckbox.setChecked(True)
        self.rightArmCheckbox = QtWidgets.QCheckBox('Right Arm')

        self.chbLayout.addWidget(self.leftArmCheckbox)
        self.chbLayout.addWidget(self.rightArmCheckbox)

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
        if self.leftArmCheckbox.isChecked():
            self.createLeftArmJoints()
        if self.rightArmCheckbox.isChecked():
            self.createRightArmJoints()

    def orientJoints(self):
        """
        orient joints based on checkboxes
        """
        if self.leftArmCheckbox.isChecked():
            self.orientLeftArmJoints()
        if self.rightArmCheckbox.isChecked():
            self.orientRightArmJoints()

    def createRig(self):
        """
        create rig based on checkboxes
        """
        if self.leftArmCheckbox.isChecked():
            self.createLeftArmRig()
        if self.rightArmCheckbox.isChecked():
            self.createRightArmRig()

    def createLeftArmJoints(self):
        # Implementation here
        self.leftArm = CreateArm('Left')
 
    def createRightArmJoints(self):
        # Implementation here
        self.rightArm = CreateArm('Right')

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


"""
nurbsCube -p 0 0 0 -ax 0 1 0 -w 1 -lr 1 -hr 1 -d 3 -u 1 -v 1 -ch 1; objectMoveCommand;
active Snap To points magnit
CV Curve Tool - 1 Linear

curve -d 1 -p -0.5 0.5 0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 0.5 0.5 -p -0.5 0.5 -0.5 -p 0.5 0.5 -0.5 -p 0.5 0.5 0.5 -p 0.5 -0.5 0.5 -p 0.5 -0.5 -0.5 -p 0.5 0.5 -0.5 -p -0.5 0.5 -0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p -0.5 -0.5 0.5 -p -0.5 -0.5 -0.5 -p 0.5 -0.5 -0.5 -p 0.5 -0.5 0.5 -p 0.5 0.5 0.5 -k 0 -k 1 -k 2 -k 3 -k 4 -k 5 -k 6 -k 7 -k 8 -k 9 -k 10 -k 11 -k 12 -k 13 -k 14 -k 15 -k 16 -k 17 -k 18 -k 19 ;


import maya.cmds as cmds

points = [
    (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, -0.5, 0.5),
    (-0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (0.5, 0.5, 0.5),
    (0.5, -0.5, 0.5), (0.5, -0.5, -0.5), (0.5, 0.5, -0.5), (0.5, -0.5, 0.5),
    (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, -0.5, 0.5), (-0.5, 0.5, -0.5),
    (0.5, 0.5, -0.5), (0.5, -0.5, -0.5), (-0.5, -0.5, -0.5), (-0.5, 0.5, -0.5)
]

degree = 1
knots = range(len(points))

cmds.curve(d=degree, p=points, k=knots)
"""