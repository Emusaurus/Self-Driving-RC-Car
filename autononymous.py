#unused
from datetime import datetime
datetime.now().strftime('%H:%M:%S')
length = int(input("Ft to move: "))
if length < 0:
  print('Invalaid input')
speed = 5 #ft/s
movingtime = length/speed
