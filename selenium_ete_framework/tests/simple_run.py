# import time
#
# from selenium import webdriver
#
# # from selenium.webdriver.chrome.service import Service
# #
# # service_obj=Service("C:\shetty\chromedriver-win32\chromedriver.exe")
# driver=webdriver.Firefox()
#
# driver.get("https://www.facebook.com/")
#
# time.sleep(3)
# line=file.readline()
# while line !="":
#     print(line)
#     line=file.readline()

# file.close()
# print(file.readline(1))
# print(file.read(1))

# with open("C:/Users/shettappa.chalawadi/PycharmProjects/selenium_ete_framework/tests/test.jason",'r') as reader:
#     reader.readlines()
# with open("C:/Users/shettappa.chalawadi/PycharmProjects/selenium_ete_framework/tests/wr.json", 'w') as writer:
#     writer.write("testing")

# data = {
#     "name": "John Doe",
#     "age": 30,
#     "is_student": False,
#     "courses": ["Math", "Science", "History"]
# }
#
# # with open("wr.json", 'r') as file:
# #     data = json.load(file)
# #     # print(data)
# with open("second.json",'w') as file:
#     json.dump(data,file)

import json

source="C:/Users/shettappa.chalawadi/PycharmProjects/selenium_ete_framework/tests/second.json"
target="C:/Users/shettappa.chalawadi/PycharmProjects/selenium_ete_framework/tests/wr.json"

with open(source,'r') as file:
    data=json.load(file)

with open(target,'w') as f1:
    json.dump(data,f1)
