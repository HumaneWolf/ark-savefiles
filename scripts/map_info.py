from utils.ArkSaveReader import ArkSaveReader

with ArkSaveReader('savefiles/TheIsland.ark') as save:
	print('    == HEADER ==')
	print('Version: ', save.read_int(2))
	print('Unknown 1 (was nameOffset in v6): ', save.read_wildcard(4))
	print('Unknown 2 (was propertiesOffset in v6): ', save.read_wildcard(4))
	print('Unknown 3 (was gameTime(float32) in v6, possible list of names offset): ', save.read_wildcard(4))
	print('Unknown 4 (possible offset for additional data, or maybe object list): ', save.read_wildcard(4))
	print('Unknown 5 (possible gametime in seconds, float32): ', save.read_wildcard(4))
	print('Unknown 6: ', save.read_wildcard(4))

	print('\n    == REFERENCES TO DATAFILES ==')
	number_of_datafiles = save.read_int(4)
	print('Number of files: ', number_of_datafiles)
	for i in range(0, number_of_datafiles):
		datafile = save.read_string()
		print(format(i, '02d'), ' => ', datafile)
	
	print('\n    == EMBEDDED DATA ==')
	number_of_embeds = save.read_int(4)
	print('Number of embedded data: ', number_of_embeds)
	for i in range(0, number_of_embeds):
		data = save.read_embedded_data()
		print(format(i, '02d'), ' => ', data.path, '- with', len(data.parts), 'parts')
		for j in range(0, len(data.parts)):
			part = data.parts[j]
			print('    => Blobs in part: ', len(part.blobs))
			for k in range(0, len(part.blobs)):
				blob = part.blobs[k]
				print('    =>     => Int32 words in blob: ', len(blob.words))
