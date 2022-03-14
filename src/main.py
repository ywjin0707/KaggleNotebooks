import requests

img_data = requests.get("https://capture-website-api.herokuapp.com/capture?url=https://www.kaggle.com/yongwonjin").content
with open('kaggleprofile.jpg', 'wb') as handler:
  handler.write(img_data)
