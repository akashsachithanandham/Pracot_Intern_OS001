import os 
import sys
from tqdm import tqdm 
import time 
from progress.bar import IncrementalBar

if(len(sys.argv)==1):
    searchQuery = input("Enter the Search Query:")
    searchQuery = searchQuery.lower()
    logFile = input("Enter the log file:")
    f = open(logFile, "a")
    wikiLink = "https://en.wikipedia.org/wiki/" + searchQuery + '\n'
    #f.write(wikiLink +'\n')
    Length = len(wikiLink )
    bar = IncrementalBar('Progress', max = Length)
    for i in wikiLink:
        f.write(i)
        bar.next()
        time.sleep(0.05)
    bar.finish()
  
    
      
    print("Complete.") 
    print("The Wiki link is successfully uploaded inside the log file!!")
    f.close()
else:
    searchQuery = sys.argv[1]
    searchQuery = searchQuery.lower()
    logFile = sys.argv[2]
    f = open(logFile, "a")
    wikiLink = "https://en.wikipedia.org/wiki/" + searchQuery + '\n'
    #f.write(wikiLink +'\n')
    Length = len(wikiLink )
    bar = IncrementalBar('Progress', max = Length)
    for i in wikiLink:
        f.write(i)
        bar.next()
        time.sleep(0.05)
    bar.finish()
  
      
    print("Complete.") 
    print("The Wiki link is successfully uploaded inside the log file!!")
    f.close()