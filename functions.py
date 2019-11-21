#!/usr/bin/python3
import requests
import json

#get user basic info (picture,username, strengths)
userinfo = []

response = requests.get("https://torre.bio/api/bios/xica369")

userpicture = response.json()['person'].get('picture')

username = response.json()['person'].get('name')

userinfo.append(username)
userinfo.append(userpicture)


userstrengths = response.json()['strengths']

for names in userstrengths:
    strengthname = names['name']
    userinfo.append(strengthname)

print(userinfo)


#get user connections ids 
usercontacts = requests.get("https://bio.torre.co/api/people/xica369/connections")


contactsids = usercontacts.json()

for i in range(len(contactsids)):
    cont = contactsids[i]['person']['publicId']
    print(cont)