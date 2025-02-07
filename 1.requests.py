
import requests


URL = "https://www.link-academy.com/"

response = requests.get(URL)
print(response.status_code)
print(type(response.content))
print(response.text)

# 1 byte = 8 biti 

#OLD STYLE
# file_handler = open("link-academy.html", "w")
# file_handler.write(response.text)
# file_handler.close()

#NEW STYLE

with open("link-academy.html", "w", encoding = "utf-8") as file_handler:
    file_handler.write(response.text)