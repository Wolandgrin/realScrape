import os
import csv
import requests
from lxml import html
from selenium import webdriver


def move_ru():
    driver = webdriver.Chrome()

    #TODO: verify amount of pages
    max_page = 57

    #for all 56 pages
    for i in range(max_page - 1):
        url = "https://move.ru/agents/?page=" + str(i + 1) + "&limit=50"

        page_content = requests.get(url)
        tree = html.fromstring(page_content.content)
        agents_list = tree.xpath('//*[starts-with(@id, "agent-phone")]')

        # click on all Show Phone links on the page
        driver.get(url)
        for agent in agents_list:
            try:
                driver.find_element_by_css_selector("#" + agent.attrib.get('id') + " > a").click()
            except Exception as e:
                print(e)

        # get 'name-phone' pair to the dict
        mydict = {}
        for agent in agents_list:
            name = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[3]/div[' +
                                                str(agents_list.index(agent) + 1) + ']/div/div[1]/div/a[2]').text
            phone = driver.find_element_by_xpath('//*[@id="' + agent.attrib.get('id') + '"]/div/a').text
            mydict[name] = phone

        with open('move_ru.csv', 'a', newline='') as f:
            w = csv.writer(f)
            w.writerows(mydict.items())

    driver.close()
