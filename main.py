import tkinter as tk
from tkinter.colorchooser import askcolor
from os.path import isfile
from led import rgb
from com import send


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
colour1     =   rgb()
colour2     =   rgb()


def check_config(write=False, cip=None, cpt=None):
    if(write):
        with open("cfg/config.cfg", "w") as configs:
            configs.write(cip)
            configs.write(cpt)
        
    else:
        if isfile("cfg/config.cfg"):
            with open("cfg/config.cfg", "r") as configs:
                global com_ip
                global com_port
                com_ip = configs.readline()
                com_port = configs.readline()

def helper_modify_label(label, colour):
    label.config(bg="#%s" %(colour.getHexAsStr()))


#BUTTON HANDLERS

def handler_save_config(msg):
    check_config(True, com_ip, com_port)
    

def handler_load_config(ipDialog=None):
    check_config(False)
    if ipDialog is not None:
        ipDialog.destroy()

def handler_ip_submit(dialog, iptxt, ipprt):
    global com_ip
    global com_port
    com_ip = iptxt.get("1.0", "1.15").strip()
    com_port = ipprt.get("1.0", "1.5").strip()
    dialog.destroy()

def handler_set_colour1(label):
    handler_set_colour(label, 1)
    pass

def handler_set_colour2(label):
    handler_set_colour(label, 2)
    pass

def handler_set_colour(label, btn_num):
    temp_colour = askcolor()
    
    if btn_num == 1:
        global colour1
        colour1 = rgb(temp_colour[0][0], temp_colour[0][1], temp_colour[0][2])
        helper_modify_label(label, colour1)
    else:
        global colour2
        colour2 = rgb(temp_colour[0][0], temp_colour[0][1], temp_colour[0][2])
        helper_modify_label(label, colour2)

def handler_submit(cmdStr):
    send(colour1, colour2, cmdStr, com_ip, com_port)
    pass


#   OPEN_IP
#   
#   Opens the IP settings Dialog
#
#   window: the top level window

def open_IP(window):
    ipDialog = tk.Toplevel(window)
    ipDialog.iconbitmap(BITMAP)
    ipDialog.overrideredirect(True)
    ipDialog.configure(bg=BGCOLOR)
    ipDialog.resizable(width=False, height=False)
    xh = window.winfo_screenwidth()/2 - 75
    yh = window.winfo_screenheight()/2 - 65
    ipDialog.geometry("150x130+%d+%d" %(xh, yh) )

    lbl_setIP = tk.Label(ipDialog, text="Set IP", bg=BGCOLOR, fg=FGCOLOR)
    txt_setIP = tk.Text(ipDialog, height=1, width=15)
    lbl_setPt = tk.Label(ipDialog, text="Set Port", bg=BGCOLOR, fg=FGCOLOR)
    txt_setPt = tk.Text(ipDialog, height=1, width=15)
    btn_submit = tk.Button(ipDialog, text="Submit", command=lambda:handler_ip_submit(ipDialog, txt_setIP, txt_setPt), bg=BGCOLOR, fg=FGCOLOR)
    btn_ldcfg = tk.Button(ipDialog, text="Load Config", command=lambda:handler_load_config(ipDialog), bg=BGCOLOR, fg=FGCOLOR)

    txt_setIP.insert(tk.END, com_ip)
    txt_setPt.insert(tk.END, com_port)

    lbl_setIP.pack(anchor="nw")
    txt_setIP.pack()
    lbl_setPt.pack(anchor="nw")
    txt_setPt.pack()
    btn_submit.pack(side="right")
    btn_ldcfg.pack(side="left")

def main():
    window = tk.Tk()

    window.title("LED Colour Picker v%s" %VERSION)
    window.iconbitmap(BITMAP)
    xh = window.winfo_screenwidth()/2 - WIDTH
    yh = window.winfo_screenheight()/2 - HEIGHT
    window.geometry("640x360+%d+%d" %(xh, yh))
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

    #   INITIALIZE COLOUR BUTTON
    frame_colorchooser = tk.Frame(master=window, width=WIDTH/2, height=HEIGHT/2, bg=BGCOLOR)
    frame_colorchooser.grid(row=0, column=1)


    lbl_currentColour1 = tk.Label(master=frame_colorchooser, width=8)
    btn_setColour = tk.Button(
        master=frame_colorchooser,
        text="Set Colour 1",
        command=lambda:handler_set_colour1(lbl_currentColour1)
    )

    lbl_currentColour1.place(anchor='center', relx=0.3, rely=0.3)
    btn_setColour.place(anchor='center', relx=0.6, rely=0.3)


    lbl_currentColour2 = tk.Label(master=frame_colorchooser, width=8)
    btn_setColour2 = tk.Button(
        master=frame_colorchooser,
        text="Set Colour 2",
        command=lambda:handler_set_colour2(lbl_currentColour2)
    )

    lbl_currentColour2.place(anchor='center', relx=0.3, rely=0.6)
    btn_setColour2.place(anchor='center', relx=0.6, rely=0.6)



    btn_saveConfig = tk.Button(
        master=frame_cButtons,
        text="Save Config",
        command=lambda:handler_save_config(modeSelect)
    )
    btn_saveConfig.place(relx=0.2, rely=0.9, anchor="s", width=80)



    btn_setIP = tk.Button(
        master=frame_cButtons,
        text="Set Network",
        command=lambda:open_IP(window)
    )
    btn_setIP.place(relx=0.5, rely=0.9, anchor="s", width=80)
    
    btn_submit = tk.Button(
        master=frame_cButtons,
        text="Submit",
        command=lambda:handler_submit(modeSelect.get())
    )
    btn_submit.place(relx=0.8, rely=0.9, anchor="s", width=80)

    #color = askcolor()
    #print(color)
    
    check_config(False, com_ip, com_port)
    window.mainloop()


main()