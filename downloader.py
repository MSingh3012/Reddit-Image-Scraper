__author__ = 'Rookev'

import urllib.request
import os

from bs4 import BeautifulSoup

import config


def processDirectLink(url, folder):
    '''
    Downloads an imgur image from a direct link ending on "jpg", "png" or "gif"

    :param url: "http://i.imgur.com/XYZ123.jpg"
    :param folder: Name of folder where image is saved
    '''

    # Initializing file format
    fileFormat = "";

    # If applicable, remove "?1" at the end of the url
    if ("?" in url):
        url = url[:url.find("?")]

    # Set file format
    if (url.endswith(".jpg")):
        fileFormat = ".jpg";

    elif (url.endswith(".png")):
        fileFormat = ".png";

    elif (url.endswith(".gif")):
        fileFormat = ".gif";

    # File format was found
    if (fileFormat != ""):

        # Generate file name: /[Folder]/[Index].[Format]
        fileName = folder + str(config.currentFile) + fileFormat;

        # Download file
        print("Downloading image " + str(config.currentFile) + ":\t" + url);
        try:
            urllib.request.urlretrieve(url, fileName);
        except:
            print("Error while opening:\t" + url);
            return;

        # Increment counter to generate new file name for the next download
        config.currentFile += 1;


def processNormalLink(url, folder):
    '''
    Processes an imgur link by extracting the direct link and downloading it

    :param url: "http://imgur.com/XYZ123"
    :param folder: Name of folder where image is saved
    '''

    # Read html file to url
    try:
        htmlPage = urllib.request.urlopen(url);
    except:
        print("Error while opening:\t" + url);
        return;
    try:
        soup = BeautifulSoup(htmlPage);
    except:
        print("Error while parsing:\t" + url);
        return;

    # Extract url from html file
    url = soup.select('.image a');

    if (len(url) == 1):
        url = url[0]['href'];

        # Download image
        url = formatUrl(url);
        processDirectLink(url, folder);

    # lastSlash = url.rfind("/");

def processAlbum(url, albumTitle):
    '''
    Processes an imgur album by extracting direct links and downloading them seperately.

    :param url: "http://imgur.com/a/XYZ123"
    :param albumTitle: Name of subfolder to be created for this album
    '''

    # Read html file to url
    try:
        htmlPage = urllib.request.urlopen(url);
    except:
        print("Error while opening:\t" + url);
        return;
    try:
        soup = BeautifulSoup(htmlPage);
    except:
        print("Error while parsing:\t" + url);
        return;

    # Generate subfoldername for album
    subfolder = config.folderName + albumTitle + os.path.sep;

    # Create subfolder
    if not (os.path.exists(subfolder)):
        os.makedirs(subfolder);

    # Extract image links from html
    urls = soup.select('.album-view-image-link a');
    for url in urls:
        url = url['href'];

        # Download image
        url = formatUrl(url);
        processDirectLink(url, subfolder);


def formatUrl(url):
    '''
    Formats url strings by front adding "http:" if needed
    :param url: "//imgur.com/XYZ123"
    :return: "http://imgur.com/XYZ123"
    '''
    if (url.startswith("//")):
        url = "http:" + url;
    return url;