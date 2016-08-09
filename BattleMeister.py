import json
import xml.etree.ElementTree as ET
import requests
import urllib2
import random

NORMAL_WEATHER = "normal regular weather"

URL_GAME     = 'http://www.dragonsofmugloar.com/api/game'
URL_WEATHER  = 'http://www.dragonsofmugloar.com/weather/api/report/{%d}'
URL_BATTLE   = 'http://www.dragonsofmugloar.com/api/game/{%d}/solution'

DRAGON_STRING = '''{"dragon":{
                 "scaleThickness": %d,
                 "clawSharpness": %d,
                 "wingStrength": %d,
                 "fireBreath": %d}
                 }'''

def getStrRepres(char, number):
 s = ''
 for i in range(number):
     s= s + char
 return s
 
def newDragon(scaleThickness, clawSharpness, wingStrength, fireBreath):
    return DRAGON_STRING % (scaleThickness, clawSharpness, wingStrength, fireBreath)

def newRandomDragon():
    MAX_STAT = 10
    TOTAL_POINTS = 20
    
    sum = 0;
    
    while sum!= TOTAL_POINTS:
         param_list = list()
         sum = 0;
         for i in range(4):
             n = random.randint(0, MAX_STAT)
             sum += n
             param_list.append(n)
    print param_list
    return newDragon(param_list[0],param_list[1],param_list[2],param_list[3])

def putDragonToFigth(gameId, dragon):
 #print "Game ID = %d" % gameId
# print "Dragon = %s" % dragon 
 battle_url = URL_BATTLE % (gameId)  
 opener = urllib2.build_opener(urllib2.HTTPHandler)
 request = urllib2.Request(battle_url, dragon)
 request.add_header('Content-Type', 'application/json; charset=utf-8')
 request.get_method = lambda: 'PUT'
 resp = opener.open(request)
 battle_result = resp.read(200)
 print battle_result
 battle_info = json.loads(battle_result)
 stat = battle_info.get("status")
 mess = battle_info.get("message")
 #print stat
 return stat, mess
 
def getGameId(game_string):
 info = json.loads(game_string)
 gameId = info.get("gameId")
 #print "This game ID: %d"%gameId
 return gameId
 
def getWeather(gameId):
 wether_url = URL_WEATHER%gameId
 r = requests.get(wether_url)
 tree = ET.fromstring(r.content) 
 message = tree.find('message').text
 #print "This game message: %s" % message
 cordX   = tree.find('coords').find('x').text
 cordY   = tree.find('coords').find('y').text
 cordZ   = tree.find('coords').find('z').text
 varRat  = tree.find('varX-Rating').text
 #print "This game location X:%s, X:%s, X:%s, Var: %s"% (cordX,cordY,cordZ,varRat)
 cord = [cordX,cordY,cordZ]
 return message,cord

def getKnight(game_string):
 info = json.loads(game_string)
 gameId = info.get("gameId")
 #print "This game ID: %d"%gameId
 knight_dict = info.get("knight")
 knName = knight_dict.get("name") 
 knAgil = knight_dict.get("agility") 
 knArmr = knight_dict.get("armor") 
 knAtak = knight_dict.get("attack") 
 knEndur = knight_dict.get("endurance") 
 knProp = [knAgil,knArmr,knAtak,knEndur]   
 return knName, knProp

def getNewGame():
 game_url = URL_GAME
 r = requests.get(game_url)
 game_string = r.content
 
 print "New Game string:"
 print game_string
 gameId = getGameId(game_string)
 mes, cord = getWeather(gameId)
 if NORMAL_WEATHER in mes:
    print "This game have regular weather"
 else:
    print "Strange weather, don't fly!"
    print mes
    return
 
 newKn = getKnight(game_string)
 print "The knight name:%s"% newKn[0]
 print "The knight properties:%s"% newKn[1]
 print "Knight agility: "+getStrRepres('g',newKn[1][0])
 print "knight   armor: "+getStrRepres('r',newKn[1][1])
 print "knight  attack: "+getStrRepres('a',newKn[1][2])
 print "knight enduran: "+getStrRepres('e',newKn[1][3])
 
 print "Now we try to fight with basic Dragon! (5,5,5,5)"
 dragon = newDragon(5,5,5,5)
 putDragonToFigth(gameId, dragon)   

def tryRandomDrago(game_string):
 gameId = getGameId(game_string)
 newKn  = getKnight(game_string)
 for i in range(100):
    dragon = newRandomDragon()
    status, mess = putDragonToFigth(gameId, dragon)
    if "Defeat" not in status:
        print "This dragon WINNN!!"
        print dragon
    
    
 
 
 
