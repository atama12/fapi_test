import requests
import json
data =  {
      "title": "トマトスープ",
      "making_time": "15分",
      "serves": "5人",
      "ingredients": "玉ねぎ, トマト, スパイス, 水",

    }

response = requests.post(
    "https://fapi-test.onrender.com/recipes",
    data=json.dumps(data),
    headers={"Content-Type": "application/json"}
)

print(response.json())
