#!/usr/bin/python3
import sys, os, time
from files import *
from ffserver import *
from ffmpeg import *
from display import *
from utils import *

DEBUG = False

def main(argv):
	try:
		mediaFolder = argv[0]
		displayMode = argv[1]
		loopMode = argv[2]
	except:
		print("USAGE: python3 rtsp_server_tool.py <medias folder> <display mode File or Console> <loop mode>")
		sys.exit()

	if DEBUG:
		print("Arguments:")
		print(argv)

	files = Files(mediaFolder)

	if DEBUG:
		print("------------ IMAGES CONVERSION --------------")

	imageFolderList = files.getImageFolderList()

	if DEBUG:
		print("Image files: ")
		print(imageFolderList)
		print("Conversion report: ")

	files.convertImages(DEBUG)

	if DEBUG:
		print("---------------- VIDEO LIST -----------------")

	videoFilesList = files.getVideoFilesList()

	if DEBUG:
		print("Video files:")
		print(videoFilesList)

	if DEBUG:
		print("-------------- FFSERVER CONFIG --------------")
	config = FFServerConf(videoFilesList)
	streamNamesList = config.streamNames

	if DEBUG:
		print("Streaming names:")
		print(config.streamNames)

		print("-------------- FFSERVER LAUNCH --------------")

	ffserver = FFServer()

	if DEBUG:
		print("FFServer subprocess PID:")
		print(ffserver.sprc.pid)
	time.sleep(0.5)

	if DEBUG:
		print("--------------- FFMPEG LAUNCH ---------------")

	ffmpegPrcs = []
	for video, name in zip(videoFilesList, streamNamesList):
		ffmpegPrcs.append(FFMpeg(video, name, loopMode))

	if DEBUG:
		if loopMode == "loop":
			print("Loop mode: Enabled")
		else:
			print("Loop mode: Disabled")
		print("FFMpeg subprocesses PID:")
		for ffmpeg in ffmpegPrcs:
			print(ffmpeg.sprc.pid)

	#done = [ffmpeg.sprc.wait() for ffmpeg in ffmpegPrcs]

	print("---------- RTSP SERVER IS STARTED -----------")
	time.sleep(1)
	disp = Display(displayMode, videoFilesList, streamNamesList)

	while True:
		pass 

if __name__ == "__main__":
	try:
		main(sys.argv[1:])
	except KeyboardInterrupt:
		print("---------- RTSP SERVER IS STOPPED -----------")
		sys.exit()
