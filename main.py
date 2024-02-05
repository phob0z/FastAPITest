from fastapi import FastAPI
import requests
import xml.etree.ElementTree as et
from zeep import Client, Settings

app = FastAPI()
pu = "https://mingle-sso.inforcloudsuite.com:443/MF5A2WL57LSB5PPE_DEM/as/"
oa_auth = "authorization.oauth2"
# or_revoke = "revoke_token.oauth2"
ot_token = "token.oauth2"
ci = "MF5A2WL57LSB5PPE_DEM~4m-IoYSoOGLQUrO0kIYPO4TdshOFPu7AU_Ij9R9jvHI"
cs = "G1iyuaIlfIOUc6IYB_dR9VHvJymcNTztkJrkkv7WUJX1JbSTIREbHIimURVLgMxNAwG9akP2HL-q-OfZY5tmqw"
username = "MF5A2WL57LSB5PPE_DEM#-xXOpRWOaqJWHruRAs2Ms6JcpOOGtMkTuvPzVAJ-OdxiJJB5iBNY3LYzk4wXbHQr558rQgMBkDJSw3OV6bHSsA"    #saak
password = "S1FLYIjvIpR7smX9NOElFFrxKP1VcbAPb1goDrE0zTQ4-FqBfU0DiC8AZCWMD1ZTKIea2PgoUDBBoq5PE98jIQ"                         #sask
autorizationTokenURL = pu + oa_auth
accessTokenURL = pu + ot_token
refreshTokenURL = pu + ot_token
redirectURi = "https://fast-api-test-sage.vercel.app/"
# authorizationServer = "https://mingle-sso.inforcloudsuite.com:443/MF5A2WL57LSB5PPE_DEM/as/authorization.oauth2"             #pu + oa

@app.get("/")
async def root():
    # redirect_uri: encodeURIComponent(settings.redirectUri),
    # scope:‘offline_access’,
    # refresh_token:req.user.refresh_token
    # ‘Cache-Control’: ‘no-cache’,
    # ‘grant_type’:‘refresh_token’,
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "application/json", "Authorization": "Basic " + ci + cs}
    # access_token = requests.get(url = accessTokenURL + "?grant_type=password&client_id=" + ci + "&client_secret=" + cs, headers=headers).text#json()["access_token"]
    access_token = requests.get(url = autorizationTokenURL + "?grant_type=password&client_id=" + ci + "&redirect_uri=https://fast-api-test-sage.vercel.app/" + + "&response_type=code", headers=headers).text#json()["access_token"]
    print(access_token)
    #requests.get(authorizationServer, params={client_id: "MF5A2WL57LSB5PPE_DEM~RvgYv88ONiYVwjTMhZpjnlVdatxcWKe2VT9gF_eaM7A",redirect_uri: ,response_type:code})
    return {"hola": "mundo"}

@app.get("/algo")
async def root():
    return "Hola"

@app.get("/soap")
async def root(token: str):
    req_headers = {"content-type": "text/xml; charset=utf-8", "authorization": "Bearer " + token}
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

@app.get("/soap3")
async def root(token: str = "eyJraWQiOiJrZzplMGRlNmFiZC1jY2NlLTQyYzEtYjFlNS05ZDkwNjdhMmRkMGMiLCJhbGciOiJSUzI1NiJ9.eyJTZXJ2aWNlQWNjb3VudCI6Ik1GNUEyV0w1N0xTQjVQUEVfREVNI1ljanJJOVNUQnhxNUEyQ0dwZEtUQ214Nl9Db0FiNG1KYTBLZkdBek5yR3JRQ18zOGh3by1DT01OeW5YQUI4bmxNd2x0bVpadEVFQi1KWDVNNk43cEVnIiwiVGVuYW50IjoiTUY1QTJXTDU3TFNCNVBQRV9ERU0iLCJJZGVudGl0eTIiOiI0YmVhYjNmMS02MzRjLTRlZjAtOWU3My0xYjIxMTY1OTFlYzUiLCJFbmZvcmNlU2NvcGVzRm9yQ2xpZW50IjoiMCIsImdyYW50X2lkIjoiZTg1NmFmMDctNjc5YS00NWZiLWFlZTQtYzk5OGQyYThmMDdiIiwiSW5mb3JTVFNJc3N1ZWRUeXBlIjoiQVMiLCJjbGllbnRfaWQiOiJNRjVBMldMNTdMU0I1UFBFX0RFTX40bS1Jb1lTb09HTFFVck8wa0lZUE80VGRzaE9GUHU3QVVfSWo5UjlqdkhJIiwianRpIjoiMzM0ZTdlZTEtYWY0NS00ZDE3LTlkMzEtMmIxZjI2NDE1MWRjIiwiaWF0IjoxNzA2OTI3NjUzLCJuYmYiOjE3MDY5Mjc2NTMsImV4cCI6MTcwNjkzNDg1MywiaXNzIjoiaHR0cHM6Ly9taW5nbGUtc3NvLmluZm9yY2xvdWRzdWl0ZS5jb206NDQzIiwiYXVkIjoiaHR0cHM6Ly9taW5nbGUtaW9uYXBpLmluZm9yY2xvdWRzdWl0ZS5jb20ifQ.fqidnXTOWodpxQtfp1Um3J-Jr9vxcKShgRoJlmleG_6ExXboceDoOyH9KRr9cj_mH905uroOgtNj-aDN5JVDDPOYy7VnzkjnMvCwyFh_BwVedlosVVc9hGxx8kUBDmzDk_i_sVHGYM9xeBBZSQEOXc9tEclYVxQK168iki2nHNgY5xIYCTAYpOk5_QoOv_LpqtCnNe2h6tQ7ESWc7eI9_s_YccF_WHglVtO3NMWsO8EiIB10fx81rGiukdu_qmK8_XvykEFPMOgHhNQJ17PHDp2gwr_ZR2Y7SeMPrw0CsIeGH4fM3bkIKpAfT26_TPmsapv0yiezhLJgngEySFDNEw"):
    url = "https://mingle-ionapi.inforcloudsuite.com/MF5A2WL57LSB5PPE_DEM/LN/c4ws/services/Contact_v3"
    settings = Settings(extra_http_headers={"content-type": "text/xml","authorization": "Bearer " + token})
    client = Client(url, settings=settings)
    response = client.service.Show(contactCode="CT0000001")
    return response

# <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:yourNamespace="YourNamespace">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <yourNamespace:YourOperationName>
#          <contactCode>CT0000001</contactCode>
#       </yourNamespace:YourOperationName>
#    </soapenv:Body>
# </soapenv:Envelope>

# from zeep import Client
# from zeep.transports import Transport
# from requests import Session

# # Bearer token
# bearer_token = "your_bearer_token_here"

# # Create a session with a custom transport to set the Authorization header
# session = Session()
# session.headers["Authorization"] = f"Bearer {bearer_token}"
# transport = Transport(session=session)

# # Instantiate a Client object with the URL to the WSDL file
# client = Client('https://pastebin.com/yP1cKdLN', transport=transport)

# # Call the operation with the appropriate input parameters
# result = client.service.YourOperationName(contactCode="CT0000001")

# # Print or process the result as needed
# print(result)