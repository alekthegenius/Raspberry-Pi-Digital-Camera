## Introduction

I have always had a passion for photography, and so in this instructable, I will describe how I created my own Raspberry Pi Digital Camera.

I began creating this digital camera with 3 objectives:

* To have a small lightweight camera
* To make it unique
* To have full control over the camera settings, ISO, Shutter Speed, etc.
To fulfill my objectives, I first designed the camera case to be round, which reduces the size and weight of the camera, while also giving it a sleek, modern look. Using Python 3 and Tkinter, I also programmed an app to allow for full manual control over the camera settings and features.

In this instructable, I will outline the materials used, the design process, the steps to follow, as well as some improvements for the future.

**Let's dive in!**

## Supplies

### Tools

* 3D Printer
* PETG Filament
* Screwdriver

### Materials

* Raspberry Pi Zero W or Zero 2 W
* CS-Mount Lens (I used an adjustable wide-angle lens from Pimoroni)
* Pimoroni Hyperpixel 2.1" Round Touch Display
* Raspberry Pi HQ Camera
* 15cm Raspberry Pi Zero to Camera Ribbon Cable
* Short Pi Standoffs Kit (Available from Pimoroni)
* M3x6mm Screws x12
* M3 Female to Female Standoff 10mm x4
* M3 Female to Male Standoff 5mm x4
* Right Angle Micro USB Male to Female Cable
* Micro USB to USB Cable
* Portable Battey Pack
* (Optional) Tripod to Hold Camera

## Designing the Camera Case

For the design process, I used Fusion 360 to sketch out a case for the Raspberry Pi and the camera to mount to. The purpose of the case is to provide protection for the touch screen and camera.

## Setting Up the SD Card

Before we assemble the camera, let's set up the SD Card for the Raspberry Pi.

We first need to flash Rasbian Buster to an SD card. To do that you either need to download the image yourself, then use a program like Balena Etcher to flash the image, or let the Raspberry Pi Imager app do everything for you. For the purposes of this tutorial, we will be focusing on the Raspberry Pi Imager. Once you have the Raspberry Pi Imager installed and running, select Choose OS » Raspberry Pi OS (other) » Raspberry Pi OS (Legacy). Once you have selected the image to flash, select Choose Storage then select your SD card. Now you can access the advanced settings menu by clicking the gear icon. From there, configure SSH WIFI by selecting "Enable SSH", and "Configure Wireless Lan". Click Save, and It will save your settings to the image. Now, click write and wait for it to finish flashing the image to your SD card. Now you can safely remove the SD card from your computer, and insert it into the Raspberry Pi.

## Assembling the Camera

Now that we have all the parts and tools, it's time to assemble the camera. You can use the images above as guides.

1. Using the four standoffs found in the Short Pi Standoff kit, screw each standoff into the back of the Hyperpixel display.
2. Once all four standoffs are screwed into the back of the display, gently push the Raspberry Pi headers onto the headers of the Hypepixel display, careful not to break the glass.
3. Then using the M3 Female to Male Standoff 5mm, screw the Raspberry Pi securely to the back.
4. Set the display aside to work on the camera module. Using four M3x6mm screws, screw the four M3 Female to Female Standoff 10mm onto the camera module.
5. Using four more M3x6mm screws, I screwed the M3 Female to Female Standoff onto the Camera Case.
6. Now that the camera module is connected, we will finish setting up the Raspberry Pi. Feed the small end of the 15cm Raspberry Pi Zero to Camera Ribbon Cable through the square hole on the base plate (Refer to image 20 for details,) then connect the ribbon cable to the Raspberry Pi's camera port.
7. Before you screw the display into the case, feed the right angle micro USB male-to-female cable through the hole on the side of the case. Plug the right-angle male side of the cable into the Raspberry Pi's power connector.
8. Now, gently slide the display into the case until the display sits flush with the edges of the side of the case. Using the screws found in the Short Pi Standoff kit, snugly screw the Raspberry Pi into the case. Last but not least, plug the other end of the camera ribbon cable into the camera's port.

## Setting up the Software 

Before we can take pictures, we need to install the software for the HyperPixel Screen.

