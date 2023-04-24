@echo off
setlocal EnableDelayedExpansion

set arg1=%1
set arg2=%2

ECHO %arg1%

set substr=.mp4

set filename=!arg1:%substr%=!

echo %filename%

ffmpeg -i %filename%.mp4 -filter:a "volume=2" %filename%.mp3

PAUSE