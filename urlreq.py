from urllib.request import urlopen
req = urlopen("https://devops-de.tk/")
#print(req)
#print(req.status)
print(req.code)
#print(req.reason)
try: 
    url = urlopen("https://google.com/comm")
    print("Die Verbindung ist stabil!")
except Exception as e:
    print(e)
