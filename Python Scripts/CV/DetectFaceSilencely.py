import cv2
import time
import os

ScriptRoot = os.path.split(os.path.realpath(__file__))[0]
CV_FrontalFace_config_path =\
    os.path.join(ScriptRoot,'haarcascade_frontalface_alt.xml')

def DetectFaceSilencely(DetectTime:int = 5)-> bool:

    # 根据人脸特征的数据 获取人脸检测器
    face_detector =\
        cv2.CascadeClassifier(CV_FrontalFace_config_path)
    
    # 获取摄像头行为
    cap = cv2.VideoCapture(0)
    faceflag = False

    T1 = time.time()
    while True:
        # 从摄像头中按帧返回图片
        flag,frame = cap.read()
        if not flag : # 没有图片时flag为False
            break
        # 将获取的图片置灰 检测效率高一些
        face_zones = face_detector\
            .detectMultiScale(cv2.cvtColor(frame,
                                           code=cv2.COLOR_BGR2GRAY))
        T2 = time.time()
        if len(face_zones) > 0:
            faceflag = True
            break
        elif T2-T1 > DetectTime:
            break
    cap.release()
    return faceflag