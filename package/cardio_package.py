from selenium import webdriver
from selenium.webdriver.common.by import By

import random

def cardio_pack(bot,chat_id):
    cardio= ['점핑잭', '버피 테스트', '계단 오르기','스트레칭','걷기', '조깅', '달리기', '자전거']
    health_result = random.choice(cardio)
    if health_result == cardio[0]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=510&cal_type=E')
        jump = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        jm_info = f'실내에서 할 수 있는 유산소 운동 중 {health_result}을 추천합니다.\n{jump}'
        driver.quit()
        bot.send_message(chat_id, jm_info)
        return jm_info
        
    elif health_result == cardio[1]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=491&cal_type=E')
        buf = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        bf_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다.\n{buf}'
        driver.quit()
        bot.send_message(chat_id, bf_info)
        return bf_info

    elif health_result == cardio[2]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=21&cal_type=E')
        stair = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        str_info = f'실내에서 할 수 있는 유산소 운동 중  {health_result}를 추천합니다.\n{stair}'
        driver.quit()
        bot.send_message(chat_id, str_info)
        return str_info

    elif health_result == cardio[3]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=194&cal_type=E')
        strch =driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        sr_info = f'실내에서 할 수 있는 유산소 운동  {health_result}을 추천합니다.\n스트레칭은 {strch}'
        driver.quit()
        bot.send_message(chat_id, sr_info)
        return sr_info

    elif health_result == cardio[4]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=14&cal_type=E')
        walk = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        wk_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다. 걷기 운동 효과 {walk}'
        driver.quit()
        bot.send_message(chat_id, wk_info)
        return wk_info

    elif health_result == cardio[5]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=54&cal_type=E')
        jog = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        jg_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}을 추천합니다.\n{jog}'
        driver.quit()
        bot.send_message(chat_id, jg_info)
        return jg_info

    elif health_result == cardio[6]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=77&cal_type=E')
        run = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        rn_info = f'야외에서 할 수 있는 유산소 운동 중 {health_result}를 추천합니다. 달리기는 {run}'
        driver.quit()
        bot.send_message(chat_id, rn_info)
        return rn_info

    elif health_result == cardio[7]:
        driver = webdriver.Chrome('chromedriver.exe')
        driver.implicitly_wait(10)
        driver.get('https://www.dietshin.com/calorie/sports-view.asp?cal_idx=254&cal_type=E')
        bic = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/ul/li').text
        bc_info = f' 야외에서 할 수 있는 유산소 운동 중 {health_result}운동을 추천합니다.\n{bic}'
        driver.quit()
        bot.send_message(chat_id, bc_info)
        return bc_info