# -*- coding: utf-8 -*-

from urllib2 import urlopen
#static class??

class GrammGetter:
    #wikitext=0
    ruvoc=None
    test="hui"

    def __init__(self):
        pass


    @staticmethod
    def getWikiGrammar(ruvoc):
        htxt= GrammGetter.getHtmlText(ruvoc)
        cat=  GrammGetter.getCategory(htxt)
        tabletext=GrammGetter.getTableText(htxt)
        cells=GrammGetter.getStringPart(tabletext,st="<td",en="/td>")

        #signalwort fuer Tabelle: падеж

        if cat == "a" :
            GrammGetter.getWikiAdjectiv(ruvoc,cells)
        if cat == "n" :
            GrammGetter.getWikiNomen(ruvoc,cells)
        if cat == "v" :
            GrammGetter.getWikiVerb(ruvoc,cells)
        if cat == "o" :
            GrammGetter.getWikiOther(ruvoc,cells)


#############sUBFUNKTIONEN++++++++++++



    @staticmethod
    def getHtmlText(ruvoc):   #returns whole text of wiki-html
##        aResp = urlopen("http://ru.wiktionary.org/wiki/"+ruvoc)
##        return aResp

        #offlineversion for TESTING
        #htmltxt= open("K:\\ppy_projekte\\prj_russTrainerSimpel\\app\\testhtmls\\dom.htm")
        #htmltxt= open("K:\\ppy_projekte\\prj_russTrainerSimpel\\app\\testhtmls\\malenki.htm")
        htmltxt= open("K:\\ppy_projekte\\prj_russTrainerSimpel\\app\\testhtmls\\snat.htm")
        return htmltxt


    @staticmethod
    def getCategory(htmltxt):      #returns category of voc (n,v,a,o)

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
        print(cells[4])

    @staticmethod
    def getWikiAdjectiv(ruvoc,cells):
        print("final-adj")
        print(cells[4])

    @staticmethod
    def getWikiVerb(ruvoc,cells):
        print("final-verb")
        print(cells[4])

    @staticmethod
    def getWikiOther(ruvoc,cells):
        print("final-oth")
        print(cells[4])



    @staticmethod
    def getTableText(htmltxt): #returns table text from htmltext
        tabletext=""
        wiki_record=0

        for i,line in enumerate(htmltxt):
            #search start
            if "падеж</a>" in line:
                print("FOUND - start record at line "+str(i))
                wiki_record=1

            #record
            if(wiki_record==1):
                tabletext+=line
            #search end
            if ('</table' in line) and (wiki_record==1):
                wiki_record=0
                print("END recording")

        return tabletext


    @staticmethod
    def getStringPart(text,st,en): #returns stings inbetween two substring pairs
        fin=[]

        for l in text.split(en):
            if st in l:
                fin.append(l.split(st)[1])
        return fin




