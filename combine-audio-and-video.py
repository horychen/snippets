# # https://stackoverflow.com/questions/28219049/combining-an-audio-file-with-video-file-in-python
# import subprocess
# cmd = 'ffmpeg -y -i audio.m4s  -r 30 -i "【卡卡】♦囍♦一尺一恨_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili.mp4"  -filter:a aresample=async=1 -c:a flac -c:v copy "av.mp4"'
# subprocess.call(cmd, shell=True)                                     # "Muxing Done
# print('Muxing Done')
# 这个我没成功！




# https://www.reddit.com/r/learnpython/comments/ey41dp/merging_video_and_audio_using_ffmpegpython/
# pip install ffmpeg-python
import ffmpeg
video = ffmpeg.input('某个视频_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili.mp4')
audio = ffmpeg.input('audio.m4s')
out = ffmpeg.output(video, audio, 'av.mp4', vcodec='copy', acodec='aac', strict='experimental')
out.run()

