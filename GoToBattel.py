import urllib2
opener = urllib2.build_opener(urllib2.HTTPHandler)

url = 'http://www.dragonsofmugloar.com/api/game/{39656}/solution'
data = '{"dragon":{"scaleThickness":9,"clawSharpness":5,"wingStrength":5,"fireBreath":1}}'
request = urllib2.Request(url, data)
request.add_header('Content-Type', 'application/json; charset=utf-8')
request.get_method = lambda: 'PUT'
print "test1"
resp = opener.open(request)
print resp.read(100)


data = '{"dragon":{"scaleThickness":9,"clawSharpness":1,"wingStrength":1,"fireBreath":9}}'
request = urllib2.Request(url, data)
request.add_header('Content-Type', 'application/json; charset=utf-8')
request.get_method = lambda: 'PUT'
print "test2"
resp = opener.open(request)
print resp.read(100)


"""
urlencode
some pemp staff here
addHeader("Content-Type", "application/json; charset=utf-8");
r = requests.put('http://www.dragonsofmugloar.com/api/game/{39656}/solution',Dragon)
 r = requests.put('http://www.dragonsofmugloar.com/api/game/{39656}/solution',{'dragon':{'scaleThickness':'5','clawSharpness':'5','wingStrength':'5','fireBreath':'5'}})
 '''{'dragon':{'scaleThickness': 5,'clawSharpness': 5,'wingStrength': 5,'fireBreath': 5}}'''
 
 r = requests.put('http://www.dragonsofmugloar.com/api/game/{39656}/solution', data = {'dragon':{'scaleThickness':'5','clawSharpness':'5','wingStrength':'5','fireBreath':'5'}})
 '

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
 
 
 PUT a message with an optional "Dragon" in the object to the specified URL. You must spread 20 points between all four stats.
```javascript
{
    "dragon": {
        "scaleThickness": 10,
        "clawSharpness": 5,
        "wingStrength": 4,
        "fireBreath": 1
    }
}
```

"""