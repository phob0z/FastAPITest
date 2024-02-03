from fastapi import FastAPI
import requests
import xml.etree.ElementTree as et
from zeep import Client

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/algo")
async def root():
    return "Hola"

@app.get("/soap")
async def root(bearerToken: str):
    req_headers = {"content-type": "text/xml; charset=utf-8", "authorization": "Bearer " + bearerToken}
    req_body =  "<?xml version=\"1.0\" encoding=\"utf-8\"?>"
    req_body += "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:pur=\"http://www.infor.com/businessinterface/Contact_v3\" >"
    req_body += "<soapenv:Header></soapenv:Header>"
    req_body += "<soapenv:Body>"
    req_body += "<pur:Show>"
    req_body += "<ChangeRequestType>"
    req_body += "<DataArea>"
    req_body += "<Contact_v3>"
    req_body += "<contactCode>CT0000001</contactCode>"
    req_body += "</Contact_v3>"
    req_body += "</DataArea>"
    req_body += "</ChangeRequestType>"
    req_body += "</pur:Show>"
    req_body += "</soapenv:Body>"
    req_body += "</soapenv:Envelope>"
    response = requests.post(
        "https://mingle-ionapi.inforcloudsuite.com/MF5A2WL57LSB5PPE_DEM/LN/c4ws/services/Contact_v3",
        data=req_body,
        headers=req_headers
    )
    root = et.fromstring(response.text)
    resultado = root.find(".//emailAddress").text
    return resultado

@app.get("/soap2")
async def root(intA: int, intB: int):
    url = "http://www.dneonline.com/calculator.asmx?WSDL"
    client = Client(url)
    response = client.service.Add(intA=intA, intB=intB)
    return response