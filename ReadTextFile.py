class ReadTextFile:

    def __init__(self, pathtofile):
        self.filepath = pathtofile

    def openfile(pathtofile):
        ArrayOfWords = []
        with open(pathtofile, "r") as line:
            data = line.readlines()
        for line in data:
            words = line.split()
            ArrayOfWords.append(line.strip())
            # print(words)

        return ArrayOfWords






