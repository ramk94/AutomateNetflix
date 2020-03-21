# Ram Bhattarai
# Automate Netflix Login


# Import important libraries
from selenium import webdriver
from time import sleep
import json

''''
Json Username and password format, expects a token.json file that has your username and password
{
    "name" : "your_username"
    "password": "your_password"
    }
'''


class AutomateNetflix:

    def __init__(self):
        with open("token.json") as reader:
            tokens = json.load(reader)
        self.password = tokens["password"]
        self.username = tokens["name"]
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.netflix.com/login")
        sleep(2)
        self.login()

    def login(self):
        self.driver.find_element_by_xpath("//input[@name=\"userLoginId\"]").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(4)


Netflix = AutomateNetflix()
