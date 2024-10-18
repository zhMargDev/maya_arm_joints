import pymel.core as pm

from PySide2 import QtCore, QtWidgets

main_joint = "Arm"

joints = ["ForeArm", "Hand"]

keys = ['pinkies', 'rings', 'middls', 'indexes', 'thumbs']

values = {
    'pinkies': [
        {
            "name": "HandPinky",
            "x_pos": 2.747,
            "y_pos": -0.018,
            "z_pos": -2.523
        },
        {
            "name": "HandPinky1",
            "x_pos": 5.53,
            "y_pos": 0.612,
            "z_pos": 0.115
        },
        {
            "name": "HandPinky2",
            "x_pos": 2.92,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandPinky3",
            "x_pos": 2.245,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandPinky4",
            "x_pos": 2.207,
            "y_pos": 0,
            "z_pos": 0
        },
    ],
    'rings': [
        {
            "name": "HandRing",
            "x_pos": 3.096,
            "y_pos": 0.12,
            "z_pos": -1.182
        },
        {
            "name": "HandRing1",
            "x_pos": 6.003,
            "y_pos": 0.516,
            "z_pos": -0.005
        },
        {
            "name": "HandRing2",
            "x_pos": 3.958,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandRing3",
            "x_pos": 2.718,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandRing4",
            "x_pos": 2.583,
            "y_pos": 0,
            "z_pos": 0
        },
    ],
    'middls': [
        {
            "name": "HandMiddle",
            "x_pos": 3.282,
            "y_pos": 0.127,
            "z_pos": 0.169
        },
        {
            "name": "HandMiddle1",
            "x_pos": 6.395,
            "y_pos": -0.045,
            "z_pos": 0.186
        },
        {
            "name": "HandMiddle2",
            "x_pos": 4.415,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandMiddle3",
            "x_pos": 2.985,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandMiddle4",
            "x_pos": 2.666,
            "y_pos": 0,
            "z_pos": 0
        },
    ],
    'indexes': [
        {
            "name": "HandIndex",
            "x_pos": 3.056,
            "y_pos": -0.338,
            "z_pos": 1.505
        },
        {
            "name": "HandIndex1",
            "x_pos": 5.356,
            "y_pos": -0.102,
            "z_pos": 0.241
        },
        {
            "name": "HandIndex2",
            "x_pos": 4.368,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandIndex3",
            "x_pos": 2.499,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandIndex4",
            "x_pos": 2.468,
            "y_pos": 0,
            "z_pos": 0
        },
    ],
    'thumbs': [
        {
            "name": "HandThumbs",
            "x_pos": 1.26,
            "y_pos": -2.188,
            "z_pos": 2.094
        },
        {
            "name": "HandThumbs1",
            "x_pos": 4.467,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandThumbs2",
            "x_pos": 3.825,
            "y_pos": 0,
            "z_pos": 0
        },
        {
            "name": "HandThumbs3",
            "x_pos": 3.358,
            "y_pos": 0,
            "z_pos": 0
        },
    ]
}

class CreateArm:
    def __init__(self, arm_type_req):
        # Cleare all selections
        cmds.select(clear=True)
        self.arm_type = arm_type_req

        global joints, keys, values, main_joint

        self.main_joint = self.arm_type + main_joint
        self.joints = joints
        self.keys = keys
        self.values = values

        check_joints_exists = self.check_joints_names()

        if not check_joints_exists:
            self.create_main_joints()
        else:
            cmds.warning(check_joints_exists + ' joints already exist.')

    def create_main_joints(self):

        cmds.joint(name=self.main_joint)
        # Set arm position by left or right

        if self.arm_type == 'Left':
            self.setArmPositions(0, 30)
        elif self.arm_type == 'Right':
            self.setArmPositions(180, -30)

        # Ciret all joints
        for el in self.joints:
            cmds.joint(name=self.arm_type + el)

        #Set tranlate X to els
        cmds.setAttr(self.main_joint + "|" + self.arm_type + "ForeArm.translateX", 28)
        cmds.setAttr(self.main_joint + "|" + self.arm_type + "ForeArm|" + self.arm_type + "Hand.translateX", 25)

        for key in self.keys:
            self.create_joints(key)

    def create_joints(self, key):
        path = self.main_joint + "|" + self.arm_type + "ForeArm|" + self.arm_type + "Hand"

        #Create rings
        for value in self.values[key]:
            cmds.joint(name=self.arm_type + value["name"])
            #Set value parent
            if path == self.main_joint + "|" + self.arm_type + "ForeArm|" + self.arm_type + "Hand" and self.arm_type + value["name"] != self.arm_type + "HandPinky" :
                cmds.parent(self.arm_type + value["name"], path)
            # Set X pos
            cmds.setAttr(path + '|' + self.arm_type + value["name"] + '.translateX', value["x_pos"])
            cmds.setAttr(path + '|' + self.arm_type + value["name"] + '.translateY', value["y_pos"])
            cmds.setAttr(path + '|' + self.arm_type + value["name"] + '.translateZ', value["z_pos"])

            path = path + '|' + self.arm_type + value["name"]
    
    def setArmPositions(self, rotate_z, translate_x):
        # Set arm left position if arm is exists
        if cmds.objExists(self.main_joint):
            cmds.setAttr(self.main_joint + ".rotateZ", rotate_z)
            cmds.setAttr(self.main_joint + ".translateX", translate_x)

    def check_joints_names(self):
        if cmds.objExists(self.main_joint):
            return self.main_joint
        
        for joint in self.joints:
            if cmds.objExists(self.arm_type + joint):
                return self.arm_type + joint
        
        for key in self.keys:
            for value in self.values[key]:
                if cmds.objExists(self.arm_type + value["name"]):
                    return self.arm_type + value["name"]
        
        return  False

