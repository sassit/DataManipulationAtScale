import sys
import json


def parseJson(tweetFile):
    data = []
    for line in tweetFile:
        data.append(json.loads(line))
    return data


def calculateOccurence(data):
    occurence = {}
    total = 0
    for item in data:
        if 'text' not in item or item['text'] is None:
            continue
        text = item['text']
        text = text.encode('utf-8')
        tokens = text.split()
        for token in tokens:
            if token in occurence:
                occurence[token] += 1
            else:
                occurence[token] = 1
            total += 1
    return occurence, total


def writeFrequency(frequency):
    for key, value in frequency[0].iteritems():
        print key + " " + str(value / frequency[1])


def main():
    data = parseJson(open(sys.argv[1]))
    frequency = calculateOccurence(data)
    writeFrequency(frequency)


if __name__ == '__main__':
    main()
