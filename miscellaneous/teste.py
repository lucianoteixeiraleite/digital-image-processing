# Reads all images from a directory and inserts them into a list.
# Then separate the repeated photos, creating two lists,
# one with unique images and the other with repeated images

# legge tutte le immagini da una directory e le inserisce in un elenco.
# quindi separare le foto ripetute, creando due elenchi,
# uno con immagini uniche e l'altro con immagini ripetute

import os, sys
from stat import *
import hash
import pandas as pd


def walktree(top,list_files):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''
    global tot
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.lstat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname,list_files)
            
        elif S_ISREG(mode):
            # It's a file, call the callback function
            _ , extension = os.path.splitext(f)
            if extension.upper() == '.JPG':
                tot += 1
                if (tot % 1000) == 0:
                    print(tot)
                tupla=(pathname,hash.hashfile(pathname))
                list_files.append(tupla)
                
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)
            
    return list_files
   
   
def createDataframes(list_files):
    list_files = walktree("D:/luciano/Familia/fotos/todas/", list_files)
    list_files.sort(key=lambda x: x[1], reverse=True)
    
    df = pd.DataFrame(list_files, columns=['files', 'hash'])
    dfDuplicate =  df.duplicated(subset=['hash'],keep = "first")
    df = pd.concat([df,dfDuplicate], axis=1)
    df.columns = ['files', 'hash', 'duplicated']
    
    return df   

if __name__ == '__main__':
    tot = 0
    list_files = []
    df = createDataframes(list_files)
    dfnoRepeat = df.query('duplicated==False')
    dfRepeat   = df.query('duplicated==True ')
    print('###############     df     ###########################')
    print(df.shape)
    print('###############  dfnoRepeat ##########################')
    print(dfnoRepeat.head(100))
    print('###############    Repeat   ##########################')
    print(dfRepeat.head(100))
     
    
    
  
   
    
    
    