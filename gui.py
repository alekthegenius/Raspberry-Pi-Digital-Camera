"""

gui.py is written by alekthegenius, Copyright ©2022-Present

"""
#Importing Modules
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

#Gets the Touches from the HyperPixel Display
touch = Touch()

#Menu to Return to Main Menu
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


#Function to Return to Menu
def returnToMenu():
    camera.stop_preview()
    goBack.withdraw()
    tk.deiconify()

#Main menu
tk = Tk()
tk.attributes('-fullscreen', True)

#String Vars for Combobox
n = tkinter.StringVar()
a = tkinter.StringVar()
m = tkinter.StringVar()
e = tkinter.StringVar()
i = tkinter.StringVar()
f = tkinter.StringVar()
s = tkinter.StringVar()
g = tkinter.StringVar()

#Creates Combobox
res_image = ttk.Combobox(tk, textvariable = g)

iso = ttk.Combobox(tk, textvariable = i)

exposure = ttk.Combobox(tk, textvariable = n)

met = ttk.Combobox(tk, textvariable = m)

awb = ttk.Combobox(tk, textvariable = a)

effect = ttk.Combobox(tk, textvariable = e)

fps = ttk.Combobox(tk, textvariable = f)

res = ttk.Combobox(tk, textvariable = s)

#Creates Slider
shutter_speed = Scale(tk, from_=0, to=50, tickinterval = 5, orient=VERTICAL)
shutter_speed.set(0)
shutter_speed.place(height=400, relx=0.25, rely=0.5, anchor='center')

#Values for the Tkinter Widgets

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

#Set Properties of Tkinter Widgets

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

#Function to format Size of kB to GB, found in Stackoverflow
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


#Option Menu
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

#Removes all filles on Desktop
def format():
    files = glob.glob('/home/pi/Desktop/*')
    for f in files:
        os.remove(f)


def stop():
    tk.iconify()
    opt.withdraw()
#    raise SystemExit


imageDate = 0

camera = PiCamera()

#camera.framerate = 15
height = 0
width = 0

#Function for Taking Pictures
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

def Options():
    optionMenu()

#Function for Taking Videos
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

#Buttons on the Main Menu
btnCam=Button(tk, text="Picture", command=takePicture, font=fnt.Font(size=20))
btnVid=Button(tk, text="Video", command=takeVideo, font=fnt.Font(size=20))
btnOpt=Button(tk, text="Options", command=Options, font=fnt.Font(size=20))

btnCam.pack()
btnVid.pack()
btnOpt.pack()


btnCam.place(width=125, height=75, relx=0.5, rely=0.5, anchor='center')
btnVid.place(width=125, height=75, relx=0.5, rely=0.3, anchor='center')
btnOpt.place(width=125, height=75, relx=0.5, rely=0.7, anchor='center')

#Main Loop
def main():
    #Starts Hyperpixel Touch Script
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
#Runs the Application
try:
    main()
except:
    camera.close()
    
    os.execv(sys.executable, ['python3'] + sys.argv)
