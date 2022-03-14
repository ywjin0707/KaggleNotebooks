from pathlib import Path
import datetime
import pytz
import requests

def update_footer():
    timestamp = datetime.datetime.now(pytz.timezone("Canada/Central")).strftime("%c")
    footer = Path('../FOOTER.md').read_text()
    return footer.format(timestamp=timestamp)

img_data = requests.get("https://capture-website-api.herokuapp.com/capture?url=https://www.kaggle.com/yongwonjin").content
with open(Path('./kaggleprofile.png'), 'wb') as handler:
  handler.write(img_data)

readme = Path('../README.md').read_text()
with open('../README.md', "w+") as f:
    f.write(readme + update_footer())
