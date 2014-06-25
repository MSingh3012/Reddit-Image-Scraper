# -*- coding: utf-8 -*-

import warnings
import os
import sys

import praw

from .config import *
from .downloader import process_album, process_direct_link, process_normal_link

if __name__ == '__main__':
    warnings.filterwarnings('ignore')

    if len(sys.argv) != 3:
        print("Usage: python imagescraper.py Username NumberOfPostsToScrape")
        sys.exit(-1)

    # Read command line arguments
    usernameInput = sys.argv[1]
    limitInput = sys.argv[2]

    try:
        username = str(usernameInput)
        limit = int(limitInput)
    except:
        print("Usage: python imagescraper.py Username NumberOfPostsToScrape")
        sys.exit(-1)

    # foldername on disk: "/[Path to Desktop]/[Target user name]/"
    foldername += username + os.path.sep

    # Arguments summary
    print()
    print("Username:\t" + username)
    print("# of posts:\t" + str(limit))
    print()

    # Reddit access
    r = praw.Reddit(user_agent=useragent)

    # Access reddit user
    try:
        user = r.get_redditor(username)

    # User doesn't exist -> exit with exit code "-2"
    except:
        print("User '" + username + "' does not exist!")
        sys.exit(-2)

    # Fetch posts
    posts = user.get_submitted(limit=limit)

    # Create folder "/[Path to Desktop]/[Target user name]/"
    if not (os.path.exists(foldername)):
        os.makedirs(foldername)

    # Process each post
    for post in posts:

        # Read url
        url = post.url

        # Album link: "http://imgur.com/a/XYZ123"
        if "imgur.com/a/" in url:
            process_album(url, post.name)

        # Direct link: "http://i.imgur.com/XYZ123.jpg"
        elif url.endswith(".jpg") or url.endswith(".png") or url.endswith(".gif"):
            process_direct_link(url, foldername)

        # Normal link: "http://imgur.com/XYZ123"
        elif "imgur.com/" in url:
            process_normal_link(url, foldername)

    # Result summary
    print()
    print("Scraped posts:\t" + str(limit))
    print("Downloaded images:\t" + str(currentfile - 1))
    print()
