
from time import sleep
import random
from Function.Get_Argv import Get_Argv
from Process.FindProcess import FindProcessOnWindows
from Process.KillProcess import KillProcessOnWindows
from SoundRelated.NotificationSound import Notify
from CV.DetectFaceSilencely import DetectFaceSilencely

# Random Wait Time
START = 5
END = 20

# Face Detect Time
TIME = 10

# -------------------------#
ArgvList = Get_Argv("[Notify][Target Program List]")

# Turn NotifyFunction on or off
NotifyFunction:int = None
try:
    NotifyFunction = int(ArgvList[0])
except : # Didn't Get Arguments of NotifyFunction
    ProgramList = ArgvList
else:
    ProgramList = ArgvList[1:]

# -------------------------#



# Preprocess
for i in range(0,len(ProgramList)):
    if not ProgramList[i].endswith(".exe"):
        ProgramList[i]+=".exe"


result = FindProcessOnWindows(ProgramList)
# Process not Found or User isn't Look at the screen!
if (len(result) == 0 or DetectFaceSilencely(TIME) == False):
    exit()
else:
    if NotifyFunction == None:# Didn't Get Arguments of NotifyFunction
        Notify(duration=1000, times=3)
    elif NotifyFunction > 0: 
        Notify(duration=1000, times=NotifyFunction)
    else: pass # Do not Notify


# (Done)TODO: 在使用了pyw的情况下，仍弹出所需的信息窗口，可能得使用subprocess？
# 完全不打印信息只發出警示音好像也行，可能不需要修改了
# ResizeWindow(WindowWidth,WindowHeight)
# CenterMessage(Message,WindowWidth)


# Wait for Random seconds
closeTime = random.randrange(START, END)
# DisplayLoading(closeTime)
sleep(closeTime)

KillProcessOnWindows(result)

# os.system("pause")
