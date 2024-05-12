import os

def ResizeWindow(WindowWidth:int,WindowHeight:int):
    PrepareWindow = f'start /B mode con cols={WindowWidth} lines={WindowHeight}'
    os.system(PrepareWindow)
