#!/usr/bin/env python3
import os
import pypd
pypd.api_key = os.environ['PD_API_KEY']

incidents = pypd.Incident.find(maximum=10, statuses=['triggered', 'acknowledged'])

for i in incidents:
    print(i.id)
    print(i['description'])