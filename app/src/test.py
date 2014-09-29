import os,codecs

print ("Helleosdafds ")
for i in range (3):
	print i


abspath = os.path.abspath(__file__)

path_abs = os.path.abspath(__file__)
path_prj=os.path.join(os.path.dirname(__file__), "..",  "..")
path_db=os.path.join(os.path.dirname(__file__), "..",  "..", "database")
path_gui=os.path.join(os.path.dirname(__file__), "..",  "gui")
file_db=os.path.join(db_path,"ruvoc_db.txt")
file_db_bkup=os.path.join(db_path,"ruvoc_db_backup.txt")

print path_abs
print path_db
print path_gui
print path_prj


with codecs.open(file_db, "r", "utf-8") as f:
    for line in f:
        print line

