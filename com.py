import socket as sk
import led

def sendToStrip(clr):
    rgb = clr.get()