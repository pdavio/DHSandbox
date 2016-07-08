#too use, type following 2 lines without the the #
#import bloom
#bloom.getCQLQuery()

import json, os, nltk, collections
from nltk.book import *
def allVerbs():
    #load all of bloom's verbs from json and return as list
    with open('types.json','r') as fp:
        return json.load(fp)


def perceptionVerbs():
    #load all of the canonical perception verbs from txt, split on whitespace to return list
    verbs = open('perception_verbs.txt').read()
    verbList = []
    verbList = verbs.split()
    return verbList

def bloomPerceptionVerbs():
    #produce a filtered list of Bloom's verbs that are only perception verbs
    av = allVerbs()
    filteredVerbs = av[:] #copy of all verbs
    #print("verbs before filter:" + str(len(filteredVerbs)))
    pv = perceptionVerbs()

    for v in av:
        if v not in pv:
            filteredVerbs.remove(v)
    #print("verbs after filter:" + str(len(filteredVerbs)))
    return filteredVerbs
 
def getCQLQuery():
    #produce the CQL statement we can cut and paste
    filteredVerbs = str(bloomPerceptionVerbs()).replace("'","").replace(",","|").replace(" ","")
    
    query = "Command = ['corpquery','ulys_2','(meet [lemma=\"" + str(filteredVerbs) + "\"] [word=\"Bloom\"] -5 5)']"
    with open("query.txt","w") as qt:
        qt.write(query)
    print("file written to: " + os.path.dirname(qt.name) + qt.name)
    return query


def getDist(tokens):
    #print(corpus.name)
    bpv = perceptionVerbs()
    fdist = nltk.FreqDist(tokens)
    dist = []
    for verb in bpv:
        dist.append(fdist[verb]/len(tokens) * 100)
    
    d = dict(zip(dist,bpv))
    od = collections.OrderedDict(sorted(d.items(),reverse=True))
    
    for key, value in od.items():
        print(value,":",round(key,3))

