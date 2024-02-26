import pyaudio
import wave

FRAME_PER_BUFFER= 3200
FORMAT= pyaudio.paInt16
CHANNELS= 1
RATE= 1600

p= pyaudio.PyAudio()
stream= p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAME_PER_BUFFER
)

seconds=6
frames= []
for i in range(0, int(RATE/FRAME_PER_BUFFER*seconds)):
    data= stream.read(FRAME_PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj= wave.open("output.wav","wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()
