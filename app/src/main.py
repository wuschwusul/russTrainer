# -*- coding: utf-8 -*-

from vocabel import Vocabel
from slawar import Slawar
from gramgetter import GrammGetter as gget

def main():

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("START RussianTrainer")
    print("This Programm manages a set of german-Russian VocabularyDouples in an Excel, ")
    print("adds grammatical declinations from internet sources (wiktionary)")
    print("as well as generates Mp3&Wav Files from each entry (german,russian,declination)")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("for CommandLine Help press 'h' ")

    sl = Slawar()

    while True:
        kIn = raw_input("\nCommand: ")
        if len(kIn) == 0:
            break
        cmd=kIn


        if cmd == "h":
            print("l  -> load standard database to Memory")
            print("s  -> save Memory to database")
            print("a  -> add Vocabulary to Memory")
            print("d  -> delete Vocabulary from Memory")
            print("ma  -> make ArchiveFile of Memory")
            print("la  -> load ArchiveFile to Memory")
            print("gg  -> get Grammar (not implemented")
            print("' '    -> exit")

        if cmd == "l":  #load database from excel
            sl.load()
        if cmd =="s":   #save database to excel
            sl.save()
##        if cmd == "a":  #add entry in slawar
##            sl.add()
##        if cmd =="d":   #delete entry in slawar
##            sl.delete()
        if cmd =="ma":  # make archiv
            sl.save(isArch=True)
        if cmd =="la":  # load archiv
            sl.load(isArch=True)

        if cmd =="sv":  # show Vocs content of slawar
            sl.show()

        if cmd =="gm": #get gramar of missing
            print gget.test
            gget.getWikiGrammar("знать")






if __name__ == '__main__':
    main()
