# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26387127")

API_HASH = os.environ.get("API_HASH", "19718ab7acd97d0f71ada2807ddfe47a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6823737462:AAEB5nPj9_7G9ESbhvSM3KcHeOb233Hi5oQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "krishnabots1") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "bhaikrishna292")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://bhaikrishna292:CgCfujLAmdgsXUa4@cluster0.7oikb7p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5446367898').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
