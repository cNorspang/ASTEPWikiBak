from flask import Flask, jsonify, request, json
from flask_cors import CORS, cross_origin
import requests
import json
import os 

service = Flask(__name__)
cors = CORS(service)
service.config['CORS_HEADERS'] = 'Content-Type'

def main():
    print("\nWorking directory: " + os.getcwd()+ "\n\n")
    URL = "http://astep-2020-fall-stream-service-connector.astep-dev.cs.aau.dk"
    # windowsize, verbose, numberoftrees, sizelimit and maxdepth are optional params.
    # If not set, they will have default values shown below.
    PARAMS = {'key': 'SW504E20',
              'service': '-o',
              'verbose': False,
              # paper suggest 250
              'windowssize': 20,
              # paper suggest 25
              'numberoftrees': 5,
              # paper suggest windowssize/10
              'sizelimit': 2,
              # paper suggest 15
              'maxdepth': 3,
              'data': "1,1,2,2,3,3\n3,2,3,1,5,2\n1,1,3,2,3,6"}

    #Open connection
    print("\nresult from opening connection " + json.dumps(openConnection(URL, PARAMS), indent=2))

    # Uncomment what you need
    #Send row(s) - n lines of data (in this case n=2 seperated by \n)
    #print("\nresult from sending row: " + json.dumps(sendRow(URL, PARAMS), indent=2))
    #print("\nresult from sending row: " + json.dumps(sendRow(serviceInfo = serviceInfo), indent=2))
    #print("\nresult from sending row: " + json.dumps(sendRow(serviceInfo = serviceInfo), indent=2))

    #test
    print("\nresult from sending TSLA.csv: " + json.dumps(sendFileName("web_service/LOGI_adj_close.csv", URL, PARAMS), indent=2))


    #Send manyrows file
    #print("\nresult from sending TSLA.csv: " + json.dumps(sendFileName("outlier_without_string.csv", URL, PARAMS), indent=2))
    #Send IBM.csv
    #print("\nresult from sending IBM.csv: " + json.dumps(sendFileName("IBM.csv", URL, PARAMS), indent=2))
    #Send TSLA.csv
    #print("\nresult from sending TSLA.csv: " + json.dumps(sendFileName("TSLA.csv", URL, PARAMS), indent=2))
    #Send outlier.csv
    #print("\nresult from sending outlier.csv: " + json.dumps(sendFileName("outlier.csv", URL, PARAMS), indent=2))
    #Send outlier2.csv
    #print("\nresult from sending outlier2.csv: " + json.dumps(sendFileName("outlier.csv", URL, PARAMS), indent=2))
    #Close connection
    print("\nresult from closing the connection " + json.dumps(closeConnection(URL, PARAMS), indent=2))

def sendFileName(fileName, URL, PARAMS):
    with open(fileName, 'rb') as f:
        return requests.post(URL + "/" + "sendset", params = PARAMS, files={'file': f}).json()

def openConnection(URL, PARAMS):
    return requests.post(url = URL + "/" + "open", params = PARAMS).json()

def closeConnection(URL, PARAMS):
    return requests.post(url = URL + "/" + "close", params = PARAMS).json()

def sendRow(URL, PARAMS):
    return requests.post(url = URL + "/" + "sendrow", params = PARAMS).json()

if __name__ == "__main__":
    main()