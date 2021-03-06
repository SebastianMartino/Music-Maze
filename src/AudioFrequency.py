import pyaudio
import numpy as np
import wave
from midi_dict import midi_dict
import aubio

class AudioFrequency:
	def __init__(self):
		self.buffer_size = 1024
		self.FORMAT = pyaudio.paFloat32
		self.CHANNELS = 1
		self.RATE = 44100
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(format = self.FORMAT, channels = self.CHANNELS, 
					rate = self.RATE, input = True, frames_per_buffer = self.buffer_size)

		self.tolerance = 0.5
		self.win_s = 4096
		self.hop_s = self.buffer_size 
		self.pitch_o = aubio.pitch("default", self.win_s, self.hop_s, self.RATE)
		self.pitch_o.set_unit("midi")
		self.pitch_o.set_tolerance(self.tolerance)

	def get_pitch(self):
		audiobuffer = self.stream.read(self.buffer_size, exception_on_overflow=False)
		signal = np.fromstring(audiobuffer, dtype=np.float32)
		pitch = self.pitch_o(signal)[0]
		return pitch


	def get_note(self):
		pitch = self.get_pitch()
		return midi_dict.get(int(pitch), "No note")

	def close(self):
		self.stream.close()
		self.p.terminate()