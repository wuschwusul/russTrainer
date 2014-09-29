# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Falcor
#
# Created:     15.03.2014
# Copyright:   (c) Falcor 2014
# Licence:     <your licence>
# Daten Struktur
# ru-Wort, de-Wort,
#-------------------------------------------------------------------------------




import os, sys, csv

import codecs # for file saving in utf-8- for cyrillic


import urllib2, urllib  # for reading wiktionary content


path_abs = os.path.abspath(__file__)
path_prj=os.path.join(os.path.dirname(__file__), "..",  "..")
path_db=os.path.join(os.path.dirname(__file__), "..",  "..", "database")
path_gui=os.path.join(os.path.dirname(__file__), "..",  "gui")
file_db=os.path.join(path_db,"ruvoc_db.txt")
file_db_bkup=os.path.join(path_db,"ruvoc_db_backup.txt")

from PyQt4 import QtCore, QtGui
sys.path.append(path_gui)
import russgui3


class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.ui = russgui3.Ui_Dialog()
        self.ui.setupUi(self)

        #--- INITIALISATION - DATA ---

        ##self.mydict={} # haupt-array
        self.db_checker=[]      #Checkliste used to check if added de_vocs are already in DB
        self.db_structure_count=3  #for the entry structure check -input structure has to be "devoc;ruvoc;type;context" or  "0xx;1xx;2xx;3xx"
        self.my_rowsize=18
        # VOC LIST RU DE

        #--- INITIALISATION - DB LIST  ---

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(4)
        self.headlist= QtCore.QStringList()
        self.headlist.append("De")
        self.headlist.append("Ru")
        self.ui.tableWidget.setHorizontalHeaderLabels(self.headlist)

        # TODO: updateDB_List // fill in data from db file
        ##self.ui.tableWidget.setItem(0,0,QtGui.QTableWidgetItem("..."))  # dummy filler
        self._update_db_list()

        #--- INITIALISATION - combo box  ---
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("Nomen")
        self.ui.comboBox.addItem("Verb")
        self.ui.comboBox.addItem("Adjektiv")
        self.ui.comboBox.addItem("Other")


        #--- INITIALISATION - GUI  BUTTONS  ---
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"),self.doOK)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"),self.doAB)

        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),self._add_manually)
        self.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"),self._add_from_file)
        self.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"),self._add_to_DB_List)
        self.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"),self._update_db_list)

        self.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"),self._delete_Entry)

        self.connect(self.ui.pushButton_6, QtCore.SIGNAL("clicked()"),self._make_DB_Backup)
        self.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"),self._load_DB_Backup)

        #self.ui.pushButton_7.setToolTip('testi') infofeld
####################### FUNCTIONS #########################


