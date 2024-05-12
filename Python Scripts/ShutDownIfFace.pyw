from CV.DetectFaceSilencely import DetectFaceSilencely
from subprocess import run
from SoundRelated.NotificationSound import Notify

if DetectFaceSilencely():
    Notify()
    run("shutdown /f /p",shell=True)
