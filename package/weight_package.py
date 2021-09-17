from selenium import webdriver
from selenium.webdriver.common.by import By

import random


def weight_pack(bot,chat_id):
    weight = ['팔굽혀펴기','윗몸일으키기','턱걸이','플랭크','벤치프레스','데드리프트','스쿼트','밀리터리프레스'] 
    health_result = random.choice(weight)

    if health_result == weight[0]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=451&cal_type=E')
        pus = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        pu_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{pus}' 
        driver.quit()
        bot.send_message(chat_id, pu_info)
        return pu_info

    elif health_result == weight[1]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=453&cal_type=E')
        stup = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        st_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{stup}'
        driver.quit()
        bot.send_message(chat_id, st_info)
        return st_info

    elif health_result == weight[2]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=316&cal_type=E')
        pul = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        pl_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{pul}'
        driver.quit()
        bot.send_message(chat_id, pl_info)
        return pl_info

    elif health_result == weight[3]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=378&cal_type=E')
        plk = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        plk_info = f'집에서 할 수 있는 근력운동 중 {health_result}를 추천합니다.\n{plk}'
        driver.quit()
        bot.send_message(chat_id, plk_info)
        return plk_info

    elif health_result == weight[4]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=105&cal_type=E')
        bnp = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        bp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n{bnp}'
        driver.quit()
        bot.send_message(chat_id, bp_info)
        return bp_info

    elif health_result == weight[5]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=59&cal_type=E')
        dlft = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        dl_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n{dlft}'
        driver.quit()
        bot.send_message(chat_id, dl_info)
        return dl_info

    elif health_result == weight[6]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=461&cal_type=E')
        squ =driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        sq_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다. 스쿼트 운동 효과, {squ}'
        driver.quit()
        bot.send_message(chat_id, sq_info)
        return sq_info

    elif health_result == weight[7]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=471&cal_type=E')
        mlp = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li/text()').text
        mp_info = f'더 강도높은 운동을 원하신다면 헬스장에 가보세요. {health_result}를 추천합니다.\n밀리터리 프레스는 {mlp}'
        driver.quit()
        bot.send_message(chat_id, mp_info)
        return mp_info
