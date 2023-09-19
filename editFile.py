vidFile = "vids.txt"
histFile = "history.txt"
keyFile = "key.txt"

def loadVoices():
    f = open(vidFile,"r")
    i = 0
    j = 0
    out = []
    pair = []
    for line in f.readlines():
        line = line.strip()
        pair.append(line)
        
        if i == 1:
            out.append(pair)
            pair = []
        j+=1
        i =j % 2
    f.close()
    return out

def saveVoice(name:str,vid:str):
    f = open(vidFile,"a")
    f.write("\n"+name+"\n"+vid)
    f.close()

def getVoice(s:str):
    vlist =loadVoices()
    for name,vid in vlist:
        if s == name:
            return vid

def listVoices():
    vlist = loadVoices()
    for name,vid in vlist:
        print(f'Name: {name},   Voice ID: {vid}')

def loadHistory():
    f = open(histFile,"r")
    out = []
    for line in f.readlines():
        out.append(line)
    f.close()
    return out

def saveHistory(path:str):
    f = open(histFile,"a")
    f.write("\n"+path)
    f.close()

def getHist(s:str):
    hList = loadHistory()
    for path in hList:
        if path.endswith(s):
            return path
        
def listHistory():
    hlist = loadHistory()
    for path in hlist:
        print(f'Path: {path}')

def getLast():
    hlist = loadHistory()
    return hlist[len(hlist)-1]

def getKey():
    f = open(keyFile,"r")
    for line in f.readlines():
        f.close()
        return line


    