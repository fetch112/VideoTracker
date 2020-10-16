import cv2
import numpy as np

video_path ='D:/개인용폴더/데스크탑/비디오영상/Primitive Technology- Round hut.mp4'
cap=cv2.VideoCapture(video_path)
if not cap.isOpened():
    exit()
tracker = cv2.TrackerCSRT_create()
ret, img = cap.read() #첫번째 프레임 읽기
cv2.namedWindow("select window")
cv2.imshow("select window",img)

##setting ROI 내가 선택한 영역 저장
rect= cv2.selectROI("select window",img, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("select window")
# initialize  tracker
tracker.init(img,rect)
## 실행##


while True:

    ret, img= cap.read() #1프레임씩 읽기
    if not ret:
        exit()
    tracker.init(img,rect)
    success, box = tracker.update(img)
    left, top, w, h =[int(v) for v in box]
    cv2.rectangle(img, pt1=(left,top), pt2=(left+w, top + h), color=(255,255,0),
                    thickness=3)
    cv2.imshow("img",img)
    if cv2.waitKey(1)==ord('q'):
        break

    

