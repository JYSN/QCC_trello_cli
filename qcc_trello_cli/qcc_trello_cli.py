""" A simple command line utility to pull the Trello API for the cards under TODO on the QCC tasks board
    1. Use the /members/{id}/boards endpoint and the special member ID of ME to get a list of open boards
        1. Filter for only open boards by passing the FILTER parameter with the value OPEN
        2. Include the board LISTS in the results by passing LISTS param with the value OPEN
        3. Find board with the NAME QCC: {NAME}, the the list with NAME TODO in the board."
    2. Get cards on TODO list
        1. using /lists/{id}/cards endpoint
            filter to only open cards by passing CARDS param with value VISIBLE
    3. Print card info
        1.Fore each card:
        Skip any non-member card by checking if SUBSCRIBED == TRUE
        Print card NAME, SHORTURL, DUE DATE, and LABELS NAME

    related board
    https://trello.com/b/e9BAH5bn/qcc-nightfate
    """



# Imports
# ===============


import requests

import json

import private

from pprint import pprint

from os import _exit as exit



# Variables
# ===================

## Debug variables
# __________________

DEBUG = False

 
## Globals
# ___________________

# TKEY = private.TRELLO_KEY


# TTKN = private.TRELLO_TKN

TRELLORL = "https://api.trello.com/1/members/me/boards"

## Request variables
# ___________________

MULTIPASS = {
    'key': private.TRELLO_KEY,
    'token' : private.TRELLO_TKN
}

# Functions
# ===================


def nl(contents):
    print("\n")
    print(contents)
    print("\n")


def small_goal():
    # print trello key and token
    print("\n", MULTIPASS, "\n")


def callweb(url, parameters):
    """A webrequest function for returning JSON data, as well as type/length info.
        Expects two arguements (URL, PARAMETERS),
            where the second arguement should be a dictionary for the request paramters.
        Raises an error with Code and Reason if response.ok=False"""
    
    response = requests.get(url, params=parameters)

    if not response.ok:
        print(f"The Cake is a lie!: {response.status_code} {response.reason}")
        exit(1)

    data  = response.json()
    
    # print(f" length:{len(data)},\n type:{type(data)}")

    return data

# ## Requests

# MAIN
# ===================

def main():
    """Uses private tokens to make webrequest to trello's API,
        then parses data for specific info"""
    # small_goal()
    nl("NEW INSTANCE !1!1")
    data = callweb("https://api.trello.com/1/xxx", MULTIPASS)
    # data = callweb(TRELLORL, MULTIPASS)
    pprint(data)


main()



