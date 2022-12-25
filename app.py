import streamlit as st
from pytube import YouTube
import time

st.title("Welcome to Viznu YouTube downloader!")

# Get the YouTube URL from the user
link = st.text_input("Paste link here")

# Check if the link is empty or not
if not link:
    st.error("Please enter a valid YouTube URL")
else:
    # Display a radio button to select the file format
    mode = st.radio('Audio or the video?', ('Audio', 'Video'))

    # Display the video details
    try:
        video = YouTube(link)
        st.image(video.thumbnail_url, width=400)
        st.write("Video Title: ", video.title)
        st.write("Duration:", time.strftime("%H:%M:%S",time.gmtime(video.length)), "seconds") # Displays the duration in default format
        if mode == 'Video':
            yt = video.streams.get_highest_resolution()
        elif mode == "Audio":
            yt = video.streams.filter(only_audio=True).first()
        st.write("File size:", "{:.1f}".format(yt.filesize / 1024**2), "MB")  # display file size in MB
    except:
        st.error("Invalid YouTube URL or connection error")

    def video_download():
        try:
            yt = video.streams.get_highest_resolution()
            yt.download()  # download to the current working directory
            st.success("Video downloaded successfully!")
        except:
            st.error('Connection error!')

    def audio_download():
        try:
            yt = video.streams.filter(only_audio=True).first()
            yt.download()  # download to the current working directory
            st.success("Audio downloaded successfully!")
        except:
            st.error('Connection error!')

    # download button
    if st.button("Download"):
        if mode == 'Video':
            video_download()
        elif mode == "Audio":
            audio_download()