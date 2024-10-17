

def create_button():
    window = cmds.window(title="Arms_Joints")
    cmds.columnLayout()
    cmds.button(label="Run Script", command='import sys; sys.path.append("C:/Users/[Имя пользователя]/Documents/maya/scripts/maya_arm_joints"); execfile("main.py")')
    cmds.showWindow(window)

create_button()