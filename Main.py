import requests
import os
import discord
import time
import threading
import asyncio
import json
from requests.structures import CaseInsensitiveDict
from discord import app_commands 

url = "https://discord.com/api/webhooks/1276577230268665957/BZTvykCizh_wgGe4UKR0fsfq05J_fJLBLfEIz-t1J_f0N1C6W7w26ZvDjwt9-hMxjIXt" # webhook url, from here: https://i.imgur.com/f9XnAew.png

result = requests.post(url, json = {"content" : "message content","username" : "custom username"})