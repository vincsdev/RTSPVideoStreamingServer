RTSP Video Streaming Server
===========================

It provides the streaming of several video files.
Moreover, it can take in input a folder with images to create a video file which will be streamed.

It is available on Python3. I don't know if it works with Python2 because I don't want use it.

Requirements
============
* Python3
* moviepy
* FFMpeg


Installation
============
You just need to clone or download this repository.


Usage
=====
For the moment, you can use it like a simple script:
```
  $ python3 RTSPVideoStreamingServer <medias folder> <display mode of streaming url: console or file> <loop mode>
```

There is a suplementary tool called gethttpimages. It provides an http server to retrieve images from http multipart post request.
Then it saves images in a tree folder specified.
To use it, just run:
```
  $ python3 gethttpimages.py
```
