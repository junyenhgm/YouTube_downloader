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

print("Give URL:")
url = input()
try:
    video = YouTube(url)
    st = video.streams.all()

    for i in st:
        print(i)

    tag = input("Input tag you want to download:")

    # Add Serial Number at the end of filename
    sequence = ""
    Filename = "YouTube%s.mp4"

    while isfile(Filename % sequence):
        sequence = int(sequence or 0) + 1
    Filename = Filename % sequence

    Filename = Filename.replace('.mp4','')

    video.streams.get_by_itag(tag).download(filename = Filename)

except:
    print("Invalid input!")



# https://www.youtube.com/watch?v=UFQEttrn6CQ # 米津玄師 感電MV
# https://www.youtube.com/watch?v=MpYy6wwqxoo # LiSA Gurege first take
