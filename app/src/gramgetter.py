# -*- coding: utf-8 -*-

from urllib2 import urlopen
#static class??

class GrammGetter:
    test="hui"

    def __init__(self):
        pass


    @staticmethod
    def getWikiGrammar(ruvoc,act,cnt,devoc):
        #ruvoc is russian voc, act = number of actual voc, cnt = total number of vocs to fill
        print("Voc("+str(act)+"/"+str(cnt)+" Attempt download info of "),

        try:
            print ruvoc
        except:
            print devoc

        htxt= GrammGetter.getHtmlText(ruvoc)
        if htxt==False:
            return "--NA-NoWiki ---","o"
        cat=  GrammGetter.getCategory(htxt)
        if cat=="o":
            return "--NA-Other----","o"

        tabletext=GrammGetter.getTableText(htxt,cat)
        cells=GrammGetter.getStringPart(tabletext,st="<td",en="/td>")


        if cat == "a" :  #adjectives -  mask,feminin,object,plural
            cl=[1,2,3,4]
            ##cut_cells=GrammGetter.getWikiAdjectiv(ruvoc,cells)
        if cat == "n" : # nomes - singular , plural !!!! (-1) is separator signal
            cl=[1,4,7,10,13,16,-1,2,5,8,11,14,17]
            ##cut_cells=GrammGetter.getWikiNomen(ruvoc,cells)
        if cat == "v" : # verbes - 6 cases + past + imperativ (sing,plur) !!!! (-1) is separator signal
            cl=[1,5,9,13,17,21,-1,2,7,19]
            ##cut_cells=GrammGetter.getWikiVerb(ruvoc,cells)
##        if cat == "o" :
##            cut_cells=GrammGetter.getWikiOther(ruvoc,cells)
        try:
            cut_cells=GrammGetter.getWikiCell(cells,cl)
        except:
            cut_cells="--Error in extracting cell--"

        return cut_cells,cat

#############sUBFUNKTIONEN++++++++++++++++++++++++++++++++++++++++++++



    @staticmethod
    def getHtmlText(ruvoc):   #returns whole text of wiki-html of vocabulary
        htxt=[] #array of the html text

        try: #check voc
            ruvoc=ruvoc.encode("utf-8")
        except:
            pass #ruvoc stays ruvoc

        try: #check url
            aResp = urlopen("http://ru.wiktionary.org/wiki/"+ruvoc)
        except:
            print("ERROR URL cannot be opened :http://ru.wiktionary.org/wiki/"+ruvoc)
            return False

        #convert response to array
        for line in aResp:
            htxt.append(line)
        aResp.close()

        return htxt


    @staticmethod
    def getCategory(htmltxt):      #searches wiki-html and returns category of voc (n,v,a,o)

        if ([x for x in htmltxt if 'Существительное' in x].__len__()!=0) and ([x for x in htmltxt if '>падеж<' in x].__len__()!=0):
                print("FOUND-is a nomen"),
                return "n"
        elif ([x for x in htmltxt if '>Я<' in x].__len__()!=0) and ([x for x in htmltxt if 'Глагол' in x].__len__()!=0) :
                print ("FOUND-is a verb"),
                return "v"
        elif ([x for x in htmltxt if 'прилагательное' in x].__len__()!=0) or ([x for x in htmltxt if 'Прилагательное' in x].__len__()!=0):
                print ("FOUND-is a adjectiv"),
                return "a"

        print("NOT FOUND - unknown")
        return "o"




    @staticmethod
    def getTableText(htmltxt,cat):
        #returns table text from htmltext
        #criteria: searchs for 2. or 3. table start. i.e.
        #signalword "<table" and saves all lines until next signalword '</table'

        ##print("searching cat="+cat)
        if cat=="n" or cat=="a":
            signal="падеж"
            #signal="мужской род" #possible for adject
        if cat=="v":
            #signal=">наст.<"
            signal=">Я<"  #possible for verb

        tabletext=""
        wiki_record=0

        for i,line in enumerate(htmltxt): #search startline
            if signal in line:
                wiki_record=1
                print("GO - start record at line "+str(i)),

            #record
            if(wiki_record==1):
                tabletext+=line

            #search end
            if ('</table' in line) and (wiki_record==1):
                wiki_record=0
                print("END recording")
                break

        return tabletext

    @staticmethod
    def getWikiCell(cells,cl):
        #structure see in tabletext_example.docx
        gr=""

        #METHODE ISI CHEEZY
        for nr in cl:
            if nr==-1:   # -1 is signalfor separator
                gr=gr+" // "
            else:
                if "<br />" in cells[nr]:                   #check for <br> -> replace by или
                    cells[nr]=cells[nr].replace("<br />"," или ")
                gr=gr+((cells[nr].split(">")[1])[:-1])+" , "  #filters words betwen ">  <" which are the targets

        if "\n" in gr:                                  #delete \n
            gr=gr.replace("\n"," ")
        if "&#160" in gr:
            gr=gr.replace("&#160","-")                  #if no single form exists ->single column is filled with --
        if "—,&#160" in gr:
            gr=gr.replace("—,&#160","-")

        return gr


