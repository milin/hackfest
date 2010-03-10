#!/usr/bin/env python

from twisted.internet import task
from twisted.internet import reactor
from twisted.web import client

import sys
import json
import random
import time
from datetime import datetime

RANDOMIZE = True
EVENT_LOG = 'events.log'

def logEvent(event):
    global EVENT_LOG
    if type(EVENT_LOG) is str:
        open(EVENT_LOG, 'w').close()
        EVENT_LOG = open(EVENT_LOG, 'a')
    print >>EVENT_LOG, event
    EVENT_LOG.flush()

class Service(object):
    def status(self):
        if RANDOMIZE:
            return random.choice((True, False))
        return self._status()
        
class URL(Service):
    def __init__(self, teamname, url, points=1):
        self.teamname = teamname
        self.url = url
        self.points = points

    def _status(self):
        try: page = client.getPage(self.url)
        except: return False
        # url should contain text like `NAME Team'
        regex = r'(\w+)\sTeam'
        match = re.search(regex, page, re.I)
        owner = match.group(1) if match else ''
        return self.teamname.upper() == owner.upper()
    
class SSH(Service):
    def __init__(self, user, host, points=2):
        self.user = user
        self.host = host
        self.points = points
        
    def _status(self):
        # TODO: Implement
        return True

class Team(object):
    def __init__(self, name, services):
        self.name = name
        self.score = 0
        self.services = dict.fromkeys(services, False)
        self.time = None
        
    def update(self):
        for s in self.services:
            self.services[s] = s.status()
            self.time = str(datetime.now())
            if self.services[s]:
                self.score += s.points
        logEvent(self.json())

    def json(self):
        servs = {}
        for s in self.services:
            servs[s.__class__.__name__] = self.services[s]
        team = vars(self).copy()
        team['services'] = servs
        return json.dumps(team)

    def __str__(self):
        return str(vars(self))
    

teams = [
    Team('red', (
            URL('red', 'localhost'),
            SSH('whitey', 'localhost'),
            )),
    Team('blue', (
            URL('blue', 'localhost'),
            SSH('whitey', 'localhost'),
            )),
    ]

def updateTeams():
    for t in teams:
        t.update()

l = task.LoopingCall(updateTeams)
l.start(3.0)
