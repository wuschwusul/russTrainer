# -*- coding: utf-8 -*-
from urllib2 import urlopen
import codecs


ruvoc="гитара"

aResp = urlopen("http://ru.wiktionary.org/wiki/гитара")

htxt=[]
for l in aResp:
    htxt.append(l)


for l in htxt:
    if "Существительное" in l:
        print("versuch1")
        print ("do is der scheiss")

for l in htxt:
    if "Существительное" in l:
        print("versuch2")
        print ("do is der scheiss")

##for i,line in enumerate(aResp):
##
##    if "Существительное" in line:
##        print("versuch1")
##        print ("do is der scheiss")
##        print(str(i))
##
##
##aResp.reset
##for i,line in enumerate(aResp):
##    if "Существительное" in line:
##        print("versuch2")
##        print ("do is der scheiss")
##        print(str(i))

##    @staticmethod
##    def cattest(text):
##        for i,line in enumerate(text):
##            if "Существительное" in line:
##                print ("des is a nomen")
##                return True
##            if "Глагол" in line:
##                print ("des is a verb")
##                return True
##            if "Прилагательное" in line:
##                print ("des is a adjektiv")
##                return True
##        return False
