# Music-Collector-bot

This bot allows users to send a song title to Telegram and receive an audio file downloaded from YouTube.

## ⚙️ Technologies

- Python is the main programming language.
- aiogram v3 is an asynchronous framework for creating Telegram bots.
- yt_dlp is a library for downloading video/audio from YouTube.
- FFmpeg is for converting video to audio files.
- python-dotenv is for securely storing the token in an .env file.
- asyncio is for working with asynchronous code.
- Telegram Bot API is a platform for integrating with Telegram.

## Before started

1.Download Python 

 You need to install Python 3.13 on the official website https://www.python.org/downloads/

2.Download requirements

 The following two commands load aiogram and yt_dlp
 For aiogram:

 ``
 py -m pip install aiogram  
 ``
 For yt_dlp:

 ``
 py -m pip install yt_dlp       
 ``

## Getting Started

1. Clone the repository:
   
 ```
 git clone https://github.com/Kiryaoo/Music-Collector-bot.git
 cd Music-Collector-bot
 ```

2. Create a .env file

 .env the file must contain the bot token for further code execution and operation

3. Running the code 
   
 Use the next command to run code locally :
 ``
 py bot.py
 ``
