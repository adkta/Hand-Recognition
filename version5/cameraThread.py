from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage, QPixmap
import cv2
import second as htm
from ui_main import Ui_MainWindow

class CameraThread(QThread):
    frame_update = Signal(QImage)
    
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.msg= ''


    def run(self):
        detector= htm.handDetector()
        tipIds= [4,8,12,16,20]
        while not self.isInterruptionRequested():            
            ret, self.frame = self.cap.read()
            if ret:
                self.frame= detector.findHands(self.frame)
                self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                self.frame = cv2.flip(self.frame,1)
                lnlist= detector.findPosition(self.frame, draw=False)

                if len(lnlist) != 0:
                    if (lnlist[8][2]> lnlist[7][2]) and (lnlist[12][2]>lnlist[11][2]) and (lnlist[16][2]> lnlist[15][2]):
                        if (lnlist[20][2]> lnlist[19][2]):
                            if (lnlist[4][1]>lnlist[3][1]):
                                self.msg= '\u091C '             #ja
                            else:
                                self.msg= '\u0938 '             #sa
                        else:
                            self.msg= '\u0921 '                 #da

                    elif (lnlist[20][2]> lnlist[18][2]) and (lnlist[16][2]> lnlist[14][2]) and (lnlist[12][2]> lnlist[10][2]):
                        if (lnlist[4][2]<lnlist[10][2]) and (lnlist[4][1]>lnlist[8][1]):
                            self.msg= '\u0915 '          #ka
                        elif (lnlist[8][2]<lnlist[10][2]):
                            if (lnlist[4][1]< lnlist[8][1]):
                                self.msg= '\u0917 '       #ga
                            else:
                                self.msg= '\u0916 '     #kha
                    elif (lnlist[12][1]> lnlist[11][1]) and (lnlist[16][1]> lnlist[15][1]):
                        if (lnlist[4][2]>lnlist[3][2]):
                            if (lnlist[20][1]< lnlist[10][1]):
                                self.msg= '\u0918 '     #gha
                            elif (lnlist[8][1]< lnlist[7][1] ):
                                self.msg= '\u0927 '     #dhanus dha
                            else:
                                self.msg= '\u0939 '     #ha
                        else:
                            if (lnlist[8][1]> lnlist[7][1]) and (lnlist[20][1]> lnlist[19][1]) and (lnlist[4][2]<lnlist[12][2]):
                                self.msg= '\u0932 '              #la
                    
                    elif (lnlist[8][2]<lnlist[7][2]) and (lnlist[12][2]<lnlist[11][2]):
                        if (lnlist[4][1]< lnlist[3][1]):
                            if (lnlist[20][2]> lnlist[19][2]):
                                if (lnlist[16][2]> lnlist[15][2]):
                                    self.msg= '\u092D '     #va
                                else:
                                    self.msg= '\u092E '     #ma
                            else:
                                self.msg= '\u092C '     #ba
                        elif (lnlist[16][2]<lnlist[15][2]):
                            self.msg= '\u091B '     #xa
                        
                image = QImage(self.frame, self.frame.shape[1], self.frame.shape[0], self.frame.strides[0], QImage.Format_RGB888)
                
                self.frame_update.emit(image)
            self.msleep(10)

    def stop(self):
        self.cap.release()
        self.terminate()
