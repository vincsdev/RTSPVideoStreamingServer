import socket, os, shutil
from moviepy.editor import *

def getIP():
	""" return the IP address of the server. """
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	try:
		s.connect(("gmail.com",80))
		ip = s.getsockname()[0] 
		return ip
	except Exception:
		return "127.0.0.1"

def checkProcess(pid):
	try:
		os.kill(pid, 0)
	except OSError:
		return False

	else:
		return True

def convertToVideo(imagesFolder, videoFolder, infos, debug):
	folderName = os.path.basename(imagesFolder)
	try:
		animation = ImageSequenceClip(imagesFolder, fps=infos['fps'])
	except:
		animation = ImageSequenceClip(imagesFolder, fps=infos['fps_default'])
	try:
		animation.write_videofile(videoFolder+'/' + folderName + '.' + infos['format'], fps=30, verbose=debug)
	except:
		animation.write_videofile(videoFolder+'/' + folderName + '.' + infos['format_default'], fps=30)
