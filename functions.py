#!/usr/bin/python3
import requests
import json

#get user basic info (picture,username, strengths)
userinfo = []

response = requests.get("https://torre.bio/api/bios/dfrodriguezor")

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
idslists = []
usercontacts = requests.get("https://bio.torre.co/api/people/dfrodriguezor/connections")


contactsids = usercontacts.json()

for i in range(len(contactsids)):
    cont = contactsids[i]['person']['publicId']
    idslists.append(cont)


# get all connections strenghts

users_info = []

for y in idslists:
    all_user_strenghts = []
    response = requests.get("https://torre.bio/api/bios/{}".format(y))

    userpicture = response.json()['person'].get('picture')

    username = response.json()['person'].get('name')

    all_user_strenghts.append(username)
    all_user_strenghts.append(userpicture)

    userstrengths = response.json()['strengths']

    for names in userstrengths:
        strengthname = names['name']
        all_user_strenghts.append(strengthname)
    users_info.append(all_user_strenghts)


# intersection beetween user all contacts strengths

    for all in users_info:
        print(intersection(userinfo,users_info))