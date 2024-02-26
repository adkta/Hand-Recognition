import mediapipe as np
import cv2


class handDetector():
    def __init__(self, mode= False, maxHands= 2, detectionCon= 0.5, trackCon= 0.5):
        self.mode= mode
        self.maxHands= maxHands
        self.detectionCon= detectionCon
        self.trackCon= trackCon


        self.npHands= np.solutions.hands
        self.hands= self.npHands.Hands(self.mode, self.maxHands,1,self.detectionCon, self.trackCon)

        self.npDraw= np.solutions.drawing_utils

    def findHands(self, img, draw= True):
        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results= self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handlns in self.results.multi_hand_landmarks:
                if draw:
                    self.npDraw.draw_landmarks(img, handlns, self.npHands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo=0, draw= True):
        lnlist= []
        if self.results.multi_hand_landmarks:
            myHand= self.results.multi_hand_landmarks[handNo]
            for id, ln in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy= int(ln.x*w), int(ln.y*h)
                lnlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 7, (255,0,255), cv2.FILLED)
        return lnlist


'''
def main():
    pTime=0
    cTime=0
    cap= cv2.VideoCapture(0)
    img= detector= handDetector()
    while True:
        success, img= cap.read()
        img= detector.findHands(img)
        lnlist= detector.findPosition(img)
        if len(lnlist) !=0:
            print(lnlist[4])
        cTime= time.time()
        fps= 1/(cTime-pTime)
        pTime= cTime

        cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
if __name__== "__main__":
    main()'''