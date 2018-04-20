#!/usr/bin/env python3
import sys
import os
import pypd

pypd.api_key = os.environ['PD_API_KEY']
id_to_resolve = sys.argv[1]

print("Hello! Using api key", pypd.api_key)
print("Resolved incident", id_to_resolve)