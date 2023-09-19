import requests
import json
import util
import editFile as edit
key = edit.getKey()


def add(name:str,path:str):
    url = "https://api.elevenlabs.io/v1/voices/add"
    files = []
    fileList = []
    isFolder = util.folderCheck(path)
    if isFolder:
        fileList = util.openFolder(path)
    else:
        fileList.append(path)
    for fName in fileList:
        files.append(('files', (fName, open(fName, 'rb'), 'audio/mpeg')))

    headers = {
    "Accept": "application/json",
    "xi-api-key": key
    }

    data = {
        'name': name,
        'labels': '{"accent": "American"}',
        'description': "This is a description"
    }
    response = requests.post(url, headers=headers, data=data, files=files)
    vid = ""
    try:
        vid = json.loads(response.text).get("voice_id")
    except:
        print("fail")
    edit.saveVoice(name,vid)
    print(response.text)

def get(vid:str):
    url = f"https://api.elevenlabs.io/v1/voices/{vid}?with_settings=true"
    headers = {
        "Accept": "application/json",
        "xi-api-key": key
    }

    response = requests.get(url, headers=headers)

    #if(json.loads(response.text)['detail']['status'] == 'voice_not_found'):
    #    return False
    return response.text
    
def editVoice(name:str,fileList):
    url = f"https://api.elevenlabs.io/v1/voices/{str}/edit"

    headers = {
    "Accept": "application/json",
    "xi-api-key": key
    }

    data = {
        'name': 'Voice New name',
        'labels': '{"accent": "British"}',
        'description': 'Voice description'
    }

    files = []
    for fName in fileList:
        files.append('files', (fName, open(fName, 'rb'), 'audio/mpeg'))

    response = requests.post(url, headers=headers, data=data, files=files)
    return response.text

def tts(vid:str,words:str,fileOut:str):
    CHUNK_SIZE = 1024
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{vid}"

    headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": key
    }

    data = {
    "text": words,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": .6,
        "similarity_boost": .9
    }
    }
    response = requests.post(url, json=data, headers=headers)
    fName = f'output\\{fileOut}.mp3'
    if util.has(fName):
        fName = util.numerateFiles(fName)
    with open(fName, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)
    edit.saveHistory(fName)

def user(*args):
    url = "https://api.elevenlabs.io/v1/user"

    headers = {
    "Accept": "application/json",
    "xi-api-key": key
    }

    response = requests.get(url, headers=headers)
    if(len(args)== 0):
        x = json.loads(response.text)['subscription']
        for key,value in x.items():
            print(key+":", value)
    elif(len(args) == 1):
        x = json.loads(response.text)['subscription'][args[0]]
        print(args[0]+":",x)

def delete(vid:str):
    url = f"https://api.elevenlabs.io/v1/voices/{vid}"

    headers = {
    "Accept": "application/json",
    "xi-api-key": key
    }
    x = ""
    response = requests.delete(url, headers=headers)
    try:
        if (json.loads(response.text)["status"]):
            x = "Deletion Successful"
    except:
        print("Error:")
        for key,value in json.loads(response.text)["detail"].items():
            x = x + key + ":" + value + "\n" 
    print(x)
    