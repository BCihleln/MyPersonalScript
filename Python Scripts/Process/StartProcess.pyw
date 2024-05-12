import os

def StartProcessOnWindows(TargetList:list):
    for TargetProcess in TargetList:
        with os.popen(f"start {TargetProcess} > NUL") as p:
            result=p.readlines()
