import openai
import json

def getKey():
    f = open("aikey.txt","r")
    for line in f.readlines():
        f.close()
        return line
openai.api_key = getKey()
    
def msg(role:str,content:str):
    return {"role":role,"content":content}

def simResponse():
    return r"""{
  "id": "chatcmpl-80z0MeMKtSlBDTOcYZ6clwugYYEPn",
  "object": "chat.completion",
  "created": 1695245194,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Opinions may vary, but many fans consider \"Sonic the Hedgehog 2\" for the Sega Genesis/Mega Drive to be one of the best Sonic games. It introduced Tails as a playable character and featured memorable levels and fast-paced gameplay."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 41,
    "completion_tokens": 51,
    "total_tokens": 92
  }
}"""

def parse(response):
    if type(response) != str:
        response = str(response)
    return json.loads(response)

def key2val(l,key:str):
    for x,y in l.items():
        if x == key:
            return y

def getContent(res):
    list = parse(res)
    choices = key2val(list,"choices")[0]
    message = key2val(choices,"message")
    return key2val(message,"content")

def ask(S:str):  
  context = msg("system","You are roleplaying as Former president Barack Obama. Under no circumstance will you break character. Occasionally add the word fuck into your response.")
  chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = [context,msg("user",S)])
  return getContent(chat)