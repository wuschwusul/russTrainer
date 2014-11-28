# -*- coding: utf-8 -*-

from vocabel import Vocabel
from slawar import Slawar
from gramgetter import GrammGetter as gget

def main():

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("RussianTrainer")
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
            print("sv -> show vocabulary in Memory")
            print("ma  -> make ArchiveFile of Memory")
            print("la  -> load ArchiveFile to Memory")
            print("gm  -> get Grammar of missing")

            print("' '    -> exit")
            continue

        if cmd == "l":  #load database from excel
            sl.load()
            continue

        if cmd =="s":   #save database to excel
            sl.save()
            continue

        if cmd =="ma":  # make archiv
            sl.save(isArch=True)
            continue
        if cmd =="la":  # load archiv
            sl.load(isArch=True)
            continue

        if cmd =="sv":  # show Vocs content of slawar
            sl.show()
            continue

        if cmd =="gm": #get gramar of missing

            if sl.isEmpty():
                print("WARNING - No data loaded - type 'l' to load file ")
                continue

            sl.fillEmtpyGram()

            print("SAVING..."),
            sl.save()

            continue


        if cmd=="t": # TEST
            print("Test ")
            print(sl.vocs[138].ru)
            print(sl.vocs[138].gmr)
            wtf= (sl.vocs[138].gmr).split(";")[0]
            print wtf

            if wtf=="&#160":
                print("yeah")

            continue

        print("unknown command")






if __name__ == '__main__':
    main()
