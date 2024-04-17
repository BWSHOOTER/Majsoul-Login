import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 计算账户数量
acccounts = int(len(sys.argv[1:]) / 2)
print(f'Config {acccounts} accounts')

for i in range(acccounts):
    email = sys.argv[1 + i]
    passwd = sys.argv[1 + i + acccounts]
    print('----------------------------')

    # 1. 打开浏览器
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 720)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i + 1} loading game...')
    sleep(10)

    # 2. 输入邮箱
    screen = driver.find_element(By.ID, 'layaCanvas')
    ActionChains(driver).move_to_element_with_offset(screen, 250, -100).click().perform()
    driver.find_element(By.NAME, 'input').send_keys(email)
    print('Input email successfully')

    # 3. 输入密码
    ActionChains(driver).move_to_element_with_offset(screen, 250, -50).click().perform()
    driver.find_element(By.NAME, 'input_password').send_keys(passwd)
    print('Input password successfully')

    # 4. 点击登录
    ActionChains(driver).move_to_element_with_offset(screen, 250, 50).click().perform()
    print('Entering game...')
    sleep(20)  # 等待登录...

    # 模拟点击后再等待20秒
    sleep(20)
    print('Login success')
    driver.quit()
