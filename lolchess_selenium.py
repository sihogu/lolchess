from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def make_url(x_url):
    response = requests.get(x_url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0 x64)'})
    text = response.text
    html = BeautifulSoup(text, 'html.parser')
    return html
    
def find_page(x_page_number,x_url,x_html):
    target_text = "공략 더 보기"
    target_element = x_html.find(string=target_text)
    parent_element = target_element.find_parent().parent.parent.get("class")
    x_page = x_url + x_html.find_all('div',{'class':parent_element})[x_page_number].find('a')['href'] #class = css-1jardaz emls75t6
    return x_page

def find_table():
    LV5_button = driver.find_element(By.XPATH, "//*[@id=\"content-container\"]/div[2]/div[2]/div[1]/div[1]/div[2]/div/nav/div[1]")
    LV5_button.click()
    sleep(0.2)
    x_target_table = driver.find_element(By.XPATH,'//*[@id="content-container"]/div[2]/div[2]/div[1]/div[1]/div[1]')
    return x_target_table

def find_deck():
    sleep(0.2)
    x_target_table = driver.find_elements(By.CSS_SELECTOR,'.Champions.css-1z2so7.e1mdo1l0')
    return x_target_table

def first_augmenter():
    x_target_deck_name = driver.find_element(By.XPATH,'//*[@id="content-container"]/div[2]/div[2]/div[2]/div/div[1]/div/div/div[1]/h2')
    return x_target_deck_name


def find_deck_name(x_html,x_deck_name_list):
    x_deck_name = x_html.find('div',{'class':'css-1s5hngw e691syl3'}).find('h2').text
    x_deck_name_list.append(x_deck_name)
    return x_deck_name_list

def find_item(x_html,x_deck_name_list):
    t = x_html.find('div',{'class':'css-1s5hngw e691syl3'}).text
    x_deck_name_list.append(t.split('수집 아이템 추천')[1].split('활용 아이템')[0].replace('\xa0',''))
    return x_deck_name_list


url = 'https://lolchess.gg'
html = make_url(url+'/meta')
driver = webdriver.Chrome()

number = len(html.find_all('div',{'class':'css-128625v emls75t7'}))
numbers = range(1,number)



        
def make_text():
    deck_name_list = []
    item_list = []
    list_names = [deck_name_list, item_list]
    function_names2 = [find_deck_name, find_item]
    for i in numbers:
        for function_name2, list_name in zip(function_names2, list_names):
            page = find_page(i, url, html)
            tip_page = make_url(page) #html.paser
            
            function_name2(tip_page, list_name)
    return deck_name_list, item_list

def make_table_image():
    for i in numbers:
        page = find_page(i, url, html)
        driver.get(page)
        sleep(0.5)
        target = find_table()
        target.screenshot(f'lolchess_image/table/table_{i}.png')
        
def make_deck_image():
    for i in numbers:
        driver.get(url+'/meta')
        sleep(0.5)
        target = find_deck()[3]
        target.screenshot(f'lolchess_image/deck/deck_{3}.png')