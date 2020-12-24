# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request 
#import urllib2



# change the url according to your own corename and query
inurl = 'http://3.19.76.58:8983/solr/DFR/select?fl=id%2Cscore&q=text_en%3AAleppo%20HQ%20OR%20text_ru%3AAleppo%20HQ%20OR%20text_de%3AAleppo%20HQ&rows=20'
outfn = '10.txt'


# change query id and IRModel name accordingly
qid = '010'
IRModel='default'
outf = open(outfn, 'a+')
#data = urllib2.urlopen(inurl)
# if you're using python 3, you should use
data = urllib.request.urlopen(inurl)

docs = json.load(data)['response']['docs']
# the ranking should start from 1 and increase
rank = 1
for doc in docs:
    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()
