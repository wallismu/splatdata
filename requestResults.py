#!/usr/bin/env python
import requests
import json
import random
import time
from datetime import datetime
from dotenv import load_dotenv
import os
import SplatoonResult

load_dotenv()

def makeRequest():
    url = "https://app.splatoon2.nintendo.net/api/results"

    payload = {}
    headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0.1; SCH-I545 Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36',
    'cookie': os.getenv("COOKIE")
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.status_code)
    return response.json()

def writeResultsToFile(filename, response):
    with open(filename, 'w') as outfile:
        json.dump(response, outfile)

if __name__ == "__main__":
    start = time.time()

    PERIOD_OF_TIME = 61200  # 17 hours

    f = open(os.getenv("CUSTOMPATH") + "counter.txt", "r")
    counter = int(f.read())
    f.close()

    log = open(os.getenv("CUSTOMPATH") + "log.txt", "a")
    log.write("CRON started at: " + str(datetime.now()) + "\n")
    print ("is something happening??")

    while(True):
        # Wait.....
        rnd = random.randint(1620, 3060)
        #rnd = random.randint(3, 8)
        time.sleep(rnd)

        response = makeRequest()
        log.write("Made request at: " + str(datetime.now()) + "\n")
        
        # Add to master.csv
        sp = SplatoonResult.splatoonResult(response)
        if(sp.generateCSV()): # it actually DID something, save the file
            # Increase counter
            counter += 1
            # Write counter to file
            f = open(os.getenv("CUSTOMPATH") + "counter.txt", "w")
            f.write(str(counter))

            fn = os.getenv("CUSTOMPATH") + "archive/result" + str(counter) + ".json"
            # save to archive
            writeResultsToFile(fn, response)

            log.write("Recorded resulsts at: " + fn + "\n")

        # Break at midnight
        if time.time() > start + PERIOD_OF_TIME : break

        

    