#!/bin/bash

CURRENT_DIR="`pwd`"

echo $CURRENT_DIR

if [ -f /usr/bin/ffmpeg]; then
	echo "INFO:ffmpeg Found"
else
	echo "WARNING: mp3 support requires ffmpeg"
	echo "INFO: Install ffmpeg to air mp3 audio files"
fi

if [ -f $CURRENT_DIR/pifm]; then
	echo ""
else
	echo "INFO:Grabbing required dependencies"
	
	echo `wget http://omattos.com/pifm.tar.gz`
	echo `tar -xzf pifm.tar.gz`
	echo `rm pifm.tar.gz pifm.c PiFm.pyc sound.wav left_right.wav`
fi
