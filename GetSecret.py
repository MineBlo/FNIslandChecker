import time
import requests

AuthorizationCode = input("Go here (https://www.epicgames.com/id/api/redirect?clientId=3446cd72694c4a4485d81b77adbb2141&responseType=code)\nAnd paste the text found next to 'AuthorizationCode'. You will need to be logged in the browser with the account that will be doing the web requests (DO NOT USE YOUR MAIN ACCOUNT):")
bearerresponse = requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token", data = {'grant_type': 'authorization_code', 'code':AuthorizationCode}, headers = {"Content-Type": "application/x-www-form-urlencoded","Authorization":"basic MzQ0NmNkNzI2OTRjNGE0NDg1ZDgxYjc3YWRiYjIxNDE6OTIwOWQ0YTVlMjVhNDU3ZmI5YjA3NDg5ZDMxM2I0MWE="}).json()
EpicID=bearerresponse['account_id']
Bearer=bearerresponse['access_token']
DeviceAuthResponse=requests.post("https://account-public-service-prod.ol.epicgames.com/account/api/public/account/"+EpicID+"/deviceAuth", headers = {"Authorization": "Bearer "+ str(Bearer)})
print("!!!!!!!!!!! NEVER SHARE THESE WITH ANYONE NOT EVEN ME AND DONT USE YOUR MAIN ACCOUNT TO GET THESE !!!!!!!!!!!!!!")
print("DEVICE ID"+DeviceAuthResponse.json()['deviceId'])
print("EPIC ID:"+DeviceAuthResponse.json()['accountId'])
print("SECRET ID"+DeviceAuthResponse.json()['secret'])
print("!!!!!!!!!!! NEVER SHARE THESE WITH ANYONE NOT EVEN ME AND DONT USE YOUR MAIN ACCOUNT TO GET THESE !!!!!!!!!!!!!!")
input()