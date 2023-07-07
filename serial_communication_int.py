import serial # conda install serial

#              python     C 
# int          4byte    4byte
# float        8byte    4byte
# INT로 전송해서 나누기


############################## START 초기화 코드  ########################################
py_serial = serial.Serial(
    # Window
    port='COM4',
    # 보드 레이트 (통신 속도)
    baudrate=57600,
)

if (py_serial.is_open == False):
    py_serial.open()
############################## END 초기화 코드  ####################################



############################## START 점도센서값 전송(PC to MCU) ##################################
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
############################# END 점도센서값 전송(PC to MCU) ####################



######################### START 온도센서값 전송(MCU to PC)######################



######################### END 온도센서값 전송(MCU to PC)########################
while True:
    
    

############################# START 프로그램 종료 ############################

py_serial.close()

############################# END 프로그램 종료 ##############################

