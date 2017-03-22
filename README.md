RTSP Video Streaming Server
===========================

It provides the streaming of several video files.
Moreover, it can take in input a folder with images to create a video file which will be streamed.

It is available on Python3. I don't know if it works with Python2 because I don't want use it.


Requirements
============
* Python3
* pip3
* moviepy
* FFMpeg


Installation
============
Firstly you must install dependencies.
Then, you just need to clone or download this repository.


Usage
=====
For the moment, you can use it as a simple script:
```
  $ python3 RTSPVideoStreamingServer <medias folder> <display mode of streaming url> <loop mode>
```
medias folder must contain:
	- images/
	- videos/

display mode:
	- console: Display on the console link between video files and streaming urls.
	- file: Same than console but it creates the streams.txt file which contains infos.

loop mode:
	- loop: It allow streams to be played on a loop.
	- noloop: One times video is ended, the server must be restarted if you want return to the beginning of streams.

Use Ctrl + C to quit the program.


There is a suplementary tool called gethttpimages. It provides an http server to retrieve images from http multipart post request.
Then it saves images in a tree folder specified: ./medias/images/

To use it, just run:
```
  $ python3 gethttpimages.py
```
Then, add its IP adress and port on RemoteServer part of AI application(s). It will create a folder for each source id and store their images on each. It creates also default infos file for each folder for RTSPVideoStreamingServer. I advise you to modify their parameters.

Use Ctrl + C to quit the program.

You can launch it before RTSPVideoStreamingServer to get images and then run RTSPVideoStreamingServer to stream retrieved images.


Tests
=====
After performances tests, I defined for a 8 cores processor it's difficult to stream more than 16 streams with 320x240 resolution. If you tried more than 16, you will see delays on video stream.
