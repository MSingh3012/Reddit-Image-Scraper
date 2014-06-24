__author__ = 'Rookev'

try:
    from urllib.request import urlopen, urlretrieve
except ImportError:
    from urllib import urlretrieve
    from urllib2 import urlopen

import os

from bs4 import BeautifulSoup

import config


def process_direct_link(url, folder):
    """
    Downloads an imgur image from a direct link ending on "jpg", "png" or "gif"

    :param url: "http://i.imgur.com/XYZ123.jpg"
    :param folder: Name of folder where image is saved
    """

    # Initializing file format
    fileformat = ""

    # If applicable, remove "?1" at the end of the url
    if "?" in url:
        url = url[:url.find("?")]

    # Set file format
    if url.endswith(".jpg"):
        fileformat = ".jpg"

    elif url.endswith(".png"):
        fileformat = ".png"

    elif url.endswith(".gif"):
        fileformat = ".gif"

    # File format was found
    if fileformat != "":

        # Generate file name: /[Folder]/[Index].[Format]
        filename = folder + str(config.currentfile) + fileformat

        # Download file
        print("Downloading image " + str(config.currentfile) + ":\t" + url)
        try:
            urlretrieve(url, filename)
        except:
            print("Error while opening:\t" + url)
            return

        # Increment counter to generate new file name for the next download
        config.currentfile += 1


def process_normal_link(url, folder):
    """
    Processes an imgur link by extracting the direct link and downloading it

    :param url: "http://imgur.com/XYZ123"
    :param folder: Name of folder where image is saved
    """

    # Read html file to url
    try:
        htmlpage = urlopen(url)
    except:
        print("Error while opening:\t" + url)
        return
    try:
        soup = BeautifulSoup(htmlpage)
    except:
        print("Error while parsing:\t" + url)
        return

    # Extract url from html file
    url = soup.select('.image a')

    if len(url) == 1:
        url = url[0]['href']

        # Download image
        url = format_url(url)
        process_direct_link(url, folder)


def process_album(url, albumtitle):
    """
    Processes an imgur album by extracting direct links and downloading them seperately.

    :param url: "http://imgur.com/a/XYZ123"
    :param albumtitle: Name of subfolder to be created for this album
    """

    # Read html file to url
    try:
        htmlpage = urlopen(url)
    except:
        print("Error while opening:\t" + url)
        return
    try:
        soup = BeautifulSoup(htmlpage)
    except:
        print("Error while parsing:\t" + url)
        return

    # Generate subfoldername for album
    subfolder = config.foldername + albumtitle + os.path.sep

    # Create subfolder
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    # Extract image links from html
    urls = soup.select('.album-view-image-link a')
    for url in urls:
        url = url['href']

        # Download image
        url = format_url(url)
        process_direct_link(url, subfolder)


def format_url(url):
    """
    Formats url strings by front adding "http:" if needed
    :param url: "//imgur.com/XYZ123"
    :return: "http://imgur.com/XYZ123"
    """
    if url.startswith("//"):
        url = "http:" + url
    return url