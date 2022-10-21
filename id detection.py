import cv2
import numpy as np
import cv2.aruco as aruco

Videocap=True
cap=cv2.VideoCapture(1)

main=cv2.imread("resources/aruco_0.png")

#defining function for finding aruco marker ids
def findaruco(main,marker_size=6,total_markers=250,draw=True):
    imggrey = cv2.cvtColor(main,cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f'DICT_5X5_250')
    arucodict = aruco.Dictionary_get(key)
    arucoparam = aruco.DetectorParameters_create()

    (corners,ids,rejected) = cv2.aruco.detectMarkers(main,arucodict,parameters=arucoparam,)
    
    
    for corner in corners:
        centerX = (corner[0][0][0] + corner[0][1][0] + corner[0][2][0] + corner[0][3][0]) / 4
        centerY = (corner[0][0][1] + corner[0][1][1] + corner[0][2][1] + corner[0][3][1]) / 4
        center = [int(centerX), int(centerY)]
        
        print(ids)
    
    if draw:
        aruco.drawDetectedMarkers(main,corners)
    
    return corners,ids 

while True:
    if Videocap:_,main=cap.read(0)
    else:
        main=cv2.imread("resources/aruco_0.png")
        #main=cv2.resize(main,(0,0),fx=0.4,fy=0.4)
    corners,ids=findaruco(main)
    if cv2.waitKey(1)==113:
        break
    cv2.imshow("main",main)





