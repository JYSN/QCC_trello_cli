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


import requests

import json

import private



# Variables


TKEY = private.TRELLO_KEY


TTKN = private.TRELLO_TKN



# Functions

## Requests

