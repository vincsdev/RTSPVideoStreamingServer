from http.server import *
import json, os

class GetHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		length = int(self.headers.get('content-length'))

		#print(self.rfile.read(length))

		content = self.rfile.read(length).split(b"--gc0p4Jq0M2Yt08jU534c0p")
		#print(content)
		#print(len(content))
		if len(content) > 1:
			jsonData = content[1].decode('utf-8')
			jsonData = jsonData.split('json_data:')[1]
			#print(jsonData)
			data = json.loads(jsonData)
			#print(data)

			path = "./medias/images/"
			if not os.path.exists(path + data['id_source']):
				print("not exists")
				os.mkdir(path + data['id_source'])

			for i in range(2, len(content)-1):
				#print(i)
				imageField = content[i]
				#print(imageField)
				imageBytes = imageField.split(b"\r\n\r\n")[1]
				#print(imageBytes)
			
				fileName = path + data['id_source'] + '/' + data['timestamp'] + '-' + str(i-2) + ".jpeg"
				with open(fileName, 'wb') as fh:
					fh.write(imageBytes)
					fh.close()
				print(fileName + " saved")

			infoFile = path + data['id_source'] + ".info"
			if not os.path.exists(infoFile):
				with open(infoFile, 'w') as info:
					info.close()
				print("Info file created")
	
if __name__ == '__main__':
	server = HTTPServer(('0.0.0.0', 8000), GetHandler)
	print ('Starting server on port 8000, use <Ctrl-C> to stop')
	server.serve_forever()
