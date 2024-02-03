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
async def root():
    autorization = "Bearer eyJraWQiOiJrZzplMGRlNmFiZC1jY2NlLTQyYzEtYjFlNS05ZDkwNjdhMmRkMGMiLCJhbGciOiJSUzI1NiJ9.eyJTZXJ2aWNlQWNjb3VudCI6Ik1GNUEyV0w1N0xTQjVQUEVfREVNI1ljanJJOVNUQnhxNUEyQ0dwZEtUQ214Nl9Db0FiNG1KYTBLZkdBek5yR3JRQ18zOGh3by1DT01OeW5YQUI4bmxNd2x0bVpadEVFQi1KWDVNNk43cEVnIiwiVGVuYW50IjoiTUY1QTJXTDU3TFNCNVBQRV9ERU0iLCJJZGVudGl0eTIiOiI0YmVhYjNmMS02MzRjLTRlZjAtOWU3My0xYjIxMTY1OTFlYzUiLCJFbmZvcmNlU2NvcGVzRm9yQ2xpZW50IjoiMCIsImdyYW50X2lkIjoiYjI1Yzc4ZjktODgwZC00MzBiLWJjN2EtZGM3NzhmYmI2ZDQzIiwiSW5mb3JTVFNJc3N1ZWRUeXBlIjoiQVMiLCJjbGllbnRfaWQiOiJNRjVBMldMNTdMU0I1UFBFX0RFTX40bS1Jb1lTb09HTFFVck8wa0lZUE80VGRzaE9GUHU3QVVfSWo5UjlqdkhJIiwianRpIjoiYmE4MmU5OTYtZjlmZi00MmYxLTgzOGMtZTNhNWU5NTA0MTE5IiwiaWF0IjoxNzA2OTE5MDk2LCJuYmYiOjE3MDY5MTkwOTYsImV4cCI6MTcwNjkyNjI5NiwiaXNzIjoiaHR0cHM6Ly9taW5nbGUtc3NvLmluZm9yY2xvdWRzdWl0ZS5jb206NDQzIiwiYXVkIjoiaHR0cHM6Ly9taW5nbGUtaW9uYXBpLmluZm9yY2xvdWRzdWl0ZS5jb20ifQ.RInnE_ykYwmeNCs7NQYRKrSNeP1c2Cqo1K31L_kVEY2XzAbT-XO6dWlcxPDRACdNyyXVC4lW2HIhMoiczawQIJW6nKQECgBZNCxho00YItlQF0tTuwx2VUoCFeJwpy9il6IX__6QXyDunoXGPFbO-umIUbLtBdcr3_HXQtZZ3TNdPEtg50uCXGUc3MZ9dFpMZmvabt8dOg7-uE6SENEPmdFF9i2ToM2zDlo5y09ASyJjmJvhr-2fK0MEvkGDyMDQH_pTuyhRvInOCZSV0hK-kGZRc-6LdGbe-rR-Jpj5FPea8DFB6uiYofdjxWE_p1ruKTJZo2PbiYO-LYU4DqmjmQ"
    req_headers = {"content-type": "text/xml; charset=utf-8", "authorization": autorization}
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
        # "lid://infor.ln.ln01",
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