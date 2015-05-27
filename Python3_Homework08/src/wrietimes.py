import time, os, struct

filename = r"v:\workspace\Python3_Homework08\src\wireshark.bin"
f = open(filename, "rb")
wireshark_file_header = "IHHIIII"
print("Header")
for value in wireshark_file_header:
    if value == "I":
        s = f.read(4)
    if value == "H":
        s = f.read(2)
    x, = struct.unpack("={0}".format(value), s)
    print(x)
packs = "IIII"
seconds = 0
microseconds = 0
data_size_packet = 0
data_size_original_packet = 0
current_packet = 1
while True:
    current_position = f.tell()
    
    s = f.read(4)
    if s == b'':
        break
    else:
        f.seek(current_position)
        
    for num, val in enumerate(packs):
        s = f.read(4)
        x, = struct.unpack("={0}".format(val), s)
        if num == 0:
            seconds = x
        elif num == 1:
            microseconds = x
            timestamp = ".".join((str(seconds), str(microseconds)))
            print("Packet: {0:2} timestamp: {1}".format(current_packet,timestamp))
            current_packet +=1
        elif num == 2:
            data_size_packet = x
        else:
            data_size_original_packet = x
            f.read(data_size_packet)
