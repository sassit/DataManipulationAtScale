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
        if 'text' not in item or 'lang' not in item:
            continue
        if item['lang'] is not 'en':
            continue
        text = item['text'].encode('utf-8')
        tokens = text.split()
        sentiment = 0
        count = 0
        nonscores = []
        for key in scores.keys():
            if key in text:
                count += 1;
                sentiment += scores[key]
        for token in tokens:
            if token not in scores:
                nonscores.append(token)
        if count is 0:
            continue
        for token in nonscores:
            scores[token] = sentiment / count
    return scores


def main():
    scores = create_dictionary(open(sys.argv[1]))
    data = parse_json(open(sys.argv[2]))
    scores = calculate_sentiment(scores, data)
    for key, value in scores.items():
        print key + " " + str(value)


if __name__ == '__main__':
    main()
