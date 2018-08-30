with open('savefiles/LocalPlayer.arkprofile', 'rb') as file:
	print('Version: ', int.from_bytes(file.read(4), byteorder='little'))
	print('Objects: ', int.from_bytes(file.read(4), byteorder='little'))
