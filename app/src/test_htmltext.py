# -*- coding: utf-8 -*-
from urllib2 import urlopen

ruvoc="от ... До"
aResp = urlopen("http://ru.wiktionary.org/wiki/"+ruvoc)
htxt=[]

for line in aResp:
    htxt.append(line)
aResp.close()

if ([x for x in htxt if 'Существительное' in x].__len__()!=0) and ([x for x in htxt if '>падеж<' in x].__len__()!=0):
    print("is nomen")

    print([x for x in htxt if 'Существительное' in x].__len__())
    print ([x for x in htxt if '>падеж<' in x].__len__())
    print([x for x in htxt if 'Существительное' in x].__len__()!=0)
    print ([x for x in htxt if '>падеж<' in x].__len__()!=0)



elif ([x for x in htxt if '>Я<' in x].__len__()!=0):
        print ("FOUND-is a verb")


elif ([x for x in htxt if 'прилагательное' in x].__len__()!=0) or ([x for x in htxt if 'Прилагательное' in x].__len__()!=0):
        print ("FOUND-is a adjectiv")


if True and True:
    print("yea")