#++++++++++++++BUTTON FUNCTIONS +++++++++++++++++++++++++++

    # OK & Abort +++++++++++++++++++++++++++
    def doOK(self):
        print("ok")
        #TODO make backup of DB file
        self.accept()

    def doAB(self):
        print("abort")
        self.reject()




    def _add_manually(self): #++++++++BUTTON 1 +++++++++++++
        print ("start add manually")

        # GET TEXT
        de_voc=unicode(self.ui.lineEdit_3.displayText())
        ru_voc=unicode(self.ui.lineEdit_4.displayText())
        kntxt_voc=unicode(self.ui.lineEdit_6.displayText())

        #type_voc=unicode(self.ui.lineEdit_5.displayText())
        type_voc=str(self.ui.comboBox.currentText())[0].lower()


        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.lineEdit_6.clear()

        # GET TYPE
        # ...in progress

        # WRITE TO TextEdit
        self.ui.textEdit.append(de_voc+";"+ru_voc+";"+type_voc+";"+kntxt_voc)



    def _add_from_file(self): #++++++++BUTTON 2 +++++++++++++
        print ("here should be adding from file")
        # file name
        inf_name=unicode(self.ui.lineEdit.displayText())

        # GET FILE DATA to Array
        with codecs.open(inf_name, "r", "utf-8") as f:
            newvocs= f.readlines()

        # WRITE TO TextEdit (input list)
        print newvocs
        for i in newvocs:
            j=i.split(";")
            print j
            j[j.__len__()-1]=j[j.__len__()-1][:-2] #:-2 um \n im letzten element wegzuschneiden
            print j
            self.ui.textEdit.append(j[0]+";"+j[1]+";"+j[2]+";"+j[3])



    def _add_to_DB_List(self): #+++++++++BUTTON 3 +++++++++
        print ("start adding to DB list")

        #---GET INPUTLIST from textEdit
        inputlist=  unicode(self.ui.textEdit.toPlainText()).split("\n")  # plain text kommt als eine-zeile mit "\n" daher wirds gesplittet


        #---CHECK LIST EMPTY  - return false
        try:
            print inputlist[0][0]
        except:
            print("empty list found")
            self.ui.textEdit_2.append("Empty Input List")
            self.ui.textEdit.clear()
            return False

        #---CHECK wrong INPUTSTRUCTURE - delete from inputlist

        del_list=[]  #list of entries to delete
        for j,entry in enumerate(inputlist):
            try:
                entry.split(";")[self.db_structure_count] # check if array[3] exists - if not - false structure
            except:
                print("false input structure found in inputlist at "+str(j))
                self.ui.textEdit_2.append("false input structure found in inputlist at "+str(j))
                del_list.append(j)

        del_list.sort(reverse=True)  # order reversed to decreasing -> so each wrong entry can be deleted from top down
        for entry in del_list:
            inputlist.pop(entry)

        #---DELETE DOUBELE -  get aleardy existing entries in DB---

        deletelist=[] # list of entries in inputlist to be deleted

        for line in inputlist:                  #search db_checker for double entry
            entry=line.split(";")
            print("suche "+entry[0])
            if entry[0] in self.db_checker:
                deletelist.append(line)


        for entry in deletelist:                #deleting existing entries from inputlist
            print("removing existing "+entry)
            self.ui.textEdit_2.append(entry.split(";")[0]+"...exists in DB, not added")
            inputlist.remove(entry)


        #---CLEAR inputlist ----
        self.ui.textEdit.clear()


        #---rus_voc und type nehmen udn info holen
        for j,entry in enumerate(inputlist):                                         #für jeden Eintrag "hören;слышать;v;Verb"
            info=self._getWiki(entry.split(";")[1],entry.split(";")[2])     #splitten und ruvoc (pos 1) und type (pos 2) uebermitteln
            inputlist[j]=inputlist[j]+u";"+info                              # merge input words and info


        #---inputlist in DB einfügen - WENN nicht schon vorhanden
        self.add_to_DB(inputlist)

        #---update DB List----
        self._update_db_list()





    def add_to_DB(self,inputlist):      # adds a line "de;ru;type;kontxt;info" into DBfile
        print("in add to db")

        #---write remaining inputlist into DB
        try:
            with codecs.open(file_db, "a", "utf-8") as f:     #open file to write
                for j,entry in enumerate(inputlist):
                    f.write("\r\n"+entry)
        except:
            self.ui.textEdit_2.append("Adding to DB NOT successfull")

        self.ui.textEdit_2.append("Adding to DB successfull")




    def _update_db_list(self):
        print ("Start update dict list")

        #---Empty checklist---
        self.db_checker=[]

        #---TODO empty list ----
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderLabels(self.headlist)
        self.ui.tableWidget.setRowCount(2) #preset

        #---Fill from file--
        num_lines = sum(1 for line in open(file_db))  #coutn entries in file
        print("Entries found in file: "+str(num_lines))

        self.ui.tableWidget.setRowCount(num_lines)                  # rearrange row number of tablewidget
        rwcntr=0
        with codecs.open(file_db, "r", "utf-8") as f:
            for line in f:
                #print line
                try:
                    linearr=line.split(";")
                    self.ui.tableWidget.setRowHeight(rwcntr,self.my_rowsize) #set size of row in tablewidget
                    self.ui.tableWidget.setItem(rwcntr,0,QtGui.QTableWidgetItem(linearr[0]))  # fillin german
                    self.ui.tableWidget.setItem(rwcntr,1,QtGui.QTableWidgetItem(linearr[1]))  # fillin russian

                except:
                    print("ERROR at "+line+" in row :"+str(rwcntr))
                    self.ui.tableWidget.setItem(rwcntr,0,QtGui.QTableWidgetItem("n.a"))  # fillin german
                    self.ui.tableWidget.setItem(rwcntr,1,QtGui.QTableWidgetItem("n.a"))  # fillin russian

                rwcntr+=1

                self.db_checker.append(linearr[0])                              # fill Checklist -
        print("new checklist:")
        print self.db_checker
        print self.db_checker[0]
        print self.db_checker[1]



    def _getWiki(self,ru_voc,voctype):
    # input : russ_vocabel und type (v n a o)
    #  aufruf netz-suchfunktion
    #  return info als string "я знаю, ты знаешь..." mit Beistrich"," als trennzeichen



        try:
            if voctype=="v":
                print("wikiSearch (v) : "+ru_voc)
                print("wikiSearch successful")
                return self._getWikiVerb(ru_voc)

            elif voctype=="n":
                print("wikiSearch (n) : "+ru_voc)
                print("wikiSearch successful")
                return self._getWikiNomen(ru_voc)

            elif voctype=="a":
                print("wikiSearch (a) : "+ru_voc)
                print("wikiSearch successful")
                return self._getWikiAdjectiv(ru_voc)

            elif voctype=="o":
                print("other type - no wiki for "+ru_voc)
                return "n.a."

        except:
            print("Wiki Info not found")
            self.ui.textEdit_2.append("Error getting wiki info of "+ru_voc)
            return u"-"





    def _getWikiVerb(self,ru_voc):    # in знать  OUT знаю знаешь ....
        #---------------------------
        # Method:
        # 1) copy text between  "title="именительный" .... "</table>" >>into>> tabletxt ; this is text of the wiki table.
        #    Each cell of Table has structure:
        #     <td bgcolor= ....</td><td bgcolor= ....</td><td bgcolor= ....</td><td bgcolor= ....</td>
        #
        # 2) split string by ("<\td>")
        #    --> Array of each cell starting with
        #       "<td...."#FFFFFF">,
        #       "<td..."#FFFFFF">гита́рам",
        #       "<td..."#FFFFFF">гита́рам",
        #       "<td..."#FFFFFF">гита́рам"....
        #
        # 3) in each array split by ">" and take the entry at pos 1
        #   --> array of vocabulary appended in
        #   variable: voc_info
        #---------------------------

        # +++++++++++ GET TABLE INFO - VERB ++++++++++++++++++++++++

        tabletxt=""
        wiki_record=0

        #---get full html text ---
        aResp = urllib2.urlopen("http://ru.wiktionary.org/wiki/"+ru_voc.encode("utf-8"))

        for line in aResp:

            if 'title="я">Я</a></td>'.decode('utf-8') in line.decode('utf-8'):    #beginne lesen bei 'title="я">Я</a></td>
                print("start recording")
                wiki_record=1
            if ('</table' in line.decode('utf-8')) and (wiki_record==1):    #beginne lesen bei 'title="я">Я</a></td>
                print("end recording")
                wiki_record=0
            if (wiki_record==1):
                tabletxt+=line.decode('utf-8')


        # ++++++++++++++++++++++++++ END +++++++++++++++++++++++++++

        #---selecting 6 lines(cells) from selected Area--- eg <td align="left">слы́шим

        celltext=tabletxt.split("</td>")  # splits the selected area into it's cells (\td) is the end of each cell.
                                        #since there are 4 columsn, and we want only the second column (=1) and rows 1-6
                                        #we filter for them:
        voc_info=[]
        max_rows=6
        selected_column=1

        for j,line in enumerate(celltext):
            if j%4==selected_column and j<(max_rows)*4:         #select lines to respective table-cell (row0-5 and column 1)
                #lines are in form of  eg <td align="left">слы́шим --> splitting
                voc_info.append(line.split(">")[1])                           #---extract the vocabulary from the lines ---  eg <td align="left">слы́шим --> слы́шим

        #---convert array into a string
        wiki_info=u''
        for voc in voc_info:
            wiki_info+=unicode(voc)+","

        return wiki_info[:-1]               #returns single line of vocs - eg "слы́шу,слы́шишь,слы́шит,слы́шим,слы́шите,слы́шат"




    def _getWikiNomen(self,ru_voc):

        tabletxt=""                                                                 # hmtl text of the decliantion table
        wiki_record=0                                                               # is 0 before the singal word, is 1 after the signal word, and is 0 again after the second signal word.

        #---get full html text ---
        aResp = urllib2.urlopen("http://ru.wiktionary.org/wiki/"+ru_voc.encode("utf-8"))

        #--- get html text  of the webpage area ---
        for line in aResp:
            if ('именительный'.decode('utf-8')) in line.decode('utf-8'):    #start recording lines at именительный - occurs only once
                wiki_record=1
            if (wiki_record==1) and (('</table') in (line.decode('utf-8'))):      # ende lesen bei <\table
                print("end recrd")
                wiki_record=0
            if (wiki_record==1):
                tabletxt+=line.decode('utf-8')
        #----------------------------------end --------------------------------------

        #--- filter vocs from text
        celltext=tabletxt.split("</td>")   # splitting the text into cell elements (they area separated by <td> ..<\td>

        voc_info=[]  # araay of vocs
        max_rows=6  # length of selected rows
        wiki_columns=3  #columns of the original wiki page

        # +++ get singular nomen vocs +++
        selected_column=1  # number of selected column
        for j,line in enumerate(celltext):                                      # each line <td bgcolor="#FFFFFF">гита́рами
            if j%wiki_columns==selected_column and j<(max_rows)*wiki_columns:   # take only selected column's entries

                # IF for special case of two entries in a cell
                if line.split(">")[1][-5:]=="<br /":                                                        # if there is "<br /" then two entries are in one cell - then take both entries; else only one
                    voc_info.append(line.split(">")[1]+"..или...".decode('utf-8')+line.split(">")[2][1:])  #[1:] because first character is "\n"
                else:
                    voc_info.append(line.split(">")[1])                                                     # structure of lines <td bgcolor="#FFFFFF">музе́й  --> split(">")[1] =музе́й


        # +++ get plural nomen vocs +++
        selected_column=2 # number of selected column
        voc_info.append("...plural...")

        for j,line in enumerate(celltext):
            if j%wiki_columns==selected_column and j<(max_rows)*wiki_columns:
                #print line.split(">")[1]
                voc_info.append(line.split(">")[1])     # structure of lines <td bgcolor="#FFFFFF">музе́й


        wiki_info=u''   # single line of vocs
        for voc in voc_info:
            wiki_info+=unicode(voc)+","

        return wiki_info[:-1]   #returns single line of vocs singular and plural
                                #eg "музе́й,музе́я,музе́ю,музе́й,музе́ем,музе́е,музе́и,музе́ев,музе́ям,музе́и,музе́ями,музе́ях"


    def _getWikiAdjectiv(self,ru_voc):

        tabletxt=""
        wiki_record=0

        #---get full html text ---
        aResp = urllib2.urlopen("http://ru.wiktionary.org/wiki/"+ru_voc.encode("utf-8"))

        #--- get html text  of the webpage area ---
        for line in aResp:
            if ('именительный'.decode('utf-8')) in line.decode('utf-8'):    #start recording lines at именительный - occurs only once
                wiki_record=1
            if (wiki_record==1) and (('</table') in (line.decode('utf-8'))):      # ende lesen bei <\table
                print("end recrd")
                wiki_record=0
            if (wiki_record==1):
                tabletxt+=line.decode('utf-8')
        #----------------------------------end --------------------------------------

        # TABLE STRUCTURE
        celltext=tabletxt.split("</td>")
        voc_info=[]

        # adjective tables are irregular- therefore the selected cells are manually inserted
        for j,line in enumerate(celltext):
            if j in [1,2,3,4]:                      #1 -4 are the 1case male,neurum,female,plural
                voc_info.append(line.split(">")[1])

        wiki_info=u''
        for voc in voc_info:
            wiki_info+=unicode(voc)+","

        return wiki_info[:-1]  # return without the last ","



    def _delete_Entry(self):
        print("starting deleting from list")
        # get marked entry
        delrow=self.ui.tableWidget.currentItem().row()

        # delete from db
        lines = open(file_db).readlines()
        lines.pop(delrow)
        newlines=lines
        open(file_db, 'w').writelines(lines)

        self._update_db_list()

        # update db_list

    def _make_DB_Backup(self): #create a backup file
        print("start making backupfile")
        lines = open(file_db).readlines()
        open(file_db_bkup, 'w').writelines(lines)


    def _load_DB_Backup(self):  #get backup content and update list
        print("start load backupfile")
        lines = open(file_db_bkup).readlines()
        open(file_db, 'w').writelines(lines)
        self._update_db_list()


def main():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()

    print sys.exit(app.exec_())


if __name__ == "__main__":
    main()


