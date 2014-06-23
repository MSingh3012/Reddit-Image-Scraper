__author__ = 'Rookev'
import os

# Program identification for Reddit
user_agent = "Reddit Image Scraper by /u/Ronny93";

# Target user name
username = "";

# Number of posts to scrape
limit = 0;

# Path to user directory
userhome = os.path.expanduser('~')

# Path to user desktop
folderName = userhome + os.path.sep + "Desktop" + os.path.sep;

# Counter for downloaded images
currentFile = 1;