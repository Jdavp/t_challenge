#!/usr/bin/python3
import requests
import json


def getuserinfo(user_public_id):
    #get user basic info (picture,username, strengths)

    userinfo = []

    response = requests.get("https://torre.bio/api/bios/{}".format(user_public_id))

    userpicture = response.json()['person'].get('picture')

    username = response.json()['person'].get('name')

    userinfo.append(username)
    userinfo.append(userpicture)


    userstrengths = response.json()['strengths']

    for names in userstrengths:
        strengthname = names['name']
        userinfo.append(strengthname)

    return set(userinfo)

    


def publics_ids_list(user_public_id):
#get user connections public_ids 
    idslists = []
    usercontacts = requests.get("https://bio.torre.co/api/people/{}/connections".format(user_public_id))


    contactsids = usercontacts.json()

    for i in range(len(contactsids)):
        cont = contactsids[i]['person']['publicId']
        idslists.append(cont)
    print(idslists)   
    return idslists





def all_connections_strenghts(user_public_id):
# get all connections strenghts
    listofids = publics_ids_list(user_public_id)
    users_info = []

    for y in listofids:
        users_info.append(getuserinfo(y))
    print(len(users_info))
    print(users_info)
    return users_info

#

print(type(getuserinfo('dfrodriguezor')))

print(type(all_connections_strenghts('dfrodriguezor')))