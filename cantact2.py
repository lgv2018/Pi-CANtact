from pyvit.hw import cantact
import sys

dev = cantact.CantactDev(sys.argv[1])

dev.ser.write('S0\r'.encode())
dev.start()
count = 0
while True:
    count = count + 1
    frame = dev.recv()
    dev.send(frame)
    print("%d: %s" % (count, str(frame)))
