from pytube import YouTube
from pytube import Playlist
from os.path import isfile
import sys
import re

# st = video.streams.filter(file_extension = "mp4").all()
# st = video.streams.filter(adaptive=True).all()
# st = video.streams.filter(only_audio=True).all()
# st = video.streams.filter(audio_codec="mp4a.40.2").all()
# st = pytube_object.streams.filter(progressive=True).all()
# video.streams.get_by_itag(140).download()

class YouTube_download:
    def download_by_url(url):
        pytube_object = YouTube(url)
        stream = pytube_object.streams.filter(file_extension = "mp4").all()

        print(pytube_object.title)  # YouTube video tile
        for i in stream:
            print(i)

        tag = input("Input tag you want to download:")

        # Add Serial Number at the end of filename
        sequence = 1
        # Filename = "YouTube%s.mp4"
        Filename_ori = pytube_object.title + ".mp4"
        Filename = pytube_object.title + "(%s).mp4"

        if isfile(Filename_ori):
            while isfile(Filename % sequence):
                sequence = int(sequence or 0) + 1
            Filename = Filename % sequence
            Filename = Filename.replace('.mp4','')
            pytube_object.streams.get_by_itag(tag).download(filename = Filename)
        else:
            Filename_ori = Filename_ori.replace('.mp4','')
            pytube_object.streams.get_by_itag(tag).download(filename = Filename_ori)

    def download_music(url):
        pytube_object = YouTube(url)
        # stream = pytube_object.streams.all()
        print(pytube_object.title)  # YouTube video tile

        # Add Serial Number at the end of filename
        sequence = 1
        # Filename = "YouTube%s.mp4"
        Filename_ori = pytube_object.title + ".mp4"
        Filename = pytube_object.title + "(%s).mp4"

        if isfile(Filename_ori):    # Check if existed
            while isfile(Filename % sequence):
                sequence = int(sequence or 0) + 1
            Filename = Filename % sequence
            Filename = Filename.replace('.mp4','')
            pytube_object.streams.get_by_itag(140).download(filename = Filename)
        else:
            Filename_ori = Filename_ori.replace('.mp4','')
            pytube_object.streams.get_by_itag(140).download(filename = Filename_ori)

    def download_playlist(url):
        playlist = Playlist(url)
        # this fixes the empty playlist.videos list
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        
        print(len(playlist.video_urls))
        
        for url in playlist.video_urls:
            pytube_object = YouTube(url)
            stream = pytube_object.streams.filter(progressive=True).all()
            print(pytube_object.title)  # YouTube video tile
            # for i in stream:
            #     print(i)
            
            # Add Serial Number at the end of filename
            sequence = 1
            # Filename = "YouTube%s.mp4"
            Filename_ori = pytube_object.title + ".mp4"
            Filename = pytube_object.title + "(%s).mp4"

            if isfile(Filename_ori):
                while isfile(Filename % sequence):
                    sequence = int(sequence or 0) + 1
                Filename = Filename % sequence
                Filename = Filename.replace('.mp4','')
                pytube_object.streams.filter(progressive=True).last().download(filename = Filename)
            else:
                Filename_ori = Filename_ori.replace('.mp4','')
                pytube_object.streams.filter(progressive=True).last().download(filename = Filename_ori)


Select = input("[0] Download video by tag \n[1] Download music \n[2] Download playlist\n")
if int(Select) not in range(3):
    print("Invalid input!")
    exit()

print("Give URL:")
url = input()
try:
    if int(Select) == 0:
        YouTube_download.download_by_url(url)
    elif int(Select) == 1:
        YouTube_download.download_music(url)
    elif int(Select) == 2:
        YouTube_download.download_playlist(url)
    else:
        print("Invalid input!")
except:
    print("Invalid input!")
