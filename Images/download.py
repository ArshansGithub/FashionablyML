import requests

toDownload = open("pluh.txt", "r").read().splitlines()

for eachImg in toDownload:
    req = requests.get(eachImg)
    
    if req.status_code == 200:
        open(f"downloads/{toDownload.index(eachImg) + 1}.jpeg", "wb").write(req.content)
        print(f"Successfully wrote to downloads/{toDownload.index(eachImg) + 1}.jpeg")
    else:
        print(req.text)
        print(req.status_code)
        print("something went wrong")
    
    
    