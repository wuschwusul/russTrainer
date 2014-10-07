# -*- coding: utf-8 -*-
import os,sys
import codecs

class Vocabel:
    de = ""   #german word
    ru = ""   #russian word
    cat = ""  #category (nomen,verb, adjektiv,other)
    ktx = ""  #kontext
    gmr = ""  #GrammarString

    isMp3 = False
    isWav = False


    def __init__(self,de,ru,cat=None,ktx=None,gmr=None):
        self.de=de
        self.ru=ru
        self.ktx=ktx
        self.gmr=gmr

        if cat==None:
            self.guessCat()
        else:
            self.cat=cat



    def guessCat():
        pass

    def mkMp3(self):
        pass
        self.isMp3=true

    def mkWav(self):
        pass

    def getMp3(self):
        pass

    def getWav(self):
        pass

    def getGmr(self):
        pass

    def update(self):
        pass
        #checks if mp3,wav exists and changes the boolean

##### ueberhaupt nötig==##
    def getDe(self):
        return self.de

    def getRu(self):
        return self.ru




