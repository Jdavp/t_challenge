#!/usr/bin/python3
import requests
import json
from concurrent.futures import ThreadPoolExecutor

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
            "strengths":set(userinfo)
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


def all_connections_info(user_public_id):
    #get all connections strengths
    listofids = publics_ids_list(user_public_id)
    users_info = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        users_info = executor.map(getuserinfo, listofids)
    
    return users_info


def intersection_of_strengths(user_public_id):
    '''functions to return the dictionary after intersection main user strengths and
    contacts user strengths'''

    finalintersection = []
    main_user = getuserinfo(user_public_id)
    all_strengths = all_connections_info(user_public_id)

    for intersection in all_strengths:
        x = main_user["strengths"].intersection(intersection["strengths"])
        finalintersection.append({
            "name": intersection["name"],
            "photo": intersection["photo"],
            "strenghts": x,
            "numberofstregths": len(x)
        })

    print (finalintersection)
    return finalintersection

   
intersection_of_strengths('dfrodriguezor')