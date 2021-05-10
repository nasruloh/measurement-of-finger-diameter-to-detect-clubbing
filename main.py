#Nasruloh
import cv2
cap = cv2.VideoCapture(0)
gambar =1
while(True):
    k = cv2.waitKey(1) & 0xff
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5),0)
    ret ,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
    contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
    x=[]
    y=[]
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(0,len(contours)):
        for j in range(0,len(contours[i])):
            x.append(contours[i][j][0][0])
            y.append(contours[i][j][0][1])
            
    if len(contours)>0:
        z=0.005*(max(x)-min(x))
        a=0.005*(max(y)-min(y))
        z="Diameter = "+str(z)+"cm"
        #a="Tinggi = "+str(a)+"cm"
        cv2.putText(frame,z,(10,30),font,1,(0,255,0),2,cv2.LINE_AA)
   # if  z == 0.6 :
      #  c="Jari Tabuh"
       # cv2.putText(frame,a,(100,200),font,1,(0,255,0),2,cv2.LINE_AA)
        
        #cv2.putText(frame,a,(100,300),font,1,(0,255,0),2,cv2.LINE_AA)
        cv2.imshow("gray",thresh)
        cv2.imshow("frame",frame)
        cv2.imshow("kill",gray)
 
    if k== ord('s'):
            fileN=str(gambar)+'_Jari.png'
            cv2.imwrite(fileN,frame)
            print (gambar)
            gambar = gambar+1
    
    if k == 27: # press 'ESC' to quit
        break
    
cap.release()
cv2.destroyAllWindows()
