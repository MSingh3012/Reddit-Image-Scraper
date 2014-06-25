import os

# Program identification for Reddit
useragent = "Reddit Image Scraper by /u/Ronny93"

# Target user name
username = ""

# Number of posts to scrape
limit = 0

# Path to user directory
userhome = os.path.expanduser('~')

# Path to user desktop
foldername = userhome + os.path.sep + "Desktop" + os.path.sep

# Counter for downloaded images
currentfile = 1
