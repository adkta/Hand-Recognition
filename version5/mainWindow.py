from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QImage, QPixmap
from ui_main import Ui_MainWindow

from cameraThread import CameraThread

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.signerBtn1.clicked.connect(self.buttonClicked)
        self.ui.speakerBtn1.clicked.connect(self.buttonClicked)
        self.ui.learnerBtn1.clicked.connect(self.buttonClicked)
        self.ui.signerBtn2.clicked.connect(self.btn)
        self.ui.speakerBtn2.clicked.connect(self.btn)
        self.ui.learnerBtn2.clicked.connect(self.btn)
        self.ui.feedback2.clicked.connect(self.btn)
        self.output= ''

    def buttonClicked(self):
        self.ui.firstScreen.setCurrentWidget(self.ui.SecondPage)

        btn= self.sender()
        name= btn.objectName()
        if name == "signerBtn1":            
            self.cam_thread= CameraThread()
            self.cam_thread.start()
            self.cam_thread.frame_update.connect(self.update_frame)
        elif name == "speakerBtn1":
            self.ui.secondScreen.setCurrentWidget(self.ui.speakerPage)
        elif name == "learnerBtn1":
            self.ui.secondScreen.setCurrentWidget(self.ui.learnerPage)
        

    def btn(self):
        bton= self.sender()
        name= bton.objectName()
        if name == "signerBtn2":
            self.ui.secondScreen.setCurrentWidget(self.ui.signerPage)
        else:
            if self.cam_thread.is_alive():
                
            if name == "speakerBtn2":
                self.ui.secondScreen.setCurrentWidget(self.ui.speakerPage)
                
            elif name == "learnerBtn2":
                self.ui.secondScreen.setCurrentWidget(self.ui.learnerPage)
            
    '''def read(self):
        audio_url= upload(filename)
        save_transcript(audio_url, filename)'''

    '''def record(self):

        audio= pyaudio.PyAudio()
        stream= audio.open(format= pyaudio.paInt16, channels=1, rate=44100, input= True, frames_per_buffer=1024)
        frames= []
        try:
            while True:
                data= stream.read(1024)
                frames.append(data)
        except KeyboardInterrupt:
            pass
        stream.close()
        audio.terminate()

        sound_file= wave.open("myrecording.wav","wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframereate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()'''
    
    def letter(self,x, y):
        if x==y[0]:
            return
        else:
            self.ui.outputLabel.setText(self.output+ y)    
    
    def update_frame(self, image):
        self.ui.cameraLabel.setPixmap(QPixmap.fromImage(image))
        self.output= self.ui.outputLabel.text()
        if self.cam_thread.msg != '':
            self.letter(self.output[-2], self.cam_thread.msg)
       
    def closeEvent(self, event):
        self.cam_thread.stop()
        event.accept()