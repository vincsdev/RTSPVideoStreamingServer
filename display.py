import os
from utils import *

class Display:
	def __init__(self, mode, files, names):
		self.files = files
		self.names = names
		if mode == "file":
			self.genFile()
		elif mode == "console":
			self.genConsole()
		else:
			print("Wrong mode")

	def genFile(self):
		print("./streams.txt generated")
		with open("streams.txt", 'w') as streams:
			streams.write("Correspondence between video file and rtsp url.\n")
			for f, n in zip(self.files, self.names):
				streams.write("file : " + os.path.basename(f) + "\t< - >\tstream : rtsp://" + getIP() + ":5454/" + n + '\n')
			streams.close()


	def genConsole(self):
		for f, n in zip(self.files, self.names):
			print("file : " + os.path.basename(f) + "\t< - >\tstream : rtsp://" + getIP() + ":5454/" + n)
