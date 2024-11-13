import requests
import json
data =  {
      "title": "トマトスープレシピ",
      "making_time": "15分",
      "serves": "5人",
      "ingredients": "玉ねぎ, トマト, スパイス, 水",
      "cost":450
    }

response = requests.delete(
    "http://127.0.0.1:8000/recipes/1"
)

print(response.json())
