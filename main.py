import tkinter as tk
from tkinter.colorchooser import askcolor
from os.path import isfile


#   CONSTANTS
VERSION = "0.1"
BITMAP = "cfg/colourimage.ico"
BGCOLOR = "#4c4a48" # background colour
FGCOLOR = "#DDDDDD" # foreground / text colour
SLCOLOR = "#5d5b59" # radio button select colour
WIDTH = 640
HEIGHT = 480

MODES = [
    ("OFF", "off"),
    ("SOLID", "solid"),
    ("GRADIENT", "gradient")
]

#   VARIABLES  
com_ip      =   "192.168.0.100"
com_port    =   "55555"
modeSelect  =   None

def check_config(write=False):
    if(write):
        with open("cfg/config.cfg", "w") as configs:
            configs.write(com_ip)
            configs.write(com_port)
        
    else:
        if isfile("cfg/config.cfg"):
            with open("cfg/config.cfg", "r") as configs:
                com_ip = configs.readline()
                com+port = configs.readline()


def main():
    window = tk.Tk()
    
    window.title("LED Colour Picker v%s" %VERSION)
    window.iconbitmap(BITMAP)
    window.geometry("640x360")
    window.configure(background=BGCOLOR)
    window.resizable(width=False, height=False)

    frame_modeselect = tk.Frame(master=window, width=(WIDTH/2), bg=BGCOLOR)
    frame_modeselect.pack(fill=tk.Y, side=tk.LEFT)
    frame_option = tk.Frame(master=window, width=(WIDTH/2), bg=BGCOLOR)
    frame_option.pack(fill=tk.Y, side=tk.LEFT)

    modeSelect = tk.StringVar(master=frame_modeselect)
    modeSelect.set("off")



    #color = askcolor()
    #print(color)
    for text, mode in MODES:
        b = tk.Radiobutton( master=frame_modeselect, 
                            text=text, 
                            variable=modeSelect, 
                            value=mode, 
                            bg=BGCOLOR, 
                            indicatoron=0, 
                            fg=FGCOLOR, 
                            selectcolor=SLCOLOR,
                            width="12"
                            )
        b.pack(anchor='w')



    window.mainloop()


main()