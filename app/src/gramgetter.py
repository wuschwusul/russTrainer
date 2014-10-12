# -*- coding: utf-8 -*-

from urllib2 import urlopen
#static class??

class GrammGetter:
    test="hui"

    def __init__(self):
        pass


    @staticmethod
    def getWikiGrammar(ruvoc):
        htxt= GrammGetter.getHtmlText(ruvoc)
        cat=  GrammGetter.getCategory(htxt)
        tabletext=GrammGetter.getTableText(htxt,cat)
        print("laenge Table: "+str(len(tabletext)))
        cells=GrammGetter.getStringPart(tabletext,st="<td",en="/td>")


        if cat == "a" :
            cut_cells=GrammGetter.getWikiAdjectiv(ruvoc,cells)
        if cat == "n" :
            cut_cells=GrammGetter.getWikiNomen(ruvoc,cells)
        if cat == "v" :
            cut_cells=GrammGetter.getWikiVerb(ruvoc,cells)
        if cat == "o" :
            cut_cells=GrammGetter.getWikiOther(ruvoc,cells)

        return cut_cells

#############sUBFUNKTIONEN++++++++++++



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
        for i,line in enumerate(htmltxt):
            if "Существительное" in line:
                print("FOUND-is a nomen")
                return "n"
            elif "Глагол" in line:
                print ("FOUND-is a verb")
                return "v"
            elif "Прилагательное" in line:
                print ("FOUND-is a adjectiv")
                return "a"
        print("NOT FOUND - unknown")
        return "o"



    @staticmethod
    def getWikiNomen(ruvoc,cells):
        print("final-nomen")
        gr=""
        cl=[1,4,7,10,13,16] #singular

        #Strukur: 1.	" bgcolor="#FFFFFF">гита́ра<"
        #struktur 13.	" bgcolor="#FFFFFF">гита́рой<br />гита́рою<"

        for nr in cl:
            if "<br />" in cells[nr]:  #check for <br> -> replace by или
                cells[nr]=cells[nr].replace("<br />"," или ")
            gr=gr+((cells[nr].split(">")[1])[:-1])+","

        if "\n" in gr:
            gr=gr.replace("\n"," ")

        return gr

    @staticmethod
    def getWikiAdjectiv(ruvoc,cells):
        print("final-adj")
        print(cells[4])
        return "test"

    @staticmethod
    def getWikiVerb(ruvoc,cells):
        print("final-verb")
        print(cells[4])
        return "test"

    @staticmethod
    def getWikiOther(ruvoc,cells):
        print("final-oth")
        print(cells[4])
        return cells[1]



    @staticmethod
    def getTableText(htmltxt,cat):
        #returns table text from htmltext
        #criteria: searchs for 2. or 3. table start. i.e.
        #signalword "<table" and saves all lines until next signalword '</table'

        print("searching cat="+cat)
        if cat=="n" or cat=="a":
            signal="падеж"
        if cat=="v":
            signal=">наст.<"

##        print(type(signal))
##        print("signal is "+signal)

        tabletext=""
        wiki_record=0

        for i,line in enumerate(htmltxt): #search startline
            if signal in line:
                wiki_record=1
                print("FOUND - start record at line "+str(i))

            #record
            if(wiki_record==1):
                tabletext+=line

            #search end
            if ('</table' in line) and (wiki_record==1):
                wiki_record=0
                print("END recording")
                break

##        print tabletext
        return tabletext


    @staticmethod
    def getStringPart(text,st,en): #returns stings inbetween two substring pairs
        fin=[]

        for l in text.split(en):
            if st in l:
                fin.append(l.split(st)[1])
        return fin




