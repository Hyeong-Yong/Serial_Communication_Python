import serial # conda install serial
import time
#              python     C 
# int          4byte    4byte
# float        8byte    4byte
# INT로 전송해서 나누기

def getInit_2Byte(data):
    if data is None:
        return 0
    value = ( (0x000000ff & int.from_bytes(data[0], byteorder="little")) | ( 0x0000ff00 & int.from_bytes(data[1], byteorder="little")<<8 ) )
    return value


############################## START 초기화 코드  ########################################
ser = serial.Serial(
    # Window
    port='COM30',
    # 보드 레이트 (통신 속도)
    baudrate=57600,
)

if (ser.is_open == False):
    ser.open()
############################## END 초기화 코드  ####################################

#----------------------------------------------------------------------------#


############################## START 점도센서값 쓰기(PC to MCU) ##################################
viscosity_value = 22115

byte_1= viscosity_value     & 0x000000ff
byte_2= viscosity_value>>8  & 0x000000ff
byte_3= viscosity_value>>16 & 0x000000ff
byte_4= viscosity_value>>24 & 0x000000ff

ser.write(bytes(byte_1.to_bytes(1, byteorder="little")))
ser.write(bytes(byte_2.to_bytes(1, byteorder="little")))
ser.write(bytes(byte_3.to_bytes(1, byteorder="little")))
ser.write(bytes(byte_4.to_bytes(1, byteorder="little")))
print(byte_1)
print(byte_1.to_bytes(1, byteorder="little"))
############################# END 점도센서값 쓰기 (PC to MCU) ####################


#----------------------------------------------------------------------------#
i=0
data =[]
######################### START 온도센서값 받기(MCU to PC)######################
try:
    while True:
            if ser.readable():
                res= ser.read(1)
                if (i ==0):
                    data.append(res)
                    i=i+1
                elif (i==1):
                    data.append(res)
                    i=2
                    
            if(i==2):
                res_int=getInit_2Byte(data)
                print(res_int)
                i=0
                data.clear()   

            
            
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
######################### END 온도센서값 전송(MCU to PC)########################
    
    
#----------------------------------------------------------------------------#

############################# START 프로그램 종료 ############################

ser.close()

############################# END 프로그램 종료 ##############################
