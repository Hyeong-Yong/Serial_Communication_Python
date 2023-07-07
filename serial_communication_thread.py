import serial
import threading
import time

port= "COM4"
baud = 115200
ser = serial.Serial(port, baud, timeout=1)

def main():
    thread = threading.Thread(target=readthread, args=(ser,))
    thread.start()
    
    viscosity_value = 22115

    byte_1= viscosity_value     & 0x000000ff
    byte_2= viscosity_value>>8  & 0x000000ff
    byte_3= viscosity_value>>16 & 0x000000ff
    byte_4= viscosity_value>>24 & 0x000000ff
    
    ser.write(bytes(byte_1.to_bytes(1, byteorder="little")))
    ser.write(bytes(byte_2.to_bytes(1, byteorder="little")))
    ser.write(bytes(byte_3.to_bytes(1, byteorder="little")))
    ser.write(bytes(byte_4.to_bytes(1, byteorder="little")))
        
def readthread(ser):
    while True:
        
        if ser.readable():
            res= ser.readline()
            print(res)
            
    ser.close()
    
    
main()