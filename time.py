#!/usr/bin/env python
import unicornhat as unicorn
import random
import time
import datetime

lastMinute = 0

while True:
	unicorn.brightness(0.2)
	unicorn.rotation(180)

	now = datetime.datetime.now()
	hour = now.hour - 12 if now.hour > 11 else now.hour
	minute = now.minute

	if lastMinute != minute: 
		lastMinute = minute
		unicorn.off()

	#set hour
	for x in range(0,hour):
		if x > 7:
			unicorn.set_pixel(x - 7,1,255,0,0)
		else:
			unicorn.set_pixel(x,0,255,0,0)

	#set minute


	if minute // 10 > 0:
		for x in range(0, minute // 10):
			if x % 2 == 0:
				unicorn.set_pixel(x, 4, 0,0,255)
			else:
				unicorn.set_pixel(x, 4, 255,0,0)

	if minute % 10 > 8:
		unicorn.set_pixel(0,5,255,165,0)
		unicorn.set_pixel(7,5,255,0,0)
	else:
		unicorn.set_pixel(minute % 10 -1,5,255,0,0)
	unicorn.show()
	time.sleep(1)

