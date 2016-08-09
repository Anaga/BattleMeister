import json
import xml.etree.ElementTree as ET
import requests
import urllib2


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

def putDragonToFigth(gameId, dragon):
 print "Game ID = %d" % gameId
 print "Dragon = %s" % dragon 
 battle_url = URL_BATTLE % (gameId) 
 
 opener = urllib2.build_opener(urllib2.HTTPHandler)
 request = urllib2.Request(battle_url, dragon)
 request.add_header('Content-Type', 'application/json; charset=utf-8')
 request.get_method = lambda: 'PUT'
 print "test2"
 resp = opener.open(request)
 print resp.read(100)
 
 return

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

def getKnight(knight_dict):
 knName = knight_dict.get("name") 
 if knName ==  None:
     print "Can't find knight Name in dic_game_info"
     return

 knAgil = knight_dict.get("agility") 
 knArmr = knight_dict.get("armor") 
 knAtak = knight_dict.get("attack") 
 knEndur = knight_dict.get("endurance") 
 if None in {knAgil,knArmr,knAtak,knEndur} :
     print "Can't find knight properties"
     return 

 knProp = [knAgil,knArmr,knAtak,knEndur]   
 return knName, knProp
 print "The knight name was: %s"%knName
 print "knight agility: "+getStrRepres('g',knAgil)
 print "knight   armor: "+getStrRepres('r',knArmr)
 print "knight  attack: "+getStrRepres('a',knAtak)
 print "knight enduran: "+getStrRepres('e',knEndur) 
 print ""

def getNewGame():
 game_url = URL_GAME
 r = requests.get(game_url)
 print "New Game string:"
 print r.content
 print_game(r.json())
  
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
"""]
getNewGame()

dragon = newDragon(10,1,1,8)
putDragonToFigth(4681585, dragon)

dragon = newDragon(10,8,1,1)
putDragonToFigth(4681585, dragon)

dragon = newDragon(3,8,1,8)
putDragonToFigth(4681585, dragon)
