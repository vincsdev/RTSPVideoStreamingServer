import subprocess, shlex, os
from utils import *

DEBUG = False

FFSERVER_BIN = "ffserver" # on Linux

class FFServerConf:
	def __init__(self, filesList):
		self.filesList = filesList
		self.streamNames = []

		self.configInit()
		self.configVideoFiles()


	def configInit(self):
		""" Initialisation of the ffserver.conf file """

		if not os.path.exists("conf"):
			os.mkdir("conf")

		with open('conf/ffserver.conf', 'w') as c:
			c.write("HTTPPort 8080 \n")
			c.write("RTSPPort 5454 \n")
			c.write("HTTPBindAddress 0.0.0.0 \n")
			c.write("RTSPBindAddress 0.0.0.0 \n")
			c.write("MaxHTTPConnections 2000 \n")
			c.write("MaxClients 1000 \n")
			c.write("MaxBandwidth 20480 \n")
			c.write("CustomLog - \n")
			c.write("\n")

			c.write("<Stream status.html> \n")
			c.write("	Format status \n")
			c.write("</Stream> \n")
			c.write("\n\n")

	def configVideoFiles(self):
		""" Add in the ffserver.conf file feeds and associed streams"""

		with open('conf/ffserver.conf', 'a') as c:
	
			if not os.path.exists("conf/feeds"):
				os.mkdir("conf/feeds")
		
			IP_ADDRESS = getIP()
			rangeIP    = IP_ADDRESS.split(".")
			beginIP    = rangeIP[0]+"."+rangeIP[1]+"."+rangeIP[2]
			firstIP    = beginIP+".0"
			endIP      = beginIP+".255"

			""" Video size """
			W = 320
			H = 240

			for idx, f in enumerate(self.filesList):
				c.write("<Feed feed-" + str(idx) + ".ffm> \n")
				c.write("	File conf/feeds/feed-" + str(idx) + ".ffm \n")
				c.write("	FileMaxSize 500M \n")
				c.write("	ACL allow 127.0.0.1 \n")
				c.write("	ACL allow " + firstIP + " " + endIP + "\n")
				c.write("</Feed> \n")
				c.write("\n")

				c.write("<Stream stream-" + str(idx) + "> \n")
				c.write("	Feed feed-" + str(idx) + ".ffm \n")
				c.write("	Format rtp \n")
				c.write("	File " + os.path.basename(f) + " \n")
				c.write("	VideoSize " + str(W) + "x" + str(H) + " \n")
				c.write("	VideoQMin 1 \n")
				c.write("	VideoQMax 20 \n")
				c.write("	VideoFrameRate 30 \n")				
				c.write("	VideoBitRate 500 \n")
				c.write("	AVOptionVideo flags +global_header \n")
				c.write("	VideoCodec libx264 \n")
				c.write("	NoAudio \n")
				c.write("	NoDefaults \n")

				c.write("</Stream> \n")
				c.write("\n\n")

				self.streamNames.append("stream-" + str(idx))

class FFServer:
	""" Class taking care to launch the ffserver """

	def __init__(self):
		self.sprc = None
		self.launchServer()

	def launchServer(self):
		""" Launch the server thanks to the configuration file """
		command = shlex.split(FFSERVER_BIN + " -loglevel quiet -f conf/ffserver.conf")
		self.sprc = subprocess.Popen(command)


if DEBUG:
	if __name__ == "__main__":
		listFiles = ['/home/vini/Documents/Dev/AITech/rtsp_server/rtsp_server/videos/indoor.mkv', '/home/vini/Documents/Dev/AITech/rtsp_server/rtsp_server/videos/outdoor.mkv']
		test = FFServerConf(listFiles)
		launcher = FFServer()
