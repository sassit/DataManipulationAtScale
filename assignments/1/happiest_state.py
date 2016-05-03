import sys
import json

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

def parse_json(tweet):
    data = []
    for line in tweet:
        data.append(json.loads(line))
    return data


def create_dictionary(sentiment):
    scores = {}
    for line in sentiment:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def calculate_sentiment(afin, data):
    scores = {}
    for item in data:
        if 'text' not in item or 'user' not in item:
            continue
        if 'place' not in item or item['place'] is None:
            continue
        place = item['place']
        if 'country_code' not in place and 'full_name' not in place:
            continue
        country_code = place['country_code']
        if country_code != 'US':
            continue
        state = place['full_name'][-2:]
        if state not in states:
            continue
        tokens = item['text'].encode('utf-8').split()
        sentiment = 0
        for token in tokens:
            if token in afin:
                sentiment += afin[token]
        if state in scores:
            scores[state] += sentiment
        else:
            scores[state] = sentiment
    return scores


def print_happiest(frequency):
    inverse = [(value, key) for key, value in frequency.items()]
    highest = max(inverse)[1]
    print highest


def main():
    affin = create_dictionary(open(sys.argv[1]))
    data = parse_json(open(sys.argv[2]))
    scores = calculate_sentiment(affin, data)
    print_happiest(scores)


if __name__ == '__main__':
    main()
