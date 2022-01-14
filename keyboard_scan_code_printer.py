import keyboard

while True:
	keyboard_event = keyboard.read_event()
	scan_code = keyboard_event.scan_code
	print(f'Key with scancode {scan_code} pressed')