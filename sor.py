import util

class SoR:

    def __init__(self):
        self.schema = [] # Represents the schema for the types of the columns
        self.data = [] # Represents the data read in
        self.numColumns = 0 # Represents the number of columns

    def getSchema(self):
        return self.schema

    def getData(self):
        return self.data
    
    # Generates schema from the first 500 lines or less from file provided
    def generateSchema(self, f):
        content = []
        index = 0
        maxColumns = 0
        tmp = f.readline()

        while index < 499 and tmp != "":
            row = util.parseRow(tmp)
            maxColumns = max(len(row), maxColumns)
            if len(row) != 0:
                content.append(row)
            index += 1
            tmp = f.readline()

        fileSchema = []
        for y in range(0, maxColumns):
            fileSchema.append(util.getType(content, y))
        self.schema = fileSchema
        self.numColumns = len(self.schema)

    # Returns column type from generated schema
    def getColumnType(self, index):
        if (index < len(self.schema)): return self.schema[index]
        else: raise Exception("Invalid Column Index")

    def addParsedLine(self, line):
        parsedLine = util.parseRow(line)
        if (len(parsedLine) < self.numColumns):
            leftoverSpace = [''] * (self.numColumns - (len(parsedLine)))
            parsedLine += leftoverSpace
        self.data.append(parsedLine)

    # Generates data from the desired start byte up to the EOF or the length
    def generateData(self, f, start, length, fileLength):
        numBytesRead = 0

        f.seek(start, 0)
        if start != 0:
            prevline = f.readline()
            line = f.readline()
            numBytesRead += len(line) + len(prevline)
        else:
            line = f.readline()
            prevline = line
            numBytesRead += len(prevline)

        while numBytesRead < length and line != '':
            prevline = line
            self.addParsedLine(prevline)

            line = f.readline()
            numBytesRead += len(line)
        
        if start + length >= fileLength: self.addParsedLine(line)

    # Returns the element at specified column and row if valid
    def getElement(self, column, row):
        if column >= self.numColumns: raise Exception("Column index out of bounds")
        if row >= len(self.data): raise Exception("Row index out of bounds")
        return self.data[row][column]

    