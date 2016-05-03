import sys
import json


def create_dictionary(sentiment):
    scores = {}
    for line in sentiment:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def parse_json(tweets):
    data = []
    for line in tweets:
        data.append(json.loads(line))
    return data


def calculate_sentiment(scores, data):
    for item in data:
        if 'text' not in item:
            continue
        text = item['text']
        tokens = text.split()
        sentiment = 0
        for token in tokens:
            if token in scores:
                sentiment += scores.get(token)
        print str(sentiment)


def main():
    scores = create_dictionary(open(sys.argv[1]))
    data = parse_json(open(sys.argv[2]))
    calculate_sentiment(scores, data)


if __name__ == '__main__':
    main()
