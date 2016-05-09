import serial

ser = serial.Serial('/dev/ttyACM1', 9600)
fp = open('values.txt', 'w')

while True:
#    A = str(abs(float(ser.readline())))
    A = ser.readline()
    fp.write(A)
#    fp.write("\n")
    print A,


