# Icodestuff Reddit To Instagram Bot

This robot allows users to automate posting from subreddits to their Instagram Page.
I currently use it to run my instagram page <a href="https://www.instagram.com/icodestuff.io/"> Icodestuff.io </a>


### Getting Started
The code in app.py requires the user has the following files:

##### Setup.py
Run the following to generate the required configuration files:
`python setup.py`

##### Caption.txt
This is the Instagram caption posted on each programmatic post. I generally just use a generic message like: "follow @icodestuff.io for more content like this"

##### Hashtags.txt
This file provides hashtags on each Instagram post. You can leave it empty, however using it will drastically increase your engagement Checkout caption.txt.example

##### Credentials.json
This file required as it allows the user to login to both Reddit and Instagram programmatically. The file also has a user-agent field with the default _icodestuff.io/bot_ which you can change anything to you want. The file also contains the subreddit url where your content derives from. To generate a subreddit url just follow the example in the credentials.json.example

### How To Use
After editing all the necessary configuration files run `python app.py` which will prompt an image and ask if you want to post the image to instagram. Type _yes_ or _no_, after you answer the code will prompt another image and ask if you want to post. Once you have posted the necessary amount of photos just stop the code. 

### Known Issues
Here are list of issues I know need to be resolved: 
- CMD unexpectedly quitting
- Failure to change aspect ratio of images
- No option to post videos 

These are all issues I plan on tackling in the next version. 

### Donate 
If you enjoy using this tool please consider donating. :) 
- Buy Me A Coffee: https://www.buymeacoffee.com/oQqE7e5gj