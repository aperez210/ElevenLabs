import elabs
import editFile as edit
import threading
import time
from playsound import playsound

def start():
    inp = ""
    worker = keyword(strBreak(inp))
    while worker != "Stopping...":
        worker.start()
        loadWhile(worker,"loading")
        worker.join()
        inp = input(":")
        worker = keyword(strBreak(inp))

def keyword(tokens):
    match tokens[0]:
        case "":
            return threading.Thread(target=intro)
        case "stop" | "x":
            return "Stopping..."
        case "help" | "?":
            return threading.Thread(target=help)
        case "delete":
            return threading.Thread(target=elabs.delete,args=(tokens[1],))
        case "add":
            return threading.Thread(target=elabs.add,args=(tokens[1], tokens[2]))
        case "tts" | "say":
            return threading.Thread(target=elabs.tts,args=(edit.getVoice(tokens[1]),joinStringList(tokens[3:len(tokens)]),tokens[2]))
        case "list":
            return threading.Thread(target=edit.listVoices())
        case "history":
            return threading.Thread(target=edit.listHistory())
        case "play":
            if tokens[1] == "last" : return threading.Thread(target=play,args=(edit.getLast(),))
            else : return threading.Thread(target=play,args=(tokens[1],))
        case "get":
            return threading.Thread(target=elabs.get())
        case "user":
            return threading.Thread(target=elabs.user())
 

def joinStringList(list):
    output = ""
    for string in list:
        output= f'{output}{string} '
    return output

def strBreak(S:str):
    tokens = []
    out = ""
    for c in S+" ":
        if c != " ":
            out = out + c
        else:
            tokens.append(out)
            out = ""
    return tokens

def play(sound):
    playsound(sound)

def loadWhile(thread,msg:str):
    c = thread.is_alive()
    while c:
        c = thread.is_alive()
        zzz = .15
        for i in range(4):
            match i:
                case 0:
                    s = f"{msg}    "
                case 1:
                    s = f"{msg}."
                case 2:
                    s = f"{msg}.."
                case 3:
                    s = f"{msg}..."
            print(s,end="\r")
            time.sleep(zzz)
        print("               ",end="\r")

def help():
    print("Help:")
    print("stop --------- stops the loop")
    print("delete <VoiceName> ----- deletes voice with given name")
    print("add <VoiceName> <Path to folder/file>")
    print("tts <VoiceName> <Output file> text to be spoken ----- generates output.mp3")

def intro():
    print("Eleven Labs Command Line Interface")

start()