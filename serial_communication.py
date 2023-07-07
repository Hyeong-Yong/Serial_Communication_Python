import serial # conda install serial
import time
import struct
import numpy as np
#         python     C 
# int      4byte    4byte
# float    8byte    4byte
# int로 넘겨서 /(나누기) 해야함 


py_serial = serial.Serial(
    
    # Window
    port='COM30',
    
    # 보드 레이트 (통신 속도)
    baudrate=57600,
)


while True:
    commend = input('abs')
    value = 102
    byte_1= value     & 0x000000ff
byte_2= value>>8  & 0x000000ff
byte_3= value>>16 & 0x000000ff
byte_4= value>>24 & 0x000000ff
    py_serial.wr
    py_serial.write(bytes(bytearray([value_np])))
    py_serial.write(bytes(bytearray([value_np >>8])))
    py_serial.write(bytes(bytearray([value_np >>8])))
    py_serial.write(bytes(bytearray([value_np >>8])))


#    byte_arr = bytearray(struct.pack("f", value))
 #   byte_list = [b for b in byte_arr]
  ## print(type(byte_list))
   # ser.write(bytes(byte_list[0]))
   # ser.write(bytes(byte_list[1]))

    time.sleep(0.1)
    
    if py_serial.readable():
        
        # 들어온 값이 있으면 값을 한 줄 읽음 (BYTE 단위로 받은 상태)
        # BYTE 단위로 받은 response 모습 : b'\xec\x97\x86\xec\x9d\x8c\r\n'
        response = py_serial.readline()
        
        # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
        print(response[:len(response)-1].decode())