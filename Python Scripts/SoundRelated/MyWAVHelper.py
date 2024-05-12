import pyaudio
import wave
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt # 繪圖

CHUNK = 1024
FORMAT = pyaudio.paInt16
NCHANNELS = 1
SAMPWIDTH:None
FRAMERATE = 16000

def wavread(path):
    """
    讀取波形文件，并返回np數組與時間用以繪圖
    """
    wavfile =  wave.open(path,"rb")
    params = wavfile.getparams()
    NCHANNELS, SAMPWIDTH, FRAMERATE, frameswav = params[:4]
    datawav = wavfile.readframes(frameswav)
    wavfile.close()
    datause = np.frombuffer(datawav,dtype = np.int16)
    # datause = np.reshape(datause,[nframes,nchannels]).T # 根據聲道數轉置

    # datause.shape = -1,2 # 雙聲道時的取數據轉置方法
    # datause = datause.T

    time = np.arange(0, frameswav) * (1.0/FRAMERATE)
    return datause,time

def wavwrite(path,frames):
    wf = wave.open(path, 'wb')
    wf.setnchannels(NCHANNELS)
    wf.setsampwidth(pyaudio.get_sample_size(FORMAT))
    wf.setframerate(FRAMERATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def ShowWAVGraph(path,color='green'):
    """
    打印單個WAV文件波形圖
    """
    data,time = wavread(path)
    plt.title("Current WAV")
    plt.xlabel("Time")
    plt.ylabel("Frequency(Hz)")
    plt.plot(time,data,color=color)
    plt.show()
