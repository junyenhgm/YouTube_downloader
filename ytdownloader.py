from pytube import YouTube
from os.path import isfile


### Example ###
# <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">
# <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">
# <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">
# <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">
# <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">
# <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">
# <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">
# <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">


# st = video.streams.filter(file_extension = "mp4").all()
# st = video.streams.filter(adaptive=True).all()
# st = video.streams.filter(only_audio=True).all()
# st = video.streams.filter(audio_codec="mp4a.40.2").all()
# video.streams.get_by_itag(140).download()



class Youtube_download:
    def download_by_url(url):
        pytube_object = YouTube(url)
        stream = pytube_object.streams.all()

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



print("Give URL:")
url = input()
try:
    # Youtube_download.download_by_url(url)
    Youtube_download.download_music(url)
except:
    print("Invalid input!")
