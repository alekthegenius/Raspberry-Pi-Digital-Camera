# Raspberry-Pi-Digital-Camera
### Software to turn a Raspberry Pi into a Digital Camera

*Used with Raspberry Pi Zero W, Hyperpixel 2.1" Round Display, and Raspberry Pi HQ Camera Module.*

In this repository, there are three files, "gui.py", "startCam.sh", and "Cam.conf". The "gui.py" is a Python App for taking pictures and videos, "startCam.sh" is a program to start the "gui.py", and lastly, "Cam.conf" is a script that autostarts the "startCam.sh" program on boot, which in turn starts "gui.py".

Below is a list of all the modules that you will need to install:

- hyperpixel2r (Already installed)
- picamera (Install with PIP)
- tkinter * (Install with PIP)
- tkinter ttk (Already Installed with Tkinter)
- tkinter.font (Already Installed with Tkinter)
- subprocess (Install with PIP)
- datetime (Install with PIP)
- tkinter (Already Installed with Tkinter)
- fnmatch (Install with PIP)
- shutil (Install with PIP)
- time (Installed by default)
- glob (Install with PIP)
- sys (Installed by default)
- os (Installed by default)

First, download the file "gui.py" below, into a folder titled "App" in the documents folder of the Pi:

`~/home/pi/Documents/App/`

Once you have saved the python file to your Pi, add the file labeled "startCam.sh" below to the pi directory on the Raspberry Pi:

`~/home/pi/`

Lastly, add the "Cam.conf" file to the init directory located in etc:

`~/etc/init/`

Reboot your Pi, and you should now have a working camera!
