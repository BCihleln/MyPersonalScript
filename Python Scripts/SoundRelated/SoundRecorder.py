import pyaudio
# import wave
# import numpy as np
from tqdm import tqdm #進度條包
from io import BytesIO

from utils.MyWAVHelper import wavwrite,FORMAT,NCHANNELS,FRAMERATE

CHUNK = 1024
RECORD_SECONDS = 2 #这个是录音时间长度，修改这个调整录音时间。


class SoundRecorder:

    __pyaudio:None
    __STREAM:None
    __WAV_buffer:None

    def __init__(self) -> None:
        print("Preparing Recorder")
        self.__pyaudio = pyaudio.PyAudio()
        # 打開聲卡，設置采樣深度、采樣率、聲道數、輸入、采樣點緩存數量
        self.__STREAM = self.__pyaudio.open(format=FORMAT,
                        channels=NCHANNELS,
                        rate=FRAMERATE,
                        input=True,
                        frames_per_buffer=CHUNK)
        self.__WAV_buffer = BytesIO() # 開闢一塊内存空間，用於將錄製的WAV音頻直接暫存至内存，並模擬成硬盤文件直接讀取
        print("..... Done !")

    def __del__(self) -> None:
        self.__STREAM.close()
        self.__pyaudio.terminate()
        self.__WAV_buffer.close()

    def RecordWAV(self):
        frames = [] # 用以存儲采樣到的數據

        # 以RECORD_SECOND秒數為區間錄製
        for i in tqdm(range(0, int(FRAMERATE / CHUNK * RECORD_SECONDS))):
            data = self.__STREAM.read(CHUNK) # 讀出聲卡緩存到的數據
            frames.append(data)


        # stream.stop_stream()
        
        # # 保存文件至硬盤
        # wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        # wf.setnchannels(NCHANNELS)
        # wf.setsampwidth(self.p.get_sample_size(FORMAT))
        # wf.setframerate(FRAMERATE)
        # wf.writeframes(b''.join(frames))
        # wf.close()
        # # (已完成)FIXME: 肯定有什麽方便的技巧能直接將wave格式修改在内存數組中，而不用寫入文件再讀取，以後再説

        # 保存至内存
        self.__WAV_buffer.seek(0) # 寫數據前重置“文件”指針，避免下次使用時出錯
        wavwrite(self.__WAV_buffer,frames)

        self.__WAV_buffer.seek(0) # 每次寫完數據後，需要重置“文件”指針！
        return self.__WAV_buffer
        
