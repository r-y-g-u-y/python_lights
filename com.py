import socket as sk
import led

HEADER = 'abab'
FOOTER = 'cdcd'

def send(colour1, colour2, command, ip, port, value):
    print("Getting ready to send")
    outPkt = ledPacket(command, [colour1, colour2, value], ip, port)
    outPkt.send()
    pass

class ledPacket:
    ip = None
    port = 0
    command = "off"
    data = []

    def __init__(self, cmd="off", d=[], ip=None, port=0):
        self.ip = ip
        self.port = int(port)
        self.command = cmd
        self.data = d
        print("packing data: " + cmd + str(d) + "\nsending to " + ip + ':' + port)
        
    def _cmd2byte(self):
        cmd = {
            "off"       :   '00',
            "solid"     :   '01',
            "gradient"  :   '02'
        }
        return cmd.get(self.command, 0x00)

    def pack(self):
        print("packing payload...")
        payload = HEADER + self._cmd2byte() + self.data[0].getHexAsStr() + self.data[1].getHexAsStr() + hex(self.data[2])[2:].zfill(2) + FOOTER
        print("payload = " + payload)
        return payload

    def send(self):
        print("opening socket and sending")
        sock = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
        sock.sendto(bytes.fromhex(self.pack()), (self.ip, self.port))
        print("done sending! closing socket")
        sock.close()
        return 1

    
    


