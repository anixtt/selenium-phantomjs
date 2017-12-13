# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import json
import re

class robotspider():
    def __init__(self):
        url = "http://sheepridge.pandorabots.com/pandora/talk?botid=fef38cb4de345ab1&skin=iframe-voice"
        self.driver = webdriver.Chrome()
        self.html = self.driver.get(url)
        self.dict = {}
    def getsaying(self, value, driver, dict, count):
        area = driver.find_element_by_xpath("//input[@type='text']")
        area.clear()
        area.send_keys(str(value))
        driver.find_element_by_xpath("//input[@type='submit']").click()
        time.sleep(1)
        sayings = driver.find_elements_by_xpath("/html/body")
        text = sayings[0].text
        text = text.split('\n')
        print(text[2])
        print(text[3])
        dict['me'+str(count)] = text[2]
        dict['robot'+str(count)] = text[3]
        for i in range(len(dict)-1):
            stringa = 'me'+str(i)
            stringb = 'robot'+str(i)
            print(dict.get(stringa))
            print(dict.get(stringb))
        return json.dumps(dict, separators=(',', ':'), ensure_ascii=False)

        """
        pattern1 = re.compile(r'Lieutenant: (.*?){1,}')
        print(pattern1.search(text))
        pattern2 = re.compile(r'James T. Kirk: (.*?){1,}')
        print(pattern2.search(text))
        """
    def switchto(self, driver):
        driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frame[2]"))