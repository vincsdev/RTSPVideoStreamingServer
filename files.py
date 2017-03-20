import os, sys
from utils import convertToVideo

DEBUG = False

class Files:
	def __init__(self, path_folder):
		self.pathFolder = os.path.abspath(path_folder)
		self.imageFolderList = []
		self.videosFolder = self.pathFolder+"/videos"

	def getVideoFilesList(self):
		filesList = []
		if not os.path.exists(self.videosFolder):
			print("Path doesn't exist...")
			sys.exit()

		for root, dirs, files in os.walk(self.videosFolder, topdown=True):
			dirs.clear()
			for f in files:
				if not f.startswith('.'):
					""" Add check extension file """
					filesList.append(root+'/'+f)

		if DEBUG:
			print(filesList)

		return filesList

	def getImageFolderList(self):
		dirsList = []
		imagesFolder = self.pathFolder+"/images"
		if not os.path.exists(imagesFolder):
			print("Path doesn't exist...")
			return False

		for root, dirs, files in os.walk(imagesFolder, topdown=True):
			for d in dirs:
				dirsList.append(root+'/'+d)

		self.imageFolderList = dirsList

		if DEBUG:
			print(dirsList)

		return dirsList

	def convertImages(self, debug):		
		for d in self.imageFolderList:
			infos = self.getImagesInfos(d)
			if infos is not None:
				convertToVideo(d, self.videosFolder, infos, debug)
			else:
				print("ERROR: Information file is missing for:\n" + d)

	def getImagesInfos(self, imagesFolder):
		infos = { 'fps_default': 25, 'format_default': 'mp4'}
		try:
			with open(imagesFolder+".info") as f:
				for line in f:
					if 'fps' in line:
						infos['fps'] = int(line.split(':')[1])
					if 'format' in line:
						infos['format'] = line.split(':')[1]
						infos['format'] = infos['format'].replace('\n','')
				f.close()
			return infos
		except:
			return None		

if DEBUG:
	if __name__ == "__main__":
		test = Files('/home/vini/Documents')
