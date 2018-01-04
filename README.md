# realScrape
Pre-reqs:
- git, python 3.4.4, pysharm, chromedriver(added to PATH)
- pip v9
- selenium

This is an automated scraping tool for names and phone numbers. It is working for the following websites:
- cian.ru
- move.ru
- realto.ru
- gdeetotdom.ru

Additionally it can send messages to the realtors for gdeetotdom.ru website

Usage:
    launcher.py -s scenario

Following scenarios implemented:
- all (scrapes names and phones for all 3 websites)
- cian_ru (scrapes names and phones for cian.ru website) 
- move_ru (scrapes names and phones for move.ru website) 
- realto_ru (scrapes names and addresses for realto.ru website) 
- gdeetotdom_ru (scrapes names and phones for gdeetotdom.ru website) 
- gdeetotdom_msg (sends messages for realtors in gdeetotdom.ru website) 