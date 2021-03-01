import time
import os
import shelve
from bs4 import BeautifulSoup
from post import post_all
from urllib.request import urlopen

def setLastIdPosted(id): # acessa do banco o ultimo id postado no instagram
    s = shelve.open('test_shelf.db')
    try:
        s['last'] = id
    finally:
        s.close() 

def getText(tokens,listTexts):
   link = 'https://spotted.maronato.dev/spotted/view_spotted/'
   for i in range(len(tokens)):
      html = urlopen(link + tokens[i]+'/')
      bs = BeautifulSoup(html.read(),'html.parser')
      content = bs.find('div', class_= 'ui column eight wide')
      
      listTexts.append(str(content.p.getText()).strip())

# Função que separa o id do token
def getTokenId(listTokens,tokens,intTokens):   
   for i in range(len(listTokens)):
      tokens.append(listTokens[i][9:])
      intTokens.append(int(listTokens[i][9:])) 

#Função que pega os tokens no formato Spotted #123456
def getTokens(listTokens,lastSpotted):   
   spottedcount = 0
   pages = 1
   spottedAchado  = -1
   achei = False
   while(True):   
      html = urlopen('https://spotted.maronato.dev/spotted/list_spotteds/?page='+ str(pages))
      bs = BeautifulSoup(html.read(),'html.parser')
      nameList = bs.findAll('a', {'class':'header'})
      for name in nameList:
         spottedAchado = int(name.get_text()[9:])
         if(spottedAchado <= lastSpotted ):
            achei = True
            break
         listTokens.append(name.get_text())
      if(achei):
         break
      pages = pages + 1         
      
def get_last_spotteds():
    listTokens = [] #Lista de tokens, sendo um token Spotted #123456
    tokens = [] #Lista do id dos tokens em string, 123456
    intTokens = [] #Lista dos ids inteiros
    resultados = [] # dicionario contendo id e o texto correspondente aquele id 
    listTexts = [] # Lista de mensagens sem o token
    try:
        s = shelve.open('test_shelf.db')
    finally:
        lastSpotted =  int(s['last'])
        s.close()

    getTokens(listTokens,lastSpotted)
    print(listTokens)
    getTokenId(listTokens,tokens,intTokens)
    getText(tokens,listTexts)
   
    for i in range(len(listTexts)):
        resultados.append({'id':intTokens[i], 'text':listTexts[i]})
    resultados.reverse()
    if(len(resultados) > 0):
        setLastIdPosted(resultados[-1]['id'])
        post_all(resultados)
        
    

if __name__ == '__main__':
    setLastIdPosted(113180)
    #get_last_spotteds()
    #pass
