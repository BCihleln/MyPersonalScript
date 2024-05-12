# 調用攝像頭，檢測人臉並用圖片覆蓋
# Arranged from 
#   https://zhuanlan.zhihu.com/p/161217063 
#   https://www.jb51.net/article/238414.htm 
# Package need 
#   opencv-python, opencv-contrib-python

import cv2
if __name__ == '__main__':
    # 根据人脸特征的数据 获取人脸检测器
    face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
    # 读取覆盖图片
    Pic = cv2.imread('./head.png')
    # 获取摄像头行为
    cap = cv2.VideoCapture(0)

    while True:
        # 从摄像头中按帧返回图片
        flag,frame = cap.read()
        if not flag : # 没有图片时flag为False
            break
        # 将获取的图片置灰 检测效率高一些
        face_zones = face_detector\
            .detectMultiScale(cv2.cvtColor(frame,
                                           code=cv2.COLOR_BGR2GRAY))
        # 获取检测到的人脸区域
        # 若檢測到人臉，則返回坐標(x,y)寬高(w,h)，否則返回空
        for x,y,w,h in face_zones:
            Pic = cv2.resize(Pic,dsize = (w,h)) # 将该图片的大小重置为人脸的大小
            frame[y:y+h,x:x+w] = Pic # 将人脸显示区域 替换成覆盖的图片
        cv2.imshow('TestingWindow',frame) # 显示图片
        key = cv2.waitKey(10)
        if (key != -1): # 输入任意鍵退出读取
            break
    cv2.destroyAllWindows()
    cap.release()