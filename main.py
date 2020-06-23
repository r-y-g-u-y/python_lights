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
HEIGHT = 360

MODES = [
    ("OFF", "off"),
    ("SOLID", "solid"),
    ("GRADIENT", "gradient")
]

#   VARIABLES  
com_ip      =   "192.168.0.100"
com_port    =   "55555"
modeSelect  =   None

def check_config(write=False, cip=None, cpt=None):
    if(write):
        with open("cfg/config.cfg", "w") as configs:
            configs.write(cip)
            configs.write("\n")
            configs.write(cpt)
        
    else:
        if isfile("cfg/config.cfg"):
            with open("cfg/config.cfg", "r") as configs:
                global com_ip
                global com_port
                com_ip = configs.readline()
                com_port = configs.readline()

def save_config():
    check_config(True, com_ip, com_port)

def load_config():
    check_config(False)



def main():
    window = tk.Tk()
    
    window.title("LED Colour Picker v%s" %VERSION)
    window.iconbitmap(BITMAP)
    window.geometry("640x360")
    window.configure(background=BGCOLOR)
    window.resizable(width=False, height=False)
    for i in range(2):
        window.rowconfigure(i, weight=1, minsize=HEIGHT/2)
        window.columnconfigure(i, weight=1, minsize=WIDTH/2)
            
    
    #   INITIALIZE RADIO BUTTONS
    frame_modeselect = tk.Frame(master=window, width=(WIDTH/2), height=(HEIGHT/2),bg="#00bb00")
    frame_modeselect.grid(row=0,column=0)
    
    modeSelect = tk.StringVar(master=frame_modeselect)
    modeSelect.set("off")

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
        b.pack(anchor='center')

    #   INITIALIZE MODE OPTIONS
    frame_option = tk.Frame(master=window, width=(WIDTH/2), height=HEIGHT/2, bg=BGCOLOR)
    frame_option.grid(row=1,column=0)
    
    #   INITIALIZE CONFIG BUTTONS
    frame_cButtons = tk.Frame(master=window, width=WIDTH/2, height=HEIGHT/2, bg=BGCOLOR)
    frame_cButtons.grid(row=1, column=1)

    btn_saveConfig = tk.Button(
        master=frame_cButtons,
        text="Save Config",
        command=save_config
    )
    btn_saveConfig.place(relx=0, rely=0.9, anchor="sw")

    btn_loadConfig = tk.Button(
        master=frame_cButtons,
        text="Load Config",
        command=load_config
    )
    btn_loadConfig.place(relx=0.5, rely=0.9, anchor="s")
    

    #color = askcolor()
    #print(color)
    

    window.mainloop()


main()