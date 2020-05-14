import psutil
import time
import winsound


def switch_off():
	min_wait = 3
	max_wait = 90
	wait_counter = min_wait
	while True:
		
		# to decrease CPU utilization (kind off backoff-retry)
		if wait_counter >= max_wait:
			wait_counter = min_wait
		
		time.sleep(wait_counter)
		
		battery = psutil.sensors_battery()
		plugged = battery.power_plugged
		
		if plugged and battery.percent > 92:
			winsound.PlaySound(r"D:\desktop\code-works\battery_save\Wecker-sound.wav",
			flags=winsound.MB_ICONASTERISK)
			
		wait_counter += 1
		

if __name__ == "__main__":
	switch_off()