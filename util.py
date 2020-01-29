import re

# Returns the type of given column index, y
def getType(matrix, y):
    isBool = True
    isInt = True
    isFloat = True
    isString = True

    for x in range(0, len(matrix)):
        if len(matrix[x]) > y:
            if isBool == True:
                isBool = boolHuh(matrix[x][y])
            if isInt == True:
                isInt = intHuh(matrix[x][y])
            if isFloat == True:
                isFloat = floatHuh(matrix[x][y])

    if isBool : return "BOOL"
    elif isInt : return "INT"
    elif isFloat : return "FLOAT"
    else : return "STRING"

# Returns whether element is a boolean
def boolHuh(element):
    return element == "1" or element == "0" or element == ""

# Returns whether element is an integer
def intHuh(element):
    try:
        int(element)
        return True
    except ValueError:
        return False or boolHuh(element)

# Returns whether element is a float
def floatHuh(element):
    try:
        float(element)
        return True
    except ValueError:
        return False or intHuh(element)

# Returns whether element is a string
def stringHuh(element):
    return not boolHuh(element) and not intHuh(element) and not floatHuh(element)

# Check that columnType and element type match
def compareType(columnType, element):
    if columnType == "BOOL":
        if not boolHuh(element): raise Exception("Value in column offset does not match column type")
    elif columnType == "INT":
        if not intHuh(element): raise Exception("Value in column offset does not match column type")
    elif columnType == "FLOAT":
        if not floatHuh(element): raise Exception("Value in column offset does not match column type")
    # else:
    #     if not stringHuh(element): raise Exception("Value in column offset does not match column type")

# Returns a list representation of a string row, splitting the string at matching <>
def parseRow(line):
    lineSplit = re.findall("\< *(.*?) *\>", line)
    valid = True
    for item in lineSplit:
        if ' ' in item: # only allow strings with spaces if surrounded by double quotes
            if not (item.startswith("\"") and item.endswith("\"")):
                valid = False
                break
    if valid:
        return lineSplit
    else:
        return []

    return lineSplit