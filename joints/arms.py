import maya.cmds as cmds

class LeftArm:
    def __init__(self):
        self.joints = ["LeftArm","LeftForeArm", "LeftHand"]

        self.keys = ['pinkies', 'rings', 'middls', 'indexes', 'thumbs']

        self.values = {
                'pinkies': [
                    {
                        "name": "LeftHandPinky", 
                        "x_pos": 2.747,
                        "y_pos": -0.018,
                        "z_pos": -2.523
                    },
                    {
                        "name": "LeftHandPinky1", 
                        "x_pos": 5.53,
                        "y_pos": 0.612,
                        "z_pos": 0.115
                    },
                    {
                        "name": "LeftHandPinky2", 
                        "x_pos": 2.92,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandPinky3", 
                        "x_pos": 2.245,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandPinky4", 
                        "x_pos": 2.207,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'rings': [
                    {
                        "name": "LeftHandRing", 
                        "x_pos": 3.096,
                        "y_pos": 0.12,
                        "z_pos": -1.182
                    },
                    {
                        "name": "LeftHandRing1", 
                        "x_pos": 6.003,
                        "y_pos": 0.516,
                        "z_pos": -0.005
                    },
                    {
                        "name": "LeftHandRing2", 
                        "x_pos": 3.958,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandRing3", 
                        "x_pos": 2.718,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandRing4", 
                        "x_pos": 2.583,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'middls': [
                    {
                        "name": "LeftHandMiddle", 
                        "x_pos": 3.282,
                        "y_pos": 0.127,
                        "z_pos": 0.169
                    },
                    {
                        "name": "LeftHandMiddle1", 
                        "x_pos": 6.395,
                        "y_pos": -0.045,
                        "z_pos": 0.186
                    },
                    {
                        "name": "LeftHandMiddle2", 
                        "x_pos": 4.415,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandMiddle3", 
                        "x_pos": 2.985,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandMiddle4", 
                        "x_pos": 2.666,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'indexes': [
                    {
                        "name": "LeftHandIndex", 
                        "x_pos": 3.056,
                        "y_pos": -0.338,
                        "z_pos": 1.505
                    },
                    {
                        "name": "LeftHandIndex1", 
                        "x_pos": 5.356,
                        "y_pos": -0.102,
                        "z_pos": 0.241
                    },
                    {
                        "name": "LeftHandIndex2", 
                        "x_pos": 4.368,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandIndex3", 
                        "x_pos": 2.499,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandIndex4", 
                        "x_pos": 2.468,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ],
                'thumbs': [
                    {
                        "name": "LeftHandThumbs", 
                        "x_pos": 1.26,
                        "y_pos": -2.188,
                        "z_pos": 2.094
                    },
                    {
                        "name": "LeftHandThumbs1", 
                        "x_pos": 4.467,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandThumbs2", 
                        "x_pos": 3.825,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                    {
                        "name": "LeftHandThumbs3", 
                        "x_pos": 3.358,
                        "y_pos": 0,
                        "z_pos": 0
                    },
                ]
            }

        self.create_main_joints()

    def create_main_joints(self):
        # Ciret all joints
        for el in self.joints:
            cmds.joint(name=el)

        #Set tranlate X to els
        cmds.setAttr("LeftArm|LeftForeArm.translateX", 28)
        cmds.setAttr("LeftArm|LeftForeArm|LeftHand.translateX", 25)

        for key in self.keys:
            self.create_joints(key)
    
    def create_joints(self, key):
        path = "LeftArm|LeftForeArm|LeftHand"
        
        #Create rings
        for value in self.values[key]:
            cmds.joint(name=value["name"])
            #Set value parent
            if path == "LeftArm|LeftForeArm|LeftHand" and value["name"] != "LeftHandPinky" :
                cmds.parent(value["name"], path)
            # Set X pos
            cmds.setAttr(path + '|' + value["name"] + '.translateX', value["x_pos"])
            cmds.setAttr(path + '|' + value["name"] + '.translateY', value["y_pos"])
            cmds.setAttr(path + '|' + value["name"] + '.translateZ', value["z_pos"])

            path = path + '|' + value["name"]
