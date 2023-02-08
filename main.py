import tkinter
import customtkinter
from pytube import YouTube

def startDownload(): 
  try: 
    ytLink = link.get()
    ytObject = YouTube(ytLink)
    video = ytObject.streams.get_highest_resolution()

    title.configure(text = ytObject.title, text_color = 'white')
    finishLabel.configure(text = '')
    video.download()
  except:
    finishLabel.configure(text = 'Download Error :(', text_color = 'red')
  finishLabel.configure(text = 'Video Successfully Downloaded :)')


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text = 'Insert a YouTube link')
title.pack(padx = 10, pady = 10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text = '')
finishLabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text = 'Download', command = startDownload)
download.pack(padx = 20, pady = 20)

# Run app
app.mainloop()