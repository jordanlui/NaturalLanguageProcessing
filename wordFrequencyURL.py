# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 22:22:10 2017

@author: Jordan
"""

import nltk
from nltk.corpus import stopwords
#nltk.download()
url = 'https://www.gutenberg.org/files/47960/47960-0.txt' # Romeo & Juliet
#url = 'http://php.net'
srCustom = ['The', 'etc.', 'Cf.','And','i.','ii.','iii.','iv.','v','3.','4.','1.','(=','To']
srCustom = [unicode(i,'utf-8') for i in srCustom]
from bs4 import BeautifulSoup
import urllib3
http = urllib3.PoolManager()
r = http.request('GET',url)
print r.status
html = r.data

#print (html)
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip=True)
#print text
tokens = [t for t in text.split()] # Tokens of data

#%% Frequency Plot
freq = nltk.FreqDist(tokens)
#for key,val in freq.items():
#	print key,val
freq.plot(20, cumulative=False)

#%% Stop word removal
clean_tokens = tokens[:]
sr = stopwords.words('english')
if srCustom:
	sr = sr + srCustom
for token in tokens:
	if token in sr:
		clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
#for key,val in freq.items():
#	print key,val
freq.plot(20, cumulative=False)