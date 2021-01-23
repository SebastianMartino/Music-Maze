import pyaudio
import numpy as np
import wave
from freq_dict import freq_dict


class AudioFrequency:
	def __init__(self):
		self.CHUNK = 4096
		self.FORMAT = pyaudio.paInt16
		self.CHANNELS = 1
		self.RATE = 44100
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format = self.FORMAT, channels = self.CHANNELS, 
					rate = self.RATE, input = True, frames_per_buffer = self.CHUNK)

	def get_frequency(self):
		data = self.stream.read(self.CHUNK)
		indata = np.array(wave.struct.unpack("%dh"%(self.CHUNK), data))
		fftData=abs(np.fft.rfft(indata))**2

		#Sorts frequencies by amplitude
		temp = fftData.argsort()

		#The top 3 frequencies
		most_frequents = temp[-3:][::-1]

		#Top frequency
		top_freq = most_frequents[0]
		#if fftData[which[1]] < fftData[which[0]]:
			#print("NOT ENOUGH")
			#return -1
		
		frequency = top_freq*self.RATE/self.CHUNK
		#print("The freq is %f Hz." % (frequency))
		return frequency

	def get_note(self):
		frequency = self.get_frequency()
		print(freq_dict.get(int(frequency), "No note"))
		return freq_dict.get(int(frequency), "No note")

	def close(self):
		self.stream.close()
		self.p.terminate()

'''
How to use example

a = AudioFrequency()
while(1):
	f = a.get_frequency()
	note = a.get_note(f)
	if note != "No note":
		print(note)
'''