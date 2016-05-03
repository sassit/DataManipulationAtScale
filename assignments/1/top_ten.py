import sys
import json
from heapq import nlargest


def parse_json(tweet):
    data = []
    for line in tweet:
        data.append(json.loads(line))
    return data


def calculate_occurence(data):
    occurence = {}
    for item in data:
        if 'entities' not in item:
            continue
        entities = item['entities']
        if 'hashtags' not in entities or entities['hashtags'] is None:
            continue
        hashtags = entities['hashtags']
        for hashtag in hashtags:
            text = hashtag['text']
            text = text.encode('utf-8')
            if text in occurence:
                occurence[text] += 1
            else:
                occurence[text] = 1
    return occurence


def print_top_ten(occurence):
    for ranking in sorted(occurence.items())[:10]:
        print ranking[0] + " " + str(ranking[1])


def main():
    data = parse_json(open(sys.argv[1]))
    occurrence = calculate_occurence(data)
    print_top_ten(occurrence)


if __name__ == '__main__':
    main()
