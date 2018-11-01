#!/usr/bin/env python


#autor:ksalgut
#data:20180326
#wersja 1.0
#opis: 


import sys
from os import listdir
from os.path import isfile, join
import sys
import os
import numpy as np
import re
from datetime import datetime 
import csv

def checkpath (mypath):
     """
     sprawdza czy istnieje sciezka 
     zwraca:
     TRUE - jeśli istnieje
     FALSE - je
     """
     return os.path.isdir(mypath)
     
     
     
def checkfile (file):
    """
    """
    return os.path.isfile(file)
    
def make_dir (namedir):
   """
   
   """
   if not os.path.exists(namedir):
    os.makedirs(namedir)
    print("Note: Directory made %s" %namedir)
   else:
    print ("TypeError: Directory is exist %s" % namedir)
    sys.exit()  
    
def list_file (mypath):
    """
    
    """
    tab=[]
    for root, dirs, files in os.walk(mypath):
       if checkpath(root)==True:
        for file in files: # 
          path=os.path.join(root, file)
          tab.append(path)
          
    return tab      

def parse_log (tabfile, pattern='^ERROR|WARNING'):
    """
    tabfile - zwaiera liste plikow (ktore istnieja w systemie operacyjnym - nie sa sprawdzane)
    patter wzozec ktorego szukamy w plikach wejsciowych
    na sztywno zaszyty jest parametr selekcjonujacy pliki (*.log - konczy sie na '.log')
    """
    tab=[]
    for file in tabfile:
       m = re.compile('.log$')
       if m.search(file):
         #print (file)
         ifile = open(file, 'r')
         for line in ifile:
            temp_tab=[]
            mm=re.compile(pattern, re.MULTILINE)
            if mm.search(line):
               temp_tab.append(file)
               temp_tab.append(line)
               tab.append(temp_tab)
               #temp_tab.clear()              
         ifile.close()          
    return tab

def import_matrix_to_csv(tablog, file, force='Y'):
    """
    """
    if checkfile(file)==True and force !='Y':
      print("Note: File is exist %s and options force not chosen" %file)
      print("Note: Exit")
      sys.exit() 
    else:  
        with open(file, 'w') as outcsv:
          writer = csv.writer(outcsv, delimiter=';', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
          writer.writerow(['FILE', 'INFO'])
          for item in tablog:
            writer.writerow([item[0], item[1]])
    
    
def main():
    #czas start
    start_time = datetime.now()
    tab=[]
    tab_=[]
    #param_1= sys.argv[1]
    param_1="/Users/konrad/Documents"
    namedir=('{}'.format(datetime.now()))
    if checkpath(param_1)==False:
        print("TypeError: Path does not exist - %s" % param_1 )
        sys.exit() 
    fullnamedir=param_1+"/"+namedir
    tab=list_file (param_1)
    #rprint(np.matrix(tab))
   
    #twrzymy katalog
    #make_dir(fullnamedir) 
    
    tab_=parse_log(tab)
    print(np.matrix(tab_))
    print(len(tab_))
    import_matrix_to_csv(tab_,"/Users/konrad/Documents/wynik.csv")
    #ile trwalo
    time_elapsed = datetime.now() - start_time 

    print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))
    
if __name__ == "__main__":
    main()    
    
