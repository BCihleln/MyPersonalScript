from time import sleep
import winsound

def Notify(duration = 250,times = 1,freq = 800):
    """
    Duration:聲音長度毫秒為單位
    Freq:頻率，Hz爲單位
    """
    for i in range(0,times):
        winsound.Beep(freq, duration)   #叮~~~
        sleep(0.01)