import json
import sys
import utils

def decode(encodedText, char2Code, numOfBytes):
    binaryStr = ''.join(format(x, '08b') for x in bytearray(encodedText[:numOfBytes]))
    binaryStr += encodedText[numOfBytes:]
    code2Char = {str(code): str(char) for char, code in char2Code.items()}
    code = ""
    text = ""
    for bit in binaryStr:
        code += bit
        if code in code2Char:
            text += code2Char[code]
            code = ""
    return text

def runFromFile(inputFilename, outputFilename):
    try:
        with open(inputFilename, 'rb') as inputFile:
            char2Code = json.loads(inputFile.readline())
            numOfBytes = json.loads(inputFile.readline())
            encodedText = inputFile.read()
    except IOError:
        print "Cannot read file \"{}\".".format(inputFilename)
        return
    text = decode(encodedText, char2Code, numOfBytes)
    with open(outputFilename, 'w') as outputFile:
        outputFile.write(text)

def main():
    if len(sys.argv) == 3:
        runFromFile(sys.argv[1], sys.argv[2])
    else:
        print "Usage: python decompress.py \"inputFile\" \"OutputFile\""

if __name__ == '__main__':
    main()
