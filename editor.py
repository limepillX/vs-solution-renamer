import os
from os import walk
import chardet
import codecs

class Renamer:
    oldName = str()
    oldName_1 = str()
    newName = str()
    url = str()
    files = list()
    allfiles = list()
    directories = list()
    cppFiles = list()
    changecounter = int()
    
    
    def __init__(self, url, newName):
        self.newName = newName
        self.url = url
        self.oldName = url.split("\\")[-1]
        self.oldName_1 = self.oldName.replace('_', '')
        
        print(self.oldName_1)
        
        for root, dirs, files in os.walk(url):
            for file in files:
                if ".ico" not in file:
                    self.allfiles.append(os.path.join(root, file))
                if self.oldName in file:
                    self.files.append(os.path.join(root, file))
            for dir in dirs:
                if self.oldName in dir.split("\\")[-1]:
                    self.directories.append(os.path.join(root, dir))
        self.directories = list(reversed(self.directories))
    
    def renameFiles(self):
        for file in self.files:
            newname = file[:-len(file.split("\\")[-1])] + file.split("\\")[-1].replace(self.oldName, self.newName)
            os.rename(file, newname)
                    
    def changeFiles(self):
        for file in self.allfiles:
            try:
                bytes = min(32, os.path.getsize(file))
                raw = open(file, 'rb').read(bytes)
                if raw.startswith(codecs.BOM_UTF8):
                    encoding = 'utf-8-sig'
                else:
                    result = chardet.detect(raw)
                    encoding = result['encoding']
                    
                try:
                    f = open(file, 'r', encoding=encoding)
                    text = f.read()
                    f.close()
                except (UnicodeDecodeError, PermissionError):
                    try:
                        f = open(file, 'r', encoding='cp1252')
                        encoding = 'cp1252'
                        text = f.read()
                        f.close()
                    except UnicodeDecodeError:
                        continue
                
                while text.find(self.oldName) != -1:
                    text = text.replace(self.oldName, self.newName, 1)
                    self.changecounter += 1
            except:
                continue     
            try:
                f = open(file, 'w', encoding=encoding)
                f.write(text)
                print(f.name + " has changed")
                f.close()
            except:
                continue
            
    def start(self):
        self.changeFiles()
        self.renameFiles()
        self.printCatalog()
            
           
                
                        
    def printCatalog(self):
        print(f"{len(self.files)} файлов было переименованно" + f"\n{self.changecounter} названий было переписано")
        return f"{len(self.files)} файлов было переименованно" + f"\n{self.changecounter} названий было переписано"
        
        
if __name__ == "__main__":
    url = "C:\\Users\\justacold\\Desktop\\VikaButskevichLab8"
    newname = 'Yakovenko_8'
    project = Renamer(url, newname)
    
    project.start()