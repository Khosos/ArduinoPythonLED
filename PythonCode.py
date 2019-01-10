import serial
import time

arduino = serial.Serial('COM4', 9600)
time.sleep(2)

while True:
    var = input("Enter 1 or 0")

    if(var == '1'):
        arduino.write(str.encode('1'))
        time.sleep(1)

    elif(var == '0'):
        arduino.write(str.encode('0'))
        time.sleep(1)
    

