import csv
import requests
from lxml import html
from selenium import webdriver


def gdeetotdom_ru():
    driver = webdriver.Chrome()

    # TODO: verify amount of pages
    max_page = 688

    # for all 687 pages
    for i in range(max_page - 1):
        url = "https://www.gdeetotdom.ru/realtors/search/?rid=1232535%2C100001&sort_order=asc&sort_by=agency&PAGEN_1=" \
              + str(i + 1)

        page_content = requests.get(url)
        tree = html.fromstring(page_content.content)
        agents_list = tree.xpath('//*[starts-with(@class, "link link-black link-underline-dashed")]')

        # click on all Show Phone links on the page
        driver.get(url)
        for agent in agents_list:
            try:
                driver.find_element_by_xpath('//*[@data-realtor-id="' + agent.attrib.get('data-realtor-id') +
                                             '"]').click()
            except Exception as e:
                print(e)

        # get 'name-phone' pair to the dict
        agents_dict = {}
        for agent in agents_list:
            name = ''
            try:
                name = driver.find_element_by_xpath(
                    '//*[@id="page__container"]/div[1]/div/div[1]/div[1]/div/div[5]/div[4]/div[' +
                    str(agents_list.index(agent) + 1) + ']/div/div[2]/div/div[1]/a/span/span').text
                phone = driver.find_element_by_xpath(
                    '//*[@id="page__container"]/div[1]/div/div[1]/div[1]/div/div[5]/div[4]/div[' +
                    str(agents_list.index(agent) + 1) + ']/div/div[3]/ul/li').text
                agents_dict[name] = phone
            except Exception as e:
                print("No phone for " + name + ". " + str(e))

        with open('gdeetotdom_ru.csv', 'a', newline='') as f:
            w = csv.writer(f, delimiter=';')
            w.writerows(agents_dict.items())

    driver.close()
