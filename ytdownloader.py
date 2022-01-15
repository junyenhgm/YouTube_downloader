from pytube import YouTube
from pytube import Playlist
from os.path import isfile
import sys
import re
import moviepy.editor as mp
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import unicodedata
import os

def Get_Filename(title):
    # Add Serial Number at the end of filename
    sequence = 1

    video_title = title

    # Replace full-width characters by half-width
    video_title = unicodedata.normalize('NFKC', video_title)
    
    # Remove special characters
    # video_title = re.sub(r"('.'|【|】|':'|/)", "", video_title)
    video_title = video_title.replace('.', '').replace('【', '').replace('】', '').replace(':', '').replace(r'/', '').replace(r'?', '').replace(r'!', '')

    Filename_ori = video_title + ".mp4"
    Filename = video_title + "(%s).mp4"

    if isfile(Filename_ori):
        while isfile(Filename % sequence):
            sequence = int(sequence or 0) + 1
        Filename = Filename % sequence
        Filename = Filename.replace('.mp4','')
    else:
        Filename = Filename_ori.replace('.mp4','')

    # Remove whitespace
    Filename = Filename.replace(' ', '')

    return Filename

class YouTube_download:
    def download_by_url(self, url):
        pytube_object = YouTube(url)
        stream = pytube_object.streams.filter(file_extension = "mp4").all()

        print(pytube_object.title)  # YouTube video tile
        for i in stream:
            print(i)

        tag = input("Input tag you want to download:")
        Filename = Get_Filename(pytube_object.title)
        print(Filename)
        pytube_object.streams.get_by_itag(tag).download(filename = Filename + '.mp4')

    def download_music(self, url):
        pytube_object = YouTube(url)
        # stream = pytube_object.streams.all()
        print(pytube_object.title)  # YouTube video tile

        Filename = Get_Filename(pytube_object.title)
        print(Filename)
        pytube_object.streams.filter(progressive=True).last().download(filename = Filename + '.mp4')

        # Convert to mp3
        # videoclip = VideoFileClip(Filename + '.mp4')
        # videoclip.audio.write_audiofile(Filename + '.mp3')
        # videoclip.close()

        audioclip = mp.AudioFileClip(Filename + '.mp4')
        audioclip.write_audiofile(Filename + '.mp3')
        audioclip.close()

    def download_playlist(self, url):
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
            
            Filename = Get_Filename(pytube_object)
            pytube_object.streams.filter(progressive=True).last().download(filename = Filename)


if __name__ == "__main__":

    Select_ = input("[0] Download video by tag \n[1] Download music \n[2] Download playlist\n")
    Select = int(Select_)
    if Select not in range(3):
        print("Invalid input!")
        exit()

    print("Give URL:")
    url = input()
    try:
        yt_dl = YouTube_download()
        if Select == 0:
            yt_dl.download_by_url(url)
        elif Select == 1:
            yt_dl.download_music(url)
        elif Select == 2:
            yt_dl.download_playlist(url)
        else:
            print("Invalid input!")
    except:
        print("Invalid input!")
