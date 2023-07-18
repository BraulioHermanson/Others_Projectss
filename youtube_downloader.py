from pytube import YouTube
from sys import argv

link = argv[1] # terminal
#link2 = input("add the link :") ## run on jupyternotebook
yt = YouTube(link)

print("Title: ",yt.title)

yd = yt.streams.get_highest_resolution()

yd.download(r'C:\Users\...\projetos')

