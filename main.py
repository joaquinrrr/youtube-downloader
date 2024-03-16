import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytobject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytobject.streams.get_highest_resolution()
        

        title.configure(text=ytobject.title, text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Downloaded!")
    except:
        finishlabel.configure(text="Download Error", text_color="Red")

def on_progress(stream, chunk, bytes_reamaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_reamaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_compeletion))
    percentage.configure(text = per + '%')
    percentage.update()

    #update progress bar
    progressbar.set(float(percentage_of_compeletion)/100)


#systyem config
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("Yt downloader")

title = customtkinter.CTkLabel(app, text="Insert yt link")
title.pack(padx = 10, pady= 10)

#inpuuut
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx = 10, pady= 10)
link.pack()

#finishe downloading
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack()

#progress percertange
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)

#download butt
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady= 10)
download.pack()

app.mainloop()