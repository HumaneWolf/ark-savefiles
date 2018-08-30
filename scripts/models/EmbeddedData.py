class EmbeddedData:
    def __init__(self, path, parts):
        self.path = path
        self.parts = parts

class Part:
    def __init__(self, blobs):
        self.blobs = blobs

class Blob:
    def __init__(self, words):
        self.words = words
