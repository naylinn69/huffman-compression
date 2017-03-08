import sys
import json
import utils
from bitstring import BitArray

def encode(text):
    """Summary
    
    Args:
        text (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    charCount = utils.countCharaters(text)
    numOfChar = sum(charCount.values())
    charFreq = {char: float(count)/numOfChar for char, count in charCount.items()}
    if len(charFreq) == 1:
        char2Code = {char: '0' for (char, _) in charFreq.items()}
    else:
        encodingTree = utils.buildEncodingTree(charFreq)
        char2Code = encodingTree.getCodes()
    encodedText = BitArray("")
    for char in text:
        code = "0b" + char2Code[char]
        encodedText += BitArray(code)
    return encodedText, char2Code

def runFromFile(inputFilename, outputFilename):
    try:
        with open(inputFilename) as inputFile:
            text = inputFile.read()
    except IOError:
        print "Cannot read file \"{}\".".format(inputFilename)
        return
    encodedText, char2Code = encode(text)
    numOfBytes = len(encodedText.bin) // 8
    with open(outputFilename, 'wb') as outputFile:
        json.dump(char2Code, outputFile, separators=(',',':'))
        outputFile.write("\n")
        json.dump(numOfBytes, outputFile, separators=(',',':'))
        outputFile.write("\n")
        outputFile.write(encodedText[:numOfBytes*8].bytes)
        outputFile.write(encodedText[numOfBytes*8:].bin)

def main():
    """Main function that drives the program.
    
    Returns:
        None: Nothing
    """
    if len(sys.argv) == 1:
        runInteractive()
    elif len(sys.argv) == 3:
        runFromFile(sys.argv[1], sys.argv[2])
    else:
        print "Usage: python compress.py \"inputFile\" \"OutputFile\""

if __name__ == '__main__':
    main()