class OrienteJoints:
    def __init__(self, arm_type_req):

        # Cleare all selections
        cmds.select(clear=True)
        self.arm_type = arm_type_req

        global joints, keys, values, main_joint

        self.main_joint = self.arm_type + main_joint
        self.joints = joints
        self.keys = keys
        self.values = values

        check_joints_exists = self.check_joints_exists()

        if not check_joints_exists:
            self.dump_joints_from_parents()
            self.orient_joints()
            self.build_joints_hierarchy()
        else:
            cmds.warning(check_joints_exists + ' joint is not found.')

    def check_joints_exists(self):
        # Check if all joints exists
        cmds.select(clear=True)

        if not cmds.objExists(self.main_joint):
            return self.main_joint
        
        for joint in self.joints:
            if not cmds.objExists(self.arm_type + joint):
                return self.arm_type + joint
        
        for key in self.keys:
            for value in self.values[key]:
                if not cmds.objExists(self.arm_type + value["name"]):
                    return self.arm_type + value["name"]
        
        return  False

    def dump_joints_from_parents(self):
        cmds.select(clear=True)

        for joint in self.joints:
            if cmds.objExists(self.arm_type + joint):
                # Check if the joint is already a root joint
                if cmds.listRelatives(self.arm_type + joint, parent=True) is None:
                    continue
                cmds.parent(self.arm_type + joint, world=True)

        for key in self.keys:
            for value in self.values[key]:
                if cmds.objExists(self.arm_type + value["name"]):
                    # Check if the joint is already a root joint
                    if cmds.listRelatives(self.arm_type + value["name"], parent=True) is None:
                        continue
                    cmds.parent(self.arm_type + value["name"], world=True)

    def build_joints_hierarchy(self):
        cmds.select(clear=True)

        parent = self.main_joint

        for joint in self.joints:
            if cmds.objExists(self.arm_type + joint):
                cmds.parent(self.arm_type + joint, parent)
                parent = self.arm_type + joint
        
        hand_parent = parent
        
        for key in self.keys:
            for index, value in enumerate(self.values[key]):
                if cmds.objExists(self.arm_type + value["name"]):
                    if index == 0:
                        cmds.parent(self.arm_type + value["name"], hand_parent)
                    else:
                        cmds.parent(self.arm_type + value["name"], parent)

                    parent = self.arm_type + value["name"]

    def orient_joints(self):
        # Создаем список всех суставов руки
        joints = [self.main_joint]
        for joint in self.joints:
            joints.append(self.arm_type + joint)
        for key in self.keys:
            for value in self.values[key]:
                joints.append(self.arm_type + value["name"])

        # Проходим по каждому суставу в списке
        for i in range(len(joints) - 1):
            # Создаем aim constraint между текущим суставом и следующим
            aim_constraint = pm.aimConstraint(joints[i + 1], joints[i], aimVector=[1, 0, 0], upVector=[0, 1, 0], worldUpType="scene")
            # Удаляем aim constraint
            pm.delete(aim_constraint)

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
        """
        orient left arm joints
    
        print(True)
        # Создаем список всех суставов левой руки
        joints = [self.leftArm.main_joint] + self.leftArm.joints
        # Проходим по каждому суставу в списке
        for i in range(len(joints) - 1):
            # Устанавливаем ориентацию текущего сустава
            pm.joint(joints[i], e=True, oj='xyz', secondaryAxisOrient='yup', zso=True, ch=True)
            # Устанавливаем ориентацию следующего сустава
            pm.joint(joints[i+1], e=True, oj='xyz', secondaryAxisOrient='yup', zso=True)
        """

        self.orientLeftArm = OrienteJoints('Left')


    def orientRightArmJoints(self):
        """
        orient right arm joints
        # Создаем список всех суставов правой руки
        joints = [self.rightArm.main_joint] + self.rightArm.joints
        # Проходим по каждому суставу в списке
        for i in range(len(joints) - 1):
            # Устанавливаем ориентацию текущего сустава
            pm.joint(joints[i], e=True, oj='xyz', secondaryAxisOrient='yup', zso=True, ch=True)
            # Устанавливаем ориентацию следующего сустава
            pm.joint(joints[i+1], e=True, oj='xyz', secondaryAxisOrient='yup', zso=True)
        """

        self.orientLeftArm = OrienteJoints('Right')

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