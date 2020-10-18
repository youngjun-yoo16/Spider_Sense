try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib import urlopen


import json


flatearth = " https://factchecktools.googleapis.com/v1alpha1/claims:search?languageCode=en-US&pageSize=3&query=the%20earth%20is%20flat&key=AIzaSyC-PX-31ru9Y3O4RCKOwloQplLgJ2LTCl8"

def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def get_json_data(json):
    for claim in json["claims"]:
        claimu = claim['text']
        claiment = claim['claimant']
        for line in claim["claimReview"]:
            title = line['title']
            j_url = line['url']
            rating = line['textualRating']
    return claimu, claiment, title, j_url, rating



def main(url_json):
    json = get_jsonparsed_data(url_json)
    return get_json_data(json)



claim = main(flatearth)
for index, tuple in enumerate(claim):
	print(claim[index])


#
#         # for thing in line['textualRating']:
#         #     print(thing)
#         # print(k['claimReview']['textualRating'])
#         # # #print(v['address']['addressLine2'])
#         # # print ('')
# falsec = 0
# truec = 0
# #print(info)
# somethin = []
# false = ["False", "Falso", "Distorts the Facts", "Misleading", "Mostly False", "Pants on Fire"]
# true = ["True"]