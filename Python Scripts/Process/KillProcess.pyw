import os

# Forced Stop the process and its subprocess
def KillProcessOnWindows(TargetList:list):
    # Only works for Windows
    # see more detail by "taskkill /?" in CMD
    # Need to add gsudo program to path
    # gsudo : https://github.com/gerardog/gsudo
    for TargetProcess in TargetList: 
        result=""
        with os.popen(f"gsudo taskkill -f -im {TargetProcess} -t > NUL") as p:
            # None
            result = p.readlines()