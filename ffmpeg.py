import subprocess, shlex, threading
from utils import *

DEBUG = False

""" Class taking care to upload the videos with ffmpeg """

class FFMpeg:
	def __init__(self, videoFile, streamName, loop):
		self.videoFile = videoFile
		self.streamName = streamName
		self.loop = loop
		self.sprc = None
		self.upload()

	def upload(self):
		"""	Upload video """
		if self.loop == "loop":
			commandString = "ffmpeg -loglevel quiet -r 30 -re -f lavfi -i \"movie=filename=" + self.videoFile + ":loop=0, setpts=N/(FRAME_RATE*TB)\" -c:v rawvideo -pix_fmt yuv420 http://localhost:8080/" + self.streamName.replace('stream', 'feed') + ".ffm"
		else:
			commandString = "ffmpeg -loglevel quiet -r 30 -i " + self.videoFile + " -c:v rawvideo -pix_fmt yuv420 http://localhost:8080/" + self.streamName.replace('stream', 'feed') + ".ffm"

		if DEBUG:
			print(commandString)

		command = shlex.split(commandString)
		self.sprc = subprocess.Popen(command)

if DEBUG:
	if __name__ == "__main__":
		launcher = FFMpeg('~/video/test.mkv', 'stream-1')
