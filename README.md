***First step***

```
Upload this files and unpack zip
```
```
Move maya_arm_joints.py and joints folder to C:\user\username\documents\maya\2022\scripts\
```

**Second step**
```
Create a icon on maya

Then open script

Select Python

```

**Last step**
```
Write this code



import maya.cmds as cmds
import os

user_script_dir = cmds.internalVar(usd=True)
script_path = os.path.join(user_script_dir, "maya_arm_joints.py")

with open(script_path, 'r') as file:
    exec(file.read())
```