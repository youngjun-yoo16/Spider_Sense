from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
# blob = TextBlob("climate change is real", analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)
# blob = TextBlob("No, Climate Change Isn't 'Made Up", analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)
# blob = TextBlob("Humans are causing global warming", analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)
# blob = TextBlob("climate change is fake", analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)
import spacy
nlp = spacy.load("en_core_web_sm")
spacy.prefer_gpu()
from negspacy.negation import Negex
negex = Negex(nlp, language = "en_clinical_sensitive")

#ent_types=["PERSON","ORG"]
nlp.add_pipe(negex, last=True)
doc = nlp("The U.S. has reduced carbon dioxide emissions more than the countries who signed the Paris Climate Agreement")
for e in doc.ents:
	print(e.text, e._.negex)

#
# doc1 = nlp("sky is bad")
# doc2 = nlp("sky is good")
# print(doc1.similarity(doc2))
# blob = TextBlob("sky is bad", analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)
# blob = TextBlob("sky is good", analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)
# print(blob.sentiment)

# if seacrch = fact check claim
#fact check claim = false, then search = false, otherwise search = true

# try:
#     # For Python 3.0 and later
#     from urllib.request import urlopen
# except ImportError:
#     # Fall back to Python 2's urllib2
#     from urllib import urlopen
#
# import json
#
#
# url = ("https://factchecktools.googleapis.com/v1alpha1/claims:search?query=trump&key=AIzaSyC-PX-31ru9Y3O4RCKOwloQplLgJ2LTCl8")
#
# def get_jsonparsed_data(url):
#     response = urlopen(url)
#     data = response.read().decode("utf-8")
#     return json.loads(data)
#
#
#
# json = get_jsonparsed_data(url)
#
# info = []
# for claim in json["claims"]:
#     for line in claim["claimReview"]:
#         info.append(line['textualRating'])
#
#         # for thing in line['textualRating']:
#         #     print(thing)
#         # print(k['claimReview']['textualRating'])
#         # # #print(v['address']['addressLine2'])
#         # # print ('')
# falsec = 0
# truec = 0
# somethin = []
# false = ["False", "Falso", "Distorts the Facts", "Misleading", "Mostly False", "Pants on Fire"]
# true = ["True"]
# for item in info:
#     for val in false:
#         if(val in item):
#             falsec = falsec +1
#     for val2 in true:
#         if(val in item):
#             truec = truec + 1
# print(truec)
# print(falsec)
# str1 = "Humans are causing global warming"
# str2 = "No, Climate Change is Made Up"
# edits = [[x for x in range(len(str1) + 1)] for y in range(len(str2)+ 1)]
# for i in range(len(str2) + 1):
#     edits[i][0] = i
# for i in range(1, len(str2) + 1):
#     for j in range(1,  len(str1) + 1):
#         if str2[i-1] == str1[j-1]:
#             edits[i][j] = edits[i-1][j-1]
#         else:
#             edits[i][j] = 1 + min(edits[i-1][j-1], edits[i-1][j],
#                                      edits[i][j-1])
# print(edits[-1][-1])
#trump supports homesexuals
#approval