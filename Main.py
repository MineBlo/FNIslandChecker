import requests
import time
from requests.structures import CaseInsensitiveDict

def GetBearer():
    global bearer
    bearerresponse = requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token", data = {'grant_type': 'device_auth', 'account_id':EpicID, 'device_id': DeviceID, 'secret': Secret}, headers = {"Content-Type": "application/x-www-form-urlencoded","Authorization":"basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="}).json()
    bearer=bearerresponse['access_token']
    print(bearer)
    return bearer

def GetIslandInfo(Island):
    islandc = requests.get("https://links-public-service-live.ol.epicgames.com/links/api/fn/mnemonic/"+Island, headers = {"Authorization": "Bearer "+ str(bearer)})
    if("errorCode" in islandc):
        GetBearer()
        islandc = requests.get("https://links-public-service-live.ol.epicgames.com/links/api/fn/mnemonic/"+Island, headers = {"Authorization": "Bearer "+ str(bearer)})
    return islandc.json()

def SendWebHook(Text,Island,ShouldPing):
    if(ShouldPing==True):
        requests.post(Webhookurl, json = {"content" : "<@"+DiscordID+"> "+Text,"username" : Island})
    else:
        requests.post(Webhookurl, json = {"content" : Text,"username" : Island})
DiscordIDfile=open("DiscordID.txt")
DiscordID = DiscordIDfile.read()
DiscordIDfile.close()
Webhookurlfile=open("webhookURL.txt")
Webhookurl = Webhookurlfile.read()
Webhookurlfile.close()
EpicIDfile=open("EpicID.txt")
EpicID = EpicIDfile.read()
EpicIDfile.close()
Secretfile=open("Secret.txt")
Secret = Secretfile.read()
Secretfile.close()
DeviceIDfile=open("DeviceID.txt")
DeviceID = DeviceIDfile.read()
DeviceIDfile.close()
Islands=[]
Islandsfile=open("Islands.txt")
GetBearer()
for i in Islandsfile:
    Islands+=[i.strip("\n")]
Islandsfile.close()
print(Islands)
while (True):
    for Island in Islands:
        IslandInfo=GetIslandInfo(Island)
        try:
            if(IslandInfo['moderationStatus'] == 'Approved'):
                print("ALL GOOD "+Island)
                SendWebHook("No Issues",Island,False)
            else:
                SendWebHook("Island could not be reached or was Rejected",Island,True)
                print("NOT ALL GOOD2 "+Island)
        except:
            SendWebHook("Island could not be reached or was Rejected",Island,True)
            print("NOT ALL GOOD "+Island)
    time.sleep(50.0)






