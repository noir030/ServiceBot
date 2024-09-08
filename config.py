import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("BOT_TOKEN")
admin = int(os.getenv("ADMIN_ID"))
group = int(os.getenv("GROUP_ID"))