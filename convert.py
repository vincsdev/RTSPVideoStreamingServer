from moviepy.editor import *
import os, sys

WORKDIR = 'Images'

import datetime
import time
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')

#Creating animation
def makeAnimation(folder):
    images_list=folder
    animation = ImageSequenceClip(images_list, fps=0.8)
    return animation

#-----------------------------------------------------------------
#From pictures jpg to gif
#-----------------------------------------------------------------
def makeGif(folder):
    print "Creating GIF ..."
    makeAnimation(folder).write_gif(folder+st+".gif", fps=0.8) # export as GIF (slow)

#-----------------------------------------------------------------
#From pictures jpg to video
#-----------------------------------------------------------------
def makeVideo(folder):
    print "Creating Video ..."
    makeAnimation(folder).write_videofile(folder+st+".mp4", fps=24) # export as video

#-----------------------------------------------------------------
# For the export, many options/formats/optimizations are supported
#animation.write_videofile("my_animation.mp4", fps=24) # export as video
#animation.write_gif("my_animation.gif", fps=24) # export as GIF (slow)
# need (sudo) pip install moviepy

#-----------------------------------------------------------------
makeGif(WORKDIR)
makeVideo(WORKDIR)
