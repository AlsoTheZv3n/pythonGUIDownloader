import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        # Check if the link is a valid URL
        if not ytLink.startswith("http"):
            raise ValueError("Invalid URL")

        ytObj = YouTube(ytLink)
        video = ytObj.streams.get_highest_resolution()
        video.download()
        finishLabel.config(text="Download Successful")

    except Exception as e:
        print("Error:", e)
        finishLabel.config(text="Error: Invalid URL")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("black")

# Our app frame
app = customtkinter.CTk()
app.geometry("600x200")
app.title("Youtube Downloader")

# UI
title = customtkinter.CTkLabel(app, text="Enter YouTube URL:")
title.pack(padx=10, pady=10)

# link input
url_var = customtkinter.StringVar()
link = customtkinter.CTkEntry(app, width=50, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Download Done Label
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Run app
app.mainloop()
