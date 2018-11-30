# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:27:12 2018

@author: mohammadali
"""

from six.moves.urllib.request import urlopen
import requests
import json


username = input("Enter Instagram Username : ")
link = "https://www.instagram.com/"+username+"/"
response = urlopen(link)
content = response.read()

words = str(content)
index = words.find("logging_page_id")

userid = "" ; final_userid = ""
for x in range(50):
    userid = userid + (words[index])
    index += 1
    if x == 49 :
        for j in range(len(userid)):
            if userid[j].isnumeric():
                final_userid += userid[j]

print("The user id is : "+final_userid)


url = "https://i.instagram.com/api/v1/users/"+final_userid+"/info/"
r = requests.get(url)

parsed = json.loads(r.text)
print("HD Image Url : "+parsed['user']['hd_profile_pic_url_info']['url'])
