import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI Elements
title = customtkinter.CTkLabel(app, text='Insert a YouTube link')
title.pack(padx=10, pady=10)

# Link input
link = customtkinter.CTkEntry(app, width=350, height=40)
link.pack()

# Run app
app.mainloop()