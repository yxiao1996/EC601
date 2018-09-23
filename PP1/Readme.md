# Personal Project 1

This Repository contains code for mini-project 1 during EC601 Product Design course. The library contains a Twitter API module to fetch images from specific twitter account; a Google Vision module to perform image analysis; some functions helping to transform the images into a video. 

### some explanation about the directories and files

app.py: the top-level application file, generating video.

movie.mp4: a sample video, image from @keinishikori

tweeimg: Twitter API module

vision: Google Vision API module and functions

### User Instructions

Before using this application, you have to apply access to Twitter API and Google Vision API.

You have to modify the code a little bit in order to use you API keys.

1. in ./app.py, change the buf_folder variable to where you want to use as image buffer, change keypath variable to where you Twitter API key located. 
2. in ./app.py, you can modify the twitter account in line 18 to fetch images from the account you like.
3. in ./app.py, you can modify how many images you want in the video by changing the argument in line 78.
