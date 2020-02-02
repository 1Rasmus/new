# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 09:53:00 2020

@author: Nutzer
"""

import requests

r = requests.get('https://fanteam-game.api.scoutgg.net/tournaments/245268/players?')

print (r.text)