import os
import shutil

def organisefile():
   src_path=input("Provide the source path:->")
   for i in os.listdir(src_path):
       filename,typ=os.path.splitext(src_path+'\\'+str(i))
       if os.path.isfile(filename+typ):
          subfolder_name='newfolderpy'+str(typ[1:])
          if not os.path.exists(src_path+'\\'+subfolder_name):
             os.mkdir(src_path+'\\'+subfolder_name)
             shutil.move(filename+typ,src_path+'\\'+subfolder_name)
          else:
             shutil.move(filename+typ,src_path+'\\'+subfolder_name)
       else:
          pass


