from Function.Get_Argv import Get_Argv
from Process.StartProcess import StartProcessOnWindows

# ProgramList = Get_Argv("Target Program")

ProgramList = ["steam"]
for i in range(0,len(ProgramList)):
    if not ProgramList[i].endswith(".exe"):
        ProgramList[i]+=".exe"

StartProcessOnWindows(ProgramList)