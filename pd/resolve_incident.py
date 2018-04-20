#!/usr/bin/env python3
import sys
import os
import pypd

pypd.api_key = os.environ['PD_API_KEY']
id_to_resolve = sys.argv[1]

print("Attempting to resolve", id_to_resolve, "using api key", pypd.api_key)

incident = pypd.Incident.fetch(id_to_resolve)
incident.resolve(from_email="jmichaud@pagerduty.com")
print("Successfully resolved ", incident)