For full details visit: [https://github.com/pimoroni/hyperpixel2r](https://github.com/pimoroni/hyperpixel2r)

When you first power on the Raspberry Pi, you may notice that the Hyperpixel display is blank. This is because the Hyperpixel's Driver is not installed, and so, to get it working you'll need to install the official driver provided by Pimoroni.

After you have SSH into the Raspberry Pi, enter the commands below to install the driver:
```
git clone https://github.com/pimoroni/hyperpixel2r
cd hyperpixel2r
sudo ./install.sh
After you have finished installing the library, reboot the Pi with:
```
```
sudo reboot
```
Once it has finished rebooting, you should see the screen display the Raspberry Pi's desktop.

Now that we've got the screen up and running, we will install the Hyperpixel's Python library.

Before installing the library, we need to edit the Raspberry Pi's config file, so that we can control the display with Python.

First, run:
```
sudo nano /boot/config.txt
```
Which will pull up the config file,

then add
```
:disable-touch
```
to
```
dtoverlay=hyperpixel2r
So it will look like this:
```
```
dtoverlay=hyperpixel2r:disable-touch
```
This disables the Linux touch driver so that we can communicate through Python to the touch IC.

_Note: Adding ":disable-touch" to the config file disables touch input._

To install the Python Library, enter the following commands on the Raspberry Pi:
```
git clone https://github.com/pimoroni/hyperpixel2r-python
cd hyperpixel2r-python
sudo ./install.sh
```
Make sure to copy the examples from the library to ~/home/pi/hyperpixel2r-python/examples/

Once done installing, reboot again and now you should have a fully functional display.

## Installing the App

Now it's time to install the Python application I created for taking photos!

Below is a list of all the modules that you will need to install:

* ```hyperpixel2r (Already installed)```
* ```picamera (Install with PIP)```
* ```tkinter * (Install with PIP)```
* ```tkinter ttk (Already Installed with Tkinter)```
* ```tkinter.font (Already Installed with Tkinter)```
* ```subprocess (Install with PIP)```
* ```datetime (Install with PIP)```
* ```tkinter (Already Installed with Tkinter)```
* ```fnmatch (Install with PIP)```
* ```shutil (Install with PIP)```
* ```time (Installed by default)```
* ```glob (Install with PIP)```
* ```sys (Installed by default)```
* ```os (Installed by default)```

My Github repository contains all of the files you need.

First, download the file "gui.py" below, into a folder titled "App" in the documents folder of the Pi:

```
~/home/pi/Documents/App/
```

Once you have saved the python file to your Pi, add the file labeled "startCam.sh" below to the pi directory on the Raspberry Pi:

```
~/home/pi/
```

Lastly, add the "Cam.conf" file to the init directory located in etc:

```
~/etc/init/
```

Reboot your Pi, and you should now have a working camera!

## Breaking Down the Software

In this section, I will go through and describe how my Python application works.

### Part 1

```python
from hyperpixel2r import Touch
from picamera import PiCamera
from tkinter import *
from tkinter import ttk
import tkinter.font as fnt
import subprocess
import datetime
import tkinter
import fnmatch
import shutil
import time
import glob
import sys
import os
```
This first part imports all of the modules you will need.

### Part 2

```python
touch = Touch()
```
This creates a variable to gather the touches of the display, which we will need later.

### Part 3

```python
def imageReturn():
    global goBack

    goBack = Tk()
    goBack.attributes('-fullscreen', True)

    menu = Button(
        goBack,
        text="Return to Main Menu",
        command=returnToMenu,
        font=fnt.Font(
            size=20))
    menu.pack()
    menu.place(width=175, height=60, relx=0.5, rely=0.1, anchor='center')
```
This a function that creates a tkinter windows for returning to the main menu called imageReturn().

### Part 4

```python
def returnToMenu():
    camera.stop_preview()
    goBack.withdraw()
    tk.deiconify()
```

### Part 5

```python
tk = Tk()
tk.attributes('-fullscreen', True)
```
This creates the main menu, and assighns it to a variable called tk.

### Part 6

```python
n = tkinter.StringVar()
a = tkinter.StringVar()
m = tkinter.StringVar()
e = tkinter.StringVar()
i = tkinter.StringVar()
f = tkinter.StringVar()
s = tkinter.StringVar()
g = tkinter.StringVar()
```
This creates String Vars for the tkinter widgets.

### Part 7

```python
res_image = ttk.Combobox(tk, textvariable = g)

iso = ttk.Combobox(tk, textvariable = i)

exposure = ttk.Combobox(tk, textvariable = n)

met = ttk.Combobox(tk, textvariable = m)

awb = ttk.Combobox(tk, textvariable = a)

effect = ttk.Combobox(tk, textvariable = e)

fps = ttk.Combobox(tk, textvariable = f)

res = ttk.Combobox(tk, textvariable = s)
```
This creates the Comboboxes for changing the camera settings.

### Part 8

```python
shutter_speed = Scale(tk, from_=0, to=50, tickinterval = 5, orient=VERTICAL)
shutter_speed.set(0)
shutter_speed.place(height=400, relx=0.25, rely=0.5, anchor='center')
```
This creates a slider for changing the shutter speed of the camera.

### Part 9

```python
res['values'] = ('800x600',
                 '720p',
                 '1080p')

res_image['values'] = ('2592×1944',
                       '2464x2464',
                       '3280x2464',
                       '3040x3040',
                       '4056x3040')


fps['values'] = ('12',
                 '24',
                 '30',
                 '40',
                 '50',
                 '60',
                 '90',
                 '120')

met['values'] = ('average',
                 'spot',
                 'backlit',
                 'matrix')

effect['values'] = ('none',
                    'negative',
                    'solarize',
                    'sketch',
                    'denoise',
                    'emboss',
                    'oilpaint',
                    'hatch',
                    'gpen',
                    'pastel',
                    'watercolor',
                    'film',
                    'blur',
                    'saturation',
                    'colorswap',
                    'washedout',
                    'posterise',
                    'colorpoint'
                    'colorbalance',
                    'cartoon',
                    'deinterlace1',
                    'deinterlace2')


awb['values'] = ('off',
                 'auto',
                 'sunlight',
                 'cloudy',
                 'shade',
                 'tungsten',
                 'fluorescent',
                 'incandescent',
                 'flash',
                 'horizon')

exposure['values'] = ('off',
                      'auto',
                      'night',
                      'nightpreview',
                      'backlight',
                      'spotlight',
                      'sports',
                      'snow',
                      'beach',
                      'verylong',
                      'fixedfps',
                      'antishake',
                      'fireworks')

iso['values'] = (0,
                 100,
                 200,
                 320,
                 400,
                 500,
                 640,
                 800,
                 1600)
```
This creates the values for the comboboxes.

### Part 10

```python
effect.current(0)
effect['state'] = 'readonly'
effect.place(width=125, height=30, relx=0.8, rely=0.7, anchor='center')

res_image.current(1)
res_image['state'] = 'readonly'
res_image.place(width=125, height=30, relx=0.8, rely=0.2, anchor='center')

res.current(2)
res['state'] = 'readonly'
res.place(width=125, height=30, relx=0.8, rely=0.3, anchor='center')

fps.current(2)
fps['state'] = 'readonly'
fps.place(width=125, height=30, relx=0.8, rely=0.6, anchor='center')

iso.current(0)
iso['state'] = 'readonly'
iso.place(width=125, height=30, relx=0.8, rely=0.5, anchor='center')

met.current(0)
met['state'] = 'readonly'
met.place(width=125, height=30, relx=0.8, rely=0.4, anchor='center')

awb.current(1)
awb['state'] = 'readonly'
awb.place(width=125, height=30, relx=0.5, rely=0.15, anchor='center')

exposure.current(1)
exposure['state'] = 'readonly'
exposure.place(width=125, height=30, relx=0.5, rely=0.85, anchor='center')
```
This sets the properties of the tkinter widgets, e.g. position, state, etc...

### Part 11

```python
def formatSize(bytes):
    try:
        bytes = float(bytes)
        kb = bytes / 1024
    except:
        return "Error"
    if kb >= 1024:
        M = kb / 1024
        if M >= 1024:
            G = M / 1024
            return "%.2fG" % (G)
        else:
            return "%.2fM" % (M)
    else:
        return "%.2fkb" % (kb)
```
This is a function to convert bytes to gigbytes, megabytes, or kilobytes.

### Part 12

```python
def optionMenu():
    global opt
    opt = Tk()
    usage = shutil.disk_usage("/")
    free_space = formatSize(usage[2])
    total_space = formatSize(usage[0])
    used_space = formatSize(usage[1])
    numb_vid = len(fnmatch.filter(os.listdir("/home/pi/Desktop/"), '*.h264'))
    numb_photo = len(fnmatch.filter(os.listdir("/home/pi/Desktop/"), '*.jpg'))
    string = ('Free Space: {0}, \nTotal Space: {1}, \nUsed Space: {2}, \nNumber of Videos: {3}, \nNumber of Photos: {4}').format(free_space, total_space, used_space, numb_vid, numb_photo)
    opt.wm_attributes("-topmost", 1)
    opt.eval('tk::PlaceWindow . center')
    opt.title("Exit")
    opt.resizable(0, 0)
    opt.geometry("175x215")
    spaceLabel = Label(opt, text=string).place(height=85, relx=0.5, rely=0.5, anchor='center')
    exit = Button(opt, text="Exit", command=stop, font=fnt.Font(size=20))
    clear = Button(opt, text="!Delete All Images!", command=format, font=fnt.Font(size=20))
    clear.place(width=154, height=40, relx=0.5, rely=0.8, anchor='center')
    exit.place(width=154, height=40, relx=0.5, rely=0.2, anchor='center')
```
This is a function that creates the options menu.

### Part 13

```python
def format():
    files = glob.glob('/home/pi/Desktop/*')
    for f in files:
        os.remove(f)
```
This is a function that will format your Raspberry Pi's Desktop. The function is called by the options menu.

### Part 14

```python
def stop():
    tk.iconify()
    opt.withdraw()
#    raise SystemExit
```
This function stops the program, but leaves the touch daemon on. If you wish to completly exit out of the program including the touch daemon, remove the comment on ```raise System Exit```.

### Part 15

```python
imageDate = 0

camera = PiCamera()

height = 0
width = 0
```
The first variable creates a variable for the date exif tag.  The second sets your Pi Camera as a variable called camera. The last two create variables  the width and the height of the image.

### Part 16

```python
def takePicture():
    height = 0
    width = 0
    if res_image.get() == '2592x1944':
        height = 1944
        width = 2592
        camera.resolution = (width, height)
    elif res_image.get() == '2464x2464':
        height = 2464
        width = 2464
        camera.resolution = (width, height)
    elif res_image.get() == '3280x2464':
        height = 2464
        width = 3280
        camera.resolution = (res_image.get())
    elif res_image.get() == '3040x3040':
        height = 3040
        width = 3040
        camera.resolution = (width, height)
    elif res_image.get() == '4056x3040':
        height = 3040
        width = 4056
        camera.resolution = (width, height)
    else:
        camera.resolution = ('2464x2000')

    print("Starting Take Picture")
    tk.withdraw()
    time.sleep(0.5)
    imageReturn()
    camera.start_preview(alpha=250)
    camera.image_effect = effect.get()
    camera.exposure_mode = exposure.get()
    camera.awb_mode = awb.get()
    camera.meter_mode = met.get()
    camera.iso = int(iso.get())
    camera.shutter_speed = (int(shutter_speed.get()) * 1000)
    @touch.on_touch
    def handle_touch(touch_id, x, y, state):
        imageDate = datetime.datetime.now()
        str(imageDate)
        if y > 200 and tk.state() == 'withdrawn' and tk.state() != 'iconic':
            camera.stop_preview()
            camera.exif_tags['EXIF.ShutterSpeedValue'] = str(camera.exposure_speed)
            camera.exif_tags['EXIF.ISOSpeedRatings'] = str(camera.iso)
            camera.exif_tags['EXIF.MeteringMode'] = str(camera.meter_mode)
            camera.capture('/home/pi/Desktop/image{}.jpg'.format(imageDate))
            print("Took Photo with Settings: {0}, {1}, {2}, {3}, {4}, {5}, {6}".format(camera.image_effect, camera.exposure_mode, camera.awb_mode, camera.meter_mode, camera.iso, camera.shutter_speed, camera.resolution))
            time.sleep(int(shutter_speed.get())/10)
            camera.start_preview(alpha=250)
```
This monster of a function is for taking pictures. It decides what the resolution should be, sets the camera settings, and also adds the EXIF tags.

### Part 17

```python
def Options():
    optionMenu()
```
This function calls the Option Menu.

### Part 18

```python
def takeVideo():
    if res.get() == '1080p' and int(fps.get()) > 30 and camera.recording == False:
         camera.framerate = 30
         camera.resolution = res.get()
    elif res.get() == '720p' and int(fps.get()) > 60 and camera.recording == False:
         camera.framerate = 60
         camera.resolution = res.get()
    elif res.get() == '800x600' and camera.recording == False:
         camera.framerate = fps.get()
         camera.resolution = res.get()
         
    time.sleep(2)
    camera.start_preview(alpha=150)
    tk.withdraw()
    
    imageReturn()
    videoDate = 0
    videoState = False
    @touch.on_touch
    def handle_touch(touch_id, x, y, state):
        if y > 200 and tk.state() == 'withdrawn' and tk.state() != 'iconic' and camera.recording == False and camera.resolution != (height, width):
             camera.stop_preview()
             videoDate = datetime.datetime.now()
             print("Started Recording")
             camera.start_recording('/home/pi/Desktop/video{date}.h264'.format(date=videoDate))
             
             time.sleep(0.1)
             camera.start_preview(alpha=250)

        elif y > 200 and tk.state() == 'withdrawn' and tk.state() != 'iconic' and camera.recording == True and camera.resolution != (height, width):
             camera.stop_preview()
             videoDate = datetime.datetime.now()
             print("Stopped Recording")
             camera.stop_recording()
             
             time.sleep(0.1)
             camera.start_preview(alpha=150)
```
Here is another large function! This one is in charge of setting the resolution, and taking videos.

### Part 19

```python
btnCam=Button(tk, text="Picture", command=takePicture, font=fnt.Font(size=20))
btnVid=Button(tk, text="Video", command=takeVideo, font=fnt.Font(size=20))
btnOpt=Button(tk, text="Options", command=Options, font=fnt.Font(size=20))

btnCam.pack()
btnVid.pack()
btnOpt.pack()


btnCam.place(width=125, height=75, relx=0.5, rely=0.5, anchor='center')
btnVid.place(width=125, height=75, relx=0.5, rely=0.3, anchor='center')
btnOpt.place(width=125, height=75, relx=0.5, rely=0.7, anchor='center')
```
This creates the buttons for the main menu.

### Part 20

```python
def main():
    #Starts Hyperpixel Touch Daemon
    p = subprocess.Popen(["sudo",
                         "SDL_FBDEV=/dev/fb0",
                        "python3",
                       "/home/pi/hyperpixel2r-python/examples/uinput-touch.py"])
    tk.deiconify()
    tk.mainloop()

    @touch.on_touch
    def handle_touch(touch_id, x, y, state):
        if tk.state() == 'normal' and camera.preview:
            camera.stop_preview()
        else:
            pass
```
This function runs all of the code for the program.

### Part 21

```python
try:
    main()
except:
    camera.close()
    
    os.execv(sys.executable, ['python3'] + sys.argv)
```
This runs the main loop, and restarts the script in case of any errors.

## Navigating the Software

Once you first boot up your Pi, you will be greeted by the main menu of my camera app. From there, you can enter video or photo mode or manually change the settings of your camera's resolution, exposure, shutter speed, etc.

You can also select the options menu, which allows you to format the Raspberry Pi's desktop, exit the camera app, and view information about your storage.

Now, let's talk about how to operate the different modes, photo, and video.

When you enter photo mode, an overlay of the camera will pop up in whatever resolution you selected. To take a photo, simply, click anywhere in the bottom half of the screen (the overlay will go away for a few milliseconds, once you take a photo). If you wish to return back to the main menu, tap the very top of the screen (that is where the button to return back to the main menu is located), and you will be exited from the photo mode.

Taking videos is slightly different. When you enter video mode, you will once again see the camera's overlay on the screen, but this time, it's translucent. A translucent overlay means that a video is not currently recording, while a solid overlay means that a video is recording. To start recording, tap the bottom half of the display. To stop recording is the same process, just click the bottom half of the screen, and the overlay will become translucent again. (Important, do not exit video mode while recording!)

To manually change the camera's settings, simply tap on a combo box, and select the desired setting.

## Create an Ad-Hoc WIFI Network

When using your camera, you might take it to places where wifi is not accessible. And so, while not mandatory, in this step, I will show you how to create an Ad-Hoc Network using this script: [https://www.raspberryconnect.com/images/hsinstaller/Autohotspot-Setup.tar.xz](https://www.raspberryconnect.com/images/hsinstaller/Autohotspot-Setup.tar.xz)

For full details visit: [https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/183-raspberry-pi-automatic-hotspot-and-static-hotspot-installer](https://www.raspberryconnect.com/projects/65-raspberrypi-hotspot-accesspoints/183-raspberry-pi-automatic-hotspot-and-static-hotspot-installer)

First, download the installer with this command:
```
curl "https://www.raspberryconnect.com/images/hsinstaller/Autohotspot-Setup.tar.xz" -o AutoHotspot-Setup.tar.xz
```
Next extract the contents of the file using this command:
```
tar -xvJf AutoHotspot-Setup.tar.xz
```
Now, go into the Autohotspot directory with the cd command:
```
cd Autohotspot
```
Lastly, run the Autohotspot script with this command:
```
sudo ./autohotspot-setup.sh
```
Now you will be presented with 8 menu options, select option 3, ```Install a Permanent Access Point with eth0 access for connected devices```. Lastly, change the wifi name and password using option 7.

Once you are done with the wifi configuration, exit the script, then reboot the Pi to activate your Ad-Hoc network.

### Conclusion

After reading this Instructable, you should now hopefully be provided with enough knowledge to build your camera.

Because I used a Raspberry Pi Zero W, I encountered memory allocation errors when trying to use the max resolution of the camera, I believe a possible solution may be to upgrade to a Pi Zero 2.

Now, sit back, relax, and enjoy snapping photos with your own DIY Digital Camera.

####If you find any bugs, please post them in the issues section of the repository!
