with open('savefiles/1445416994.arktribe', 'rb') as file:
	print('Version: ', int.from_bytes(file.read(4), byteorder='little'))
	print('Objects: ', int.from_bytes(file.read(4), byteorder='little'))
