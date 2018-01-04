import csv
import requests
from lxml import html
from selenium import webdriver


def cian_ru():
    driver = webdriver.Chrome()

    # TODO: verify amount of pages
    max_page = 386

    # for all 385 pages
    for i in range(max_page - 1):
        url = "https://www.cian.ru/agents/?account_type=1&location%5B0%5D=1&sort=offers_count&p=" + str(i + 1)
        driver.get(url)
        page_content = requests.get(url)
        tree = html.fromstring(page_content.content)
        agents_list = tree.xpath('//*[starts-with(@class, "catalog__cell catalog__cell_for_avatar")]/a')

        # open every agent separately
        agents_dict = {}
        for agent in agents_list:
            agent_url = 'https://www.cian.ru' + str(agent.attrib.get('href'))
            driver.get(agent_url)

            # click on all Show Phone link on the page
            name = ''
            try:
                driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div').click()

                # get 'name-phone' pair to the dict
                name = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/div[2]/div[1]').text
                phone = driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div[3]').text
                agents_dict[name] = phone
            except Exception as e:
                print("No phone for " + name + ". " + str(e))

        with open('cian_ru.csv', 'a', newline='') as f:
            w = csv.writer(f, delimiter=';')
            w.writerows(agents_dict.items())

    driver.close()
