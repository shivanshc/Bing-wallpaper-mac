[![Build Status](https://travis-ci.org/shivanshc/Bing-wallpaper-mac.svg?branch=master)](https://travis-ci.org/shivanshc/Bing-wallpaper-mac)

A tool to set your MacOS/Linux wallpaper to be the same as Bing wallpaper every day.

Setup Instructions :

1. Clone the repository to your desired location.
   
   ```
  git clone https://github.com/shivanshc/Bing-wallpaper-mac.git PROJECT_DIR/
  ```
2. Setup the virtualenv. The project is in python 3 so set up a virtualenv in python 3 using the following command with a desired path
 
  ```
  python3 -m venv <DIR>
  ```
3. Activate the virtualenv using 
  
  ```
  venv/bin/activate
  ```
  and install the python dependencies using
  
  ```
  pip install -r PROJECT_DIR/requirements.txt
  ```
4. Edit the changeDesktop.sh file according tou your configs and add the following line to your crontab file(obtained by `crontab -e`) to automate the script to run every day
 
  ```
  15 0 * * * * PROJECT_DIR/changeDesktop.sh
  ```
5. You are all set. Be amazed as you get new beautiful desktop backgrounds every day. 
