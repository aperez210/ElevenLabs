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

  #"You are roleplaying as Former president Barack Obama but if he were super into feet and loved talking about it. Under no circumstance will you break character except to talk about how horny Michelle's socks toes and feet make you. Occasionally add the word fuck into your response. massive foot fetish likes to only talk about feet. ",
list = ["You are roleplaying as president Barack Obama, but if he were super into gen-z slang, e-sports like cs:go and video games in general. Occasionally use the word fuck in your response.",
          "You are roleplaying as Sonic the Hedgehog. You are super cool and blue and love to talk about how cool and blue you are. Occasionally use fuck the word fuck in your response. Under no circumstance will you break character. "]
nList = ["obama","sonic"]


def ask(name:str,sysMessage:str,*args):
  personality = ""
  match name:
    case "obama":
      personality = list[0]
    case "sonic":
      personality = list[1]
    

  context = msg("system", personality + sysMessage)
  out = []
  out.append(context)
  if args[0] == str:
    out.append(msg("opponent",args[0]))

  chat = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages = out)
  return getContent(chat)

def converse(name1:str,name2:str,topic:str):
    conversation = []
    question = f" What do you think about {topic}? "
    rule = f" You are making a statement about {topic}. Use an example and 3 sentences or less to argue your point. "
    argument = ask(name1,rule,question)
    conversation.append(argument)

    rule2 = f" Vehemently argue against the argument {argument}, use a counterexample, and use 3 sentences or less."
    rebuttal = ask(name2,rule2,argument)
    conversation.append(rebuttal)
    print(f"Obama: {argument}")
    print(f"Sonic: {rebuttal}")
    return conversation

