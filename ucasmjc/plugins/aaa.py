import json
from requests_html import HTMLSession
session = HTMLSession()
data = session.get("https://kfc-crazy-thursday.vercel.app/api/index")
print(data.html.text)