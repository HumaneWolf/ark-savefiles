from utils.ArkSaveReader import ArkSaveReader

with ArkSaveReader('savefiles/TheIsland.ark') as save:
	print('    == HEADER ==')
	print('Version: ', save.read_int(2))
	print('Unknown 1 (was nameOffset in v6): ', save.read_wildcard(4))
	print('Unknown 2 (was propertiesOffset in v6): ', save.read_wildcard(4))
	print('Unknown 3 (was gameTime(float32) in v6): ', save.read_wildcard(4))
	print('Unknown 4: ', save.read_wildcard(4))
	print('Unknown 5: ', save.read_wildcard(4))
	print('Unknown 6: ', save.read_wildcard(4))

	print('\n    == REFERENCES TO DATAFILES ==')
	number_of_datafiles = save.read_int(4)
	print('Number of files: ', number_of_datafiles)
	for i in range(0, number_of_datafiles):
		datafile = save.read_string()
		print(format(i, '02d'), ' => ', datafile)
	
	print('\n    == EMBEDDED DATA ==')
