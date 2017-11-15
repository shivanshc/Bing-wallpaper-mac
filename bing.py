from bs4 import BeautifulSoup
import requests
import wget
import sqlite3
import subprocess
import os

IMAGE_PATH = 'Library/Application Support/Dock/Bing/background.jpg'
IMAGE_FOLDER = 'Library/Application Support/Dock/Bing'
USER_DIR = os.getenv("HOME")


def getImageURL():
    resp = None
    while resp is None:
        try:
            resp = requests.get("http://www.bing.com")
        except:
            resp = None
    soup = BeautifulSoup(resp.text, "html.parser")
    instance = soup.find_all("script", {"type": "text/javascript"})
    for i in instance:
        jsContent = i.text
        if "g_img={url:" in jsContent:
            beginIndex = jsContent.find('g_img={url: "') + 13
            endIndex = jsContent.find('jpg', beginIndex) + 3
            imgURL = jsContent[beginIndex:endIndex]
            imgURL = "http://www.bing.com/" + imgURL
    return imgURL


def downloadImage(downloadDir):
    imgURL = getImageURL()
    fileName = wget.download(imgURL, out=downloadDir, bar=False)
    return fileName


def updateBackground(imgPath):
    imagePath = os.path.join(USER_DIR, IMAGE_PATH)
    subprocess.run(['ln', '-s', '-F', imgPath, imagePath])


def getDownloadPath():
    folderPath = os.path.join(USER_DIR, IMAGE_FOLDER)
    if not os.path.isdir(folderPath):
        os.mkdir(folderPath)
    return folderPath


def setBackground():
    downloadDir = getDownloadPath()
    imagePath = downloadImage(downloadDir)
    updateBackground(imagePath)
    subprocess.run(['killall', 'Dock'])


if __name__ == '__main__':
    setBackground()
