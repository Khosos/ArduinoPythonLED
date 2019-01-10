import serial
import time

ArduinoSerial = serial.Serial('com4', 9600)
time.sleep(2)

print (ArduinoSerial.readline())
print("1 for ON, 0 for OFF")

while(true):
      var = raw_input()

      if(var == '1'):
          ArduinoSerial.write('1')
          time.sleep(1)
      if(var == '0'):
          ArduinoSerial.write('0')
          time.sleep(1)
      
