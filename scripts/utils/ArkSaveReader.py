import struct

from models import EmbeddedData

class ArkSaveReader:
	# Class Utils
	def __init__(self, filename):
		self._file = open(filename, 'rb')
	
	def __enter__(self):
		return self
	
	def __exit__(self, type, value, traceback):
		self.close()
	
	# Close file.
	def close(self):
		self._file.close()

	# Seek to a position in the file.
	def seek(self, offset, position='start'):
		start_position = {
			'start' : 0,
			'rel'   : 1,
			'stop'  : 2,
		}
		self._file.seek(offset, start_position)
	
	# Get position
	def tell(self):
		return self._file.tell()
	
	#
	# READING SIMPLE VALUES
	#

	# Mostly used to help find what portions of the file can be.
	def read_wildcard(self, bytes):
		data = self._file.read(bytes)
		return (int.from_bytes(data, byteorder='little', signed=True),
			int.from_bytes(data, byteorder='little', signed=False),
			struct.unpack('f', data)[0])
	
	# Read the given amount of bytes as a signed integer.
	def read_int(self, bytes):
		return int.from_bytes(self._file.read(bytes), byteorder='little', signed=True)
	
	# Read the given amount of bytes as an unsigned integer.
	def read_uint(self, bytes):
		return int.from_bytes(self._file.read(bytes), byteorder='little', signed=False)
	
	# Read the given amount of bytes as a floating point.
	def read_float(self, bytes):
		return struct.unpack('f', self._file.read(bytes))[0]
	
	# Read the string
	def read_string(self):
		string_length = self.read_int(4)
		if (string_length < 0):
			return self._file.read(abs(string_length * 2)).decode('utf-16')
		else:
			return self._file.read(string_length).decode('ascii')
	
	#
	# READING MORE ADVANCED OBJECTS
	#

	# Read an Embedded Data object
	def read_embedded_data(self):
		path = self.read_string()
		part_count = self.read_int(4)
		parts = []
		for i in range(0, part_count):
			blob_count = self.read_int(4)
			blobs = []
			for i in range(0, blob_count):
				word_count = self.read_int(4)
				words = []
				for i in range(0, word_count):
					words.append(self.read_int(4))
				blobs.append(EmbeddedData.Blob(words))
			parts.append(EmbeddedData.Part(blobs))
		return EmbeddedData.EmbeddedData(path, parts)