def print_game(dic_game_info):
 if dic_game_info.get("gameId") == None:
     print "Can't find gameId key in dic_game_info"
     return
    
 gameId = dic_game_info.get("gameId")
 print "This game ID: %d"%gameId
 
 mes, cord = getWeather(gameId)
 if NORMAL_WEATHER in mes:
    print "This game have regular weather"
 else:
    print "Strange weather, don't fly!"
    print mes
    return
    
 if dic_game_info.get("knight") == None:
     print "Can't find knight key in dic_game_info"
     return

 newKn = getKnight(dic_game_info.get("knight"))
 print "The knight name:%s"% newKn[0]
 print "The knight properties:%s"% newKn[1]
 print "Knight agility: "+getStrRepres('g',newKn[1][0])
 print "knight   armor: "+getStrRepres('r',newKn[1][1])
 print "knight  attack: "+getStrRepres('a',newKn[1][2])
 print "knight enduran: "+getStrRepres('e',newKn[1][3])
 
 print "Now we try to fight with basic Dragon! (5,5,5,5)"
 dragon = newDragon(5,5,5,5)
 putDragonToFigth(gameId, dragon)
 print "Fight is over :( \n"

game_sets = [ """
{"gameId":5661739,"knight":{"name":"Sir. Miguel Peters of Alberta","attack":4,"armor":3,"agility":7,"endurance":6}}
{"gameId":1893314,"knight":{"name":"Sir. Ralph Carlson of New Brunswick","attack":8,"armor":5,"agility":2,"endurance":5}}
{"gameId":4359863,"knight":{"name":"Sir. Terry Briggs of British Columbia","attack":8,"armor":3,"agility":3,"endurance":6}}
{"gameId":7768841,"knight":{"name":"Sir. Jeremy Hammond of Ontario","attack":6,"armor":4,"agility":2,"endurance":8}}
{"gameId":5295543,"knight":{"name":"Sir. Chad Norman of Nunavut","attack":4,"armor":8,"agility":4,"endurance":4}}
{"gameId":1135436,"knight":{"name":"Sir. Roy Welch of Manitoba","attack":0,"armor":7,"agility":6,"endurance":7}}
{"gameId":515604, "knight":{"name":"Sir. Albert Simpson of Saskatchewan","attack":1,"armor":3,"agility":8,"endurance":8}}
{"gameId":4681585,"knight":{"name":"Sir. Dustin Hawkins of Nunavut","attack":0,"armor":6,"agility":6,"endurance":8}}
{"gameId":7499510,"knight":{"name":"Sir. Scott Wright of Nunavut","attack":5,"armor":2,"agility":6,"endurance":7}}
{"gameId":9895445,"knight":{"name":"Sir. Christian Lucas of Quebec","attack":2,"armor":5,"agility":7,"endurance":6}}
{"gameId":3992409,"knight":{"name":"Sir. Franklin Sanders of New Brunswick","attack":1,"armor":7,"agility":5,"endurance":7}}
{"gameId":7520527,"knight":{"name":"Sir. Carl Johnson of Newfoundland and Labrador","attack":7,"armor":2,"agility":6,"endurance":5}}
{"gameId":6585600,"knight":{"name":"Sir. Gilbert Marshall of Newfoundland and Labrador","attack":7,"armor":2,"agility":6,"endurance":5}}
{"gameId":801343, "knight":{"name":"Sir. Leon Meyer of Ontario","attack":8,"armor":2,"agility":8,"endurance":2}}
{"gameId":26920,  "knight":{"name":"Sir. Marvin Banks of Saskatchewan","attack":7,"armor":1,"agility":5,"endurance":7}}
"""]
#getNewGame()
"""
try to solve this batle:
{"gameId":4681585,"knight":{"name":"Sir. Dustin Hawkins of Nunavut","attack":0,"armor":6,"agility":6,"endurance":8}}

one dgaron WIN!
Game ID = 4681585

This dragon WINNN!!
{"dragon":{
                 "scaleThickness": 4,
                 "clawSharpness": 4,
                 "wingStrength": 2,
                 "fireBreath": 10}
                 }

This dragon WINNN!!
{"dragon":{
                 "scaleThickness": 5,
                 "clawSharpness": 2,
                 "wingStrength": 3,
                 "fireBreath": 10}
                 }
                 
"""

game_string = '{"gameId":4681585,"knight":{"name":"Sir. Dustin Hawkins of Nunavut","attack":0,"armor":6,"agility":6,"endurance":8}}'

tryRandomDrago(game_string)

