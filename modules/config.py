import re
import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

OWNER_ID = int(getenv("OWNER_ID", "5798855486"))
