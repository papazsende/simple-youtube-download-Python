from pytube import YouTube
from tkinter import *

root = Tk()

root.resizable(0,0)
root.geometry('500x500')
root.title('İstek YT Downloader')


Label(root,text = 'Youtube Video İndirici', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Lütfen indirmek istediğiniz linki yapıştırın', font = 'Arial 15 bold').place(x= 60, y= 250)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y= 90)

def indirici():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOSYA İNDİRİLDİ', font = 'arial 15').place(x= 150 , y = 210)
Button(root,text = 'İNDİR', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = indirici).place(x=200 ,y = 150)
root.mainloop()