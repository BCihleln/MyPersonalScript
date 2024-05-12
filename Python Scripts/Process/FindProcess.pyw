STATUS = "RUN" 
# STATUS = "DEBUG"

import os

def FindProcessOnWindows(TargetList:list,STATUS:str = "RUN")->list:
    # Use os.popen instead of os.system to avoid flashing out CMD window
    # Use with ... as ... in order to close pipeline automatically
    ExistTargetList=[]
    for TargetProgram in TargetList:
        with os.popen(f"tasklist | findstr {TargetProgram}") as p:
            result = p.readlines()

            if len(result)>0:
                ExistTargetList.append(TargetProgram)

        if STATUS != "RUN": # Debug Mode
            from SoundRelated.NotificationSound import Notify

            if result: Notify(freq=800)
            else: Notify(freq = 400)

    return ExistTargetList