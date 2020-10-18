try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib import urlopen


import json


url = ("https://factchecktools.googleapis.com/v1alpha1/claims:search?query=trump&key=AIzaSyC-PX-31ru9Y3O4RCKOwloQplLgJ2LTCl8")

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

info = []
json = get_jsonparsed_data(url)
for claim in json["claims"]:
    for line in claim["claimReview"]:
        info.append(line['textualRating'])

        # for thing in line['textualRating']:
        #     print(thing)
        # print(k['claimReview']['textualRating'])
        # # #print(v['address']['addressLine2'])
        # # print ('')
falsec = 0
truec = 0
print(info)
somethin = []
false = ["False", "Falso", "Distorts the Facts", "Misleading", "Mostly False", "Pants on Fire"]
true = ["True"]