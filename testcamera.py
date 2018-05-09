__author__ = 'yinchuandong'

import cv2
from face import FaceDetect

model = FaceDetect()

capture = cv2.VideoCapture(0) # cv2.VideoCapture('clocka.avi') #

#获得码率及尺寸
# fps = videoCapture.get(cv2.CAP_PROP_FPS)
# size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDT)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
width = int(capture.get(3))
height = int(capture.get(4))
fps = int(capture.get(5))
size = (width, height)

#指定写视频的格式, I420-avi, MJPG-mp4
# videoWriter = cv2.VideoWriter('oto_other.mp4', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, size)
videoWriter = cv2.VideoWriter("VideoTest.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 30, size)

# # cv2.VideoWriter()第二个参数设置为-1，程序运行时则会交互地弹出一个对话框让你从系统已有的编码中选择一个。
# v = cv2.VideoWriter('bb.avi', -1, fps, size)
# print (fps, size,'v->',v)
#读帧 生成视频
success, frame = capture.read()
print (success, fps, size,'v->', videoWriter)

while success :
    cv2.imshow("Video Test", frame) #显示
    cv2.waitKey(1000) # 延迟
    videoWriter.write(frame) # 写视频帧
    success, frame = capture.read() # 获取下一帧

# 抓拍 保存照片
print (capture.isOpened())
num = 0
while True:
    ret, img = capture.read()
    imgArr = model.detect(img)
    for img in imgArr:
        # video.write(img)
        cv2.imshow('Video', img)
        key = cv2.waitKey(1)
        cv2.imwrite('camera/%s.jpg' % (str(num)), img)
        num = num + 1
        if key == ord('q'):
            break

# video.release()
capture.release()
cv2.destroyAllWindows()
