#!/usr/bin/python3
import requests
import json


def getuserinfo(user_public_id):
    #get user basic info (picture,username, strengths)

    userinfo = []

    response = requests.get("https://torre.bio/api/bios/{}".format(user_public_id))

    userpicture = response.json()['person'].get('picture')

    username = response.json()['person'].get('name')

    userstrengths = response.json()['strengths']

    for names in userstrengths:
        strengthname = names['name']
        userinfo.append(strengthname)

    return {"name": username,
            "photo": userpicture,
            "strenghts":set(userinfo)
            }

    
def publics_ids_list(user_public_id):
#get user connections public_ids 
    idslists = []
    usercontacts = requests.get("https://bio.torre.co/api/people/{}/connections".format(user_public_id))


    contactsids = usercontacts.json()

    for i in range(len(contactsids)):
        cont = contactsids[i]['person']['publicId']
        idslists.append(cont) 
    return idslists


def all_connections_strenghts(user_public_id):
# get all connections strenghts
    listofids = publics_ids_list(user_public_id)
    users_info = []

    for y in listofids:
        users_info.append(getuserinfo(y))
    return users_info

#

def intersection_of_strenghts(user_public_id):
    finalintersection = []
    main_user = getuserinfo(user_public_id)
    all_strengths = all_connections_strenghts(user_public_id)

    for intersection in all_strengths:
        x = main_user["strenghts"].intersection(intersection["strenghts"])
        finalintersection.append({
            "name": intersection["name"],
            "photo": intersection["photo"],
            "strenghts": x,
            "numberofstreghts": len(x)
        })

    print(finalintersection)
    return finalintersection

   

intersection_of_strenghts('dfrodriguezor')