################### HELP FUNCITONS ####################################

    @staticmethod
    def getStringPart(text,st,en): #returns stings inbetween two substring pairs
        fin=[]

        for l in text.split(en):
            if st in l:
                fin.append(l.split(st)[1])
        return fin







##    @staticmethod
##    def getWikiNomen(ruvoc,cells):
##        #structure see in tabletext_example.docx
##        print("final-nomen")
##        gr=""
##        cl=[1,4,7,10,13,16] #singular
##
##        #Strukur: 1.	" bgcolor="#FFFFFF">гита́ра<"
##        #struktur 13.	" bgcolor="#FFFFFF">гита́рой<br />гита́рою<"
##
##        #METHODE A
##        for nr in cl:
##            if "<br />" in cells[nr]:  #check for <br> -> replace by или
##                cells[nr]=cells[nr].replace("<br />"," или ")
##            gr=gr+((cells[nr].split(">")[1])[:-1])+","
##
##        if "\n" in gr:
##            gr=gr.replace("\n"," ")
##
##        return gr
##
##    @staticmethod
##    def getWikiAdjectiv(ruvoc,cells):
##        print("final-adj")
##        gr=""
##        cl=[1,2,3,4] #praesens
##
##        #METHODE A
##        for nr in cl:
##            if "<br />" in cells[nr]:  #check for <br> -> replace by или
##                cells[nr]=cells[nr].replace("<br />"," или ")
##            gr=gr+((cells[nr].split(">")[1])[:-1])+","
##
##        if "\n" in gr:
##            gr=gr.replace("\n"," ")
##
##        return gr
##
##
##    @staticmethod
##    def getWikiVerb(ruvoc,cells):
##        print("final-verb")
##        gr=""
##        cl=[1,5,9,13,17,21] #praesens
##
##        #METHODE A
##        for nr in cl:
##            if "<br />" in cells[nr]:  #check for <br> -> replace by или
##                cells[nr]=cells[nr].replace("<br />"," или ")
##            gr=gr+((cells[nr].split(">")[1])[:-1])+","
##
##        if "\n" in gr:
##            gr=gr.replace("\n"," ")
##
##        return gr
##
##
##    @staticmethod
##    def getWikiOther(ruvoc,cells):
##        print("final-oth")
##        print(cells[4])
##        return cells[1]

##    def getCategory(htmltxt):      #searches wiki-html and returns category of voc (n,v,a,o)
##        for i,line in enumerate(htmltxt):
##            if "Существительное" in line:
##                print("FOUND-is a nomen"),
##                return "n"
##            elif "Глагол" in line:
##                print ("FOUND-is a verb"),
##                return "v"
##            elif "прилагательное" in line:
##                print ("FOUND-is a adjectiv"),
##                return "a"
##            elif "Прилагательное" in line:
##                print ("FOUND-is a adjectiv"),
##                return "a"
##
##        print("NOT FOUND - unknown")
##        return "o"
