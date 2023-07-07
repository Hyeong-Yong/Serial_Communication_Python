import serial # conda install serial
import time
import struct
import numpy as np
#              python     C 
# int          4byte    4byte
# float        8byte    4byte
# np.float32   4byte    4byte    

py_serial = serial.Serial(
    # Window
    port='COM4',
    # 보드 레이트 (통신 속도)
    baudrate=57600,
)

if (py_serial.is_open == False):
    py_serial.open()

viscosity_value = 22115

byte_1= viscosity_value     & 0x000000ff
byte_2= viscosity_value>>8  & 0x000000ff
byte_3= viscosity_value>>16 & 0x000000ff
byte_4= viscosity_value>>24 & 0x000000ff

py_serial.write(bytes(byte_1.to_bytes(1, byteorder="little")))
py_serial.write(bytes(byte_2.to_bytes(1, byteorder="little")))
py_serial.write(bytes(byte_3.to_bytes(1, byteorder="little")))
py_serial.write(bytes(byte_4.to_bytes(1, byteorder="little")))
print(byte_1)
print(byte_1.to_bytes(1, byteorder="little"))

py_serial.close()

#while False:
    #byte_arr = bytearray(struct.pack("f", value))
    #byte_list = [b for b in byte_arr]
    #print(type(byte_list))
    #ser.write(bytes(byte_list[0]))
   # ser.write(bytes(byte_list[1]))

#    time.sleep(0.1)
    
 #   if py_serial.readable():
        
        # 들어온 값이 있으면 값을 한 줄 읽음 (BYTE 단위로 받은 상태)
        # BYTE 단위로 받은 response 모습 : b'\xec\x97\x86\xec\x9d\x8c\r\n'
#        response = py_serial.readline()
        
        # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
 #       print(response[:len(response)-1].decode())