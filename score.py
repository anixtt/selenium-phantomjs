#!usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
import time
import json

#spider类
class enspider():
    #类的初始化
    def __init__(self):
        #目标url
        url = "http://www.yingyu.com/pigai.html"
        #phantomjs驱动的路径
        self.driver = webdriver.PhantomJS(executable_path="E:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe")
        #目标url的html
        self.html = self.driver.get(url)
    #爬虫主体，获取数据
    def getscore(self, value, driver):
        dict = {}
        #通过定位元素输入或获取值
        textarea = driver.find_element_by_id("pigai_txt")
        textarea.clear()
        textarea.send_keys(str(value))
        driver.find_element_by_id("loading").click()
        time.sleep(2)
        score = driver.find_element_by_id("score").text
        print("评分: ", score)
        dict['评分'] = score
        voca = driver.find_element_by_class_name("dim_bk_1").get_attribute("title")
        print("词汇：", voca)
        dict['词汇'] = voca
        sentence = driver.find_element_by_class_name("dim_bk_2").get_attribute("title")
        print("句子：", sentence)
        dict['句子'] = sentence
        structure = driver.find_element_by_class_name("dim_bk_3").get_attribute("title")
        print("篇章结构：", structure)
        dict['篇章结构'] = structure
        content = driver.find_element_by_class_name("dim_bk_4").get_attribute("title")
        print("内容相关：", content)
        dict['内容相关'] = content
        i_s = driver.find_elements_by_class_name("view3xh")
        Txts = driver.find_elements_by_class_name("sentTxt")
        hxs = driver.find_elements_by_xpath("//div[@class='view3Error vSentError']/ul")
        flag = 1
        for i in range(0, len(i_s)):
            print(i_s[i].text, Txts[i].text)
            dict['评语序号'] = i_s[i].text
            dict['例句'] = Txts[i].text
            for h in hxs[i].find_elements_by_class_name(" snt_hx"):
                print(h.text)
                dict['原因 ' + str(flag)] = h.text
                flag += 1
            flag = 1
        #将dict转换为json数据格式
        return json.dumps(dict, separators=(',', ':'), ensure_ascii=False)
    #第一次打开时需要转换到iframe中才能定位元素
    def switch_to(self, driver):
        driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div[5]/iframe"))
