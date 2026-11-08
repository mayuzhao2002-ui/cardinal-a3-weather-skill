#!/usr/bin/env python3
"""Standalone original skill helper. Python standard library only."""
import argparse
import json
import urllib.parse
import urllib.request

def forecast(latitude,longitude):
    if not -90<=latitude<=90 or not -180<=longitude<=180:raise ValueError("Invalid coordinates")
    query=urllib.parse.urlencode({"latitude":latitude,"longitude":longitude,
        "daily":"temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "forecast_days":2,"timezone":"auto"})
    # Adapted from https://open-meteo.com/en/docs — daily forecast query fields.
    with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?"+query,timeout=20) as response:
        return json.load(response)

if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--latitude",type=float,default=34.05);parser.add_argument("--longitude",type=float,default=-118.24)
    args=parser.parse_args()
    print(json.dumps(forecast(args.latitude,args.longitude),indent=2))
