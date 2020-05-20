from __future__ import unicode_literals
from tkinter import *
import youtube_dl



root=Tk()
root.title("YouTube Downloader")
root.geometry('350x250')
lbl=Label(root, text="Paste Link Below and Click Download to begin!")
lbl.pack()
entry=Entry(root, width=10)
entry.pack()

def Clicked():
    url=entry.get()
    ydl_opts={}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
btn=Button(root, text="Download", command=Clicked)
btn.pack()
def getEntry():
    entry.get()





root.mainloop()



