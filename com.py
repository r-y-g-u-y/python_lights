import socket as sk
import led



class ledPacket:
    command = "off"
    data = []
    def __init__(self, cmd="off", d=[]):
        command = cmd
        data = d

    def _cmd2byte(self, command):
        cmd = {
            "off"       :   0x00,
            "solid"     :   0x01,
            "gradient"  :   0x02
        }
        return cmd.get(command, 0x00)

    def pack(self):
        

    
    


