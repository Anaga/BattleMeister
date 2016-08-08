import json
import urllib
import xml.etree.ElementTree as ET
import requests

def getStrRepres(char, number):
 s = ''
 for i in range(number):
     s= s + char
 return s
 
def newDragon(scaleThickness, clawSharpness, wingStrength, fireBreath):
    sDrag = '''{ "dragon": {
                 "scaleThickness": %d,
                 "clawSharpness": %d,
                 "wingStrength": %d,
                 "fireBreath": %d}
                 } '''% (scaleThickness, clawSharpness, wingStrength, fireBreath)
                 
    return sDrag

def putDragonToFigth(gameID, dragon):
 print "Game ID = %d" % gameID
 print "Dragon = %s" % dragon
 
 battle_url = '''http://www.dragonsofmugloar.com/api/game/{%d}/solution''' % (gameID)
 
 """
 Request Lib:
 http://docs.python-requests.org/en/master/user/quickstart/
 >>> r = requests.put('http://httpbin.org/put', data = {'key':'value'})
 >>> r = requests.options('http://httpbin.org/get')
 """
 
 print "\n Test 1"
 r = requests.options(battle_url)
 if r.status_code == requests.codes.ok: print r.content
 
 print "\n Test2"
 r = requests.put(battle_url, dragon)
 if r.status_code == requests.codes.ok: print r.content
 
 print "\n Test3"
 r = requests.put(battle_url, "Abc")
 if r.status_code == requests.codes.ok: print r.content
 
 print "\n Test4"
 data = {"Dragon" : {"dragon":{"scaleThickness":5,"clawSharpness":5,"wingStrength":5,"fireBreath":5}}}
 r = requests.put(battle_url, data)
 if r.status_code == requests.codes.ok: print r.content
 
 print "\n Test5"
 data = {"dragon":{"scaleThickness":5,"clawSharpness":5,"wingStrength":5,"fireBreath":5}}
 r = requests.put(battle_url, data)
 if r.status_code == requests.codes.ok: print r.content
 
 print "\n Test6"
 data = {"Dragon" : '{"dragon":{"scaleThickness":5,"clawSharpness":5,"wingStrength":5,"fireBreath":5}}'}
 r = requests.put(battle_url, data)
 if r.status_code == requests.codes.ok: print r.content
  
 print "\n Test7"
 data = {"Dragon" : {"dragon":{"scaleThickness":5,"clawSharpness":5,"wingStrength":5,"fireBreath":5}}}
 r = requests.put(battle_url, json=data)
 if r.status_code == requests.codes.ok: print r.content


def print_game(dic_game_info):
 if dic_game_info.get("gameId") == None:
     print "Can't find gameId key in dic_game_info"
     return
    
 gameId = dic_game_info.get("gameId")
 print "This game ID: %d"%gameId
 
 wether_url = '''http://www.dragonsofmugloar.com/weather/api/report/{%d}'''%gameId
 #print 'Retrieving wether from ', wether_url
 uh = urllib.urlopen(wether_url)
 data = uh.read()
 #print 'Retrieved',len(data),'characters'
 tree = ET.fromstring(data)
 
 message = tree.find('message').text
 print "This game message: %s" % message
 cordX   = tree.find('coords').find('x').text
 cordY   = tree.find('coords').find('y').text
 cordZ   = tree.find('coords').find('z').text
 varRat  = tree.find('varX-Rating').text
 print "This game location X:%s, X:%s, X:%s, Var: %s"% (cordX,cordY,cordZ,varRat)
  
 if dic_game_info.get("knight") == None:
     print "Can't find knight key in dic_game_info"
     return

 knight = dic_game_info.get("knight")
 knName = knight.get("name") 
 if knName ==  None:
     print "Can't find knight Name in dic_game_info"
     return
 print "The knight name was: %s"%knName

 knAgil = knight.get("agility") 
 knArmr = knight.get("armor") 
 knAtak = knight.get("attack") 
 knEndur = knight.get("endurance") 
 if None in {knAgil,knArmr,knAtak,knEndur} :
     print "Can't find knight properties"
     return 

 print "knight agility: "+getStrRepres('g',knAgil)
 print "knight   armor: "+getStrRepres('r',knArmr)
 print "knight  attack: "+getStrRepres('a',knAtak)
 print "knight enduran: "+getStrRepres('e',knEndur) 
 print ""
  
 print "Now we try to fight with basic Dragon! (5,5,5,5)"
 dragon = newDragon(5,5,5,5)
 putDragonToFigth(gameId, dragon)
 print "Fight is over :( \n"
 
wether_url = '''http://www.dragonsofmugloar.com/weather/api/report/{gameId}'''
url = 'http://www.dragonsofmugloar.com/api/game'

inp = '''{"gameId":1893314,"knight":{"name":"Sir. Ralph Carlson of New Brunswick","attack":8,"armor":5,"agility":2,"endurance":5}}'''

info = json.loads(inp.encode('utf-8'))
#print_game(info)

inp = '''{"gameId":4359863,"knight":{"name":"Sir. Terry Briggs of British Columbia","attack":8,"armor":3,"agility":3,"endurance":6}}'''
info = json.loads(inp)
#print_game(info)


inp = ''' {"gameId":7768841,"knight":{"name":"Sir. Jeremy Hammond of Ontario","attack":6,"armor":4,"agility":2,"endurance":8}}'''
info = json.loads(inp)
#print_game(info)


inp = '''{"gameId":5295543,"knight":{"name":"Sir. Chad Norman of Nunavut","attack":4,"armor":8,"agility":4,"endurance":4}}'''
info = json.loads(inp)
#print_game(info)

inp = '''{"gameId":1135436,"knight":{"name":"Sir. Roy Welch of Manitoba","attack":0,"armor":7,"agility":6,"endurance":7}}'''
#info = json.loads(inp)
#print_game(info)

inp = ''' {"gameId":515604,"knight":{"name":"Sir. Albert Simpson of Saskatchewan","attack":1,"armor":3,"agility":8,"endurance":8}}'''
info = json.loads(inp)
print_game(info)


print "try to open url %s"%url
page = urllib.urlopen(url)
game = page.read()
print "Game is %s"%game
info = json.loads(game)
print_game(info)
