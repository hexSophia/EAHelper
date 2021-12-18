import time
import requests
import re
import random
import os
import win32api
from bs4 import BeautifulSoup
from selenium import webdriver

# 设置标题名称
os.system("title EA Helper Premium V2.0 Coder:YinBuLiao")


# username = 'nikita.gringgitta@gmail.com'
# password = 'Inuyasha01'
# region = 'usa'

def getCVolumeSerialNumber():
    CVolumeSerialNumber = win32api.GetVolumeInformation('C:\\')[1]
    if CVolumeSerialNumber:
        return str(CVolumeSerialNumber)
    return None


macm = getCVolumeSerialNumber()

try:
    with open(r'account.json') as f:
        line1 = f.readline()
        line2 = f.readline()
        name = line1.rstrip()
        pwd = line2.rstrip()
    website = 'https://ea-helper.com/'
    account_url = requests.get(
        website + 'verification.php?username=' + name + '&password=' + pwd)
    hwid_url = requests.get(website + 'hwidverification.php/?username=' + name + '&hwid=' + str(macm))
    expire = requests.get(website + 'verification.php/?username=' + name + '&expire')
    if 'success' in account_url.text:
        if 'nosub' in expire.text:
            print(u'您不是Premium用户')
            os.system("pause")
            os.exit()
        else:
            if '1' in hwid_url.text:
                os.system('cls')
                print(u'欢迎您：' + name)
                print(u'到期时间：' + expire.text)
            elif '2' in hwid_url.text:
                os.system('cls')
                print(u'欢迎您：' + name)
                print(u'到期时间：' + expire.text)
            elif '3' in hwid_url.text:
                os.system('cls')
                print(u'欢迎您：' + name)
                print(u'到期时间：' + expire.text)
            elif '0' in hwid_url.text:
                print(u'HWID错误，请联系管理员')
                os.system("pause")
                os.exit()
            elif '4' in hwid_url.text:
                print(u'HWID错误，请联系管理员')
                os.system("pause")
                os.exit()
    else:
        print('账号或密码错误')
        os.system("pause")
        os.exit()
except:
    forum_username = input('请输入论坛账号：')
    forum_password = input('请输入论坛密码：')
    website = 'https://ea-helper.com/'
    account_url = requests.get(
        website + 'verification.php?username=' + forum_username + '&password=' + forum_password)
    hwid_url = requests.get(website + 'hwidverification.php/?username=' + forum_username + '&hwid=' + str(macm))
    expire = requests.get(website + 'verification.php/?username=' + forum_username + '&expire')
    if 'success' in account_url.text:
        if 'nosub' in expire.text:
            print(u'您不是Premium用户')
            os.system("pause")
            os.exit()
        else:
            if '1' in hwid_url.text:
                os.system('cls')
                print(u'欢迎您：' + forum_username)
                print(u'到期时间：' + expire.text)
                file = open(r'account.json', mode='w')
                data = forum_username + '\n' + forum_password
                file.write(data)
                file.close()
            elif '2' in hwid_url.text:
                os.system('cls')
                print(u'欢迎您：' + forum_username)
                print(u'到期时间：' + expire.text)
                file = open(r'account.json', mode='w')
                data = forum_username + '\n' + forum_password
                file.write(data)
                file.close()
            elif '3' in hwid_url.text:
                os.system('cls')
                print(u'欢迎您：' + forum_username)
                print(u'到期时间：' + expire.text)
                file = open(r'account.json', mode='w')
                data = forum_username + '\n' + forum_password
                file.write(data)
                file.close()
            elif '0' in hwid_url.text:
                print(u'HWID错误，请联系管理员')
                os.system("pause")
                os.exit()
            elif '4' in hwid_url.text:
                print(u'HWID错误，请联系管理员')
                os.system("pause")
                os.exit()
    else:
        print('账号或密码错误')
        os.system("pause")
        os.exit()
username = input('请输入EA账号：')

password = input('请输入EA密码：')

comfirmbirthday = input('是否获取生日？(y/n)')
translate = input('是否访问国际版谷歌翻译？(y/n)')
clearcookie = input('是否清理缓存(y/n)：')

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
}

# 获取firstname
res = requests.get('http://www.shenfendaquan.com/', headers=headers)
res.encoding = 'uft-8'
soup = BeautifulSoup(res.text, "html5lib")
firstname = soup.find_all('input', class_="color1")

w1 = '"/>'

w2 = 'value="'

pat = re.compile(w2 + '(.*?)' + w1, re.S)
info = pat.findall(str(firstname))
firstname2 = info[1]

# 获取lastname
res = requests.get('http://www.shenfendaquan.com/', headers=headers)
res.encoding = 'uft-8'
soup = BeautifulSoup(res.text, "html5lib")
lastname = soup.find_all('input', class_="color2")

w1 = '"/>'

w2 = 'value="'

pat = re.compile(w2 + '(.*?)' + w1, re.S)
info = pat.findall(str(lastname))
lastname2 = info[1]

path = os.path.abspath('.')
# 设置不输出日志
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument('--headless')
# 打开谷歌浏览器
driver = webdriver.Chrome(executable_path='D:/chromedriver.exe', options=option)


def clearcookies():
    if clearcookie == 'y':
        driver.delete_all_cookies()
        print('清理完毕')
    else:
        pass


def getmyip():
    r = requests.get('http://23.80.5.90/ip.php', headers=headers)
    r.encoding = 'uft-8'
    soup = BeautifulSoup(r.text, "html5lib")
    ip = soup.find_all('body')
    ip1 = '>'

    ip2 = '\n'
    pat = re.compile(ip1 + '(.*?)' + ip2, re.S)
    info = pat.findall(str(ip))
    nowip = info[0]
    print('当前ip：' + nowip)
    print('Firstname：' + firstname2)
    print('Lastname：' + lastname2)


def getloginpge():
    # 打开商店页面
    driver.get('https://www.origin.com/usa/en-us/store')
    try:
        time.sleep(7)
        driver.find_element_by_xpath('//*[@id="shell"]/section/div/nav/div/div[1]/div[2]').click()
        time.sleep(1)
        # 点击弹出左边栏
        driver.find_element_by_xpath(
            '//*[@id="shell"]/section/div/nav/div/div[5]/ul/li[1]/origin-cta-login/origin-cta-primary/div/a/div').click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        newurl = driver.current_url
        with open('newurl.json', 'w') as f:
            f.write(newurl)  # 文件的写操作
        driver.close()
    except:
        time.sleep(7)
        # 点击弹出左边栏
        driver.find_element_by_xpath(
            '//*[@id="shell"]/section/div/nav/div/div[5]/ul/li[1]/origin-cta-login/origin-cta-primary/div/a/div').click()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        newurl = driver.current_url
        with open('newurl.json', 'w') as f:
            f.write(newurl)  # 文件的写操作
        driver.close()


def loginpage():
    driver.switch_to.window(driver.window_handles[0])
    with open('newurl.json', 'r') as f:
        newurl = f.read()  # 文件的写操作
    driver.get(str(newurl))
    time.sleep(3)
    # 输入firstname
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    time.sleep(1)
    # 输入lastname
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    time.sleep(1)
    # 点击开始
    driver.find_element_by_xpath('//*[@id="logInBtn"]').click()
    time.sleep(5)


def getprofile():
    driver.get("https://myaccount.ea.com/cp-ui/aboutme/index")
    html = driver.page_source
    bsoup = BeautifulSoup(html, "lxml")
    country = bsoup.find_all('dd', id="rs_country")
    phone = bsoup.find_all('dd', id="pn_phoneNumber")
    birthday = bsoup.find_all('div', class_="origin-ux-drop-down-selection")
    # 获取前半段关键词
    w1 = '">'
    # 获取后半段关键词
    w2 = '</dd>'

    b1 = '>'
    b2 = '<'
    b_pat = re.compile(b1 + '(.*?)' + b2, re.S)
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    pat_birthday = b_pat.findall(str(birthday))
    pat_country = pat.findall(str(country))
    info_country = pat_country[0]
    if comfirmbirthday == 'y':
        dd_birthday = pat_birthday[1]
        mm_birthday = pat_birthday[71]
        yy_birthday = pat_birthday[103]
        print('生日：' + mm_birthday + ' /', dd_birthday + ' /', yy_birthday)
    else:
        pass
    print('国家：' + info_country)
    try:
        pat_phone = pat.findall(str(phone))
        info_phone = pat_phone[0]
        print('手机：' + info_phone)
    except:
        print('手机：无')


'''
    with open('country.json', 'w') as f:
        f.write(str(pat_country))  # 文件的写操作

    with open('phone.json', 'w') as f:
        f.write(str(pat_phone))
'''


def getcreditcard():
    driver.get('https://myaccount.ea.com/cp-ui/paymentandshipping/index')
    html = driver.page_source
    bsoup = BeautifulSoup(html, "lxml")
    creditcard = bsoup.find_all('label', id="payment_1_displayinfo")
    # 获取前半段关键词
    w1 = '">'
    # 获取后半段关键词
    w2 = '</label>'
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    try:
        pat_credit = pat.findall(str(creditcard))
        info_credit = pat_credit[0]
        print('信用卡：' + info_credit)
    except:
        print('信用卡：无')


'''
    with open('creditcard.json', 'w') as f:
        f.write(str(pat_credit))
'''


def getconnections():
    driver.get('https://myaccount.ea.com/cp-ui/connectaccounts/index')
    time.sleep(5)
    html = driver.page_source
    bsoup = BeautifulSoup(html, "lxml")
    connections = bsoup.find_all('span', class_="platform_name")
    displayname = bsoup.find_all('div', class_="displayname")
    # 获取前半段关键词
    w1 = '">'
    # 获取后半段关键词
    w2 = '<'
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    pat_connections = pat.findall(str(connections))
    pat_displayname = pat.findall(str(displayname))
    print('平台名称：' + str(pat_connections))
    print('平台ID：' + str(pat_displayname))


def getorder():
    driver.get('https://myaccount.ea.com/cp-ui/orderhistory/index')
    # 选择已完成
    driver.find_element_by_xpath('//*[@id="category-dropdown"]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="category-dropdown"]/div[2]/div/div/div[1]/div[4]/a/span').click()
    # 选择全部时间
    driver.find_element_by_xpath('//*[@id="customdate-dropdown"]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="customdate-dropdown"]/div[2]/div/div/div[5]/a/span').click()
    time.sleep(5)
    html = driver.page_source
    bsoup = BeautifulSoup(html, "lxml")
    ordertime = bsoup.find_all('dd', class_="date")
    description = bsoup.find_all('dd', class_="des")
    price = bsoup.find_all('dd', class_="price color_orange")
    # 获取前半段关键词
    w1 = '<span>'
    # 获取后半段关键词
    w2 = '</span>'
    # 获取前半段关键词
    price1 = '>'
    # 获取后半段关键词
    price2 = '<'
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    price_pat = re.compile(price1 + '(.*?)' + price2, re.S)
    pat_ordertime = pat.findall(str(ordertime))
    pat_description = pat.findall(str(description))
    pat_price = price_pat.findall(str(price))
    info_ordertime = pat_ordertime[1]
    info_description = pat_description[0]
    info_price = pat_price[0]
    print('订单名称：' + info_description)
    print('订单时间：' + info_ordertime)
    print('订单金额：' + info_price)
    '''try:
        pat_ordertime = pat.findall(str(ordertime))
        pat_description = pat.findall(str(description))
        info_ordertime = pat_ordertime[5]
        info_description = pat_description[4]
        print('订单时间：' + info_ordertime)
        print('订单名称：' + info_description)
    except:
        print('订单时间：无')
        print('订单名称：无')'''

    '''with open('ordertime.json', 'w') as f:
        f.write(str(pat_ordertime))

    with open('description.json', 'w') as f:
        f.write(str(pat_description),encoding='utf-8')'''


def autosupport():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # 打开谷歌浏览器
    driver = webdriver.Chrome(executable_path='D:/chromedriver.exe', options=option)
    if translate == 'y':
        newwindow = 'window.open("https://translate.google.com/")'
        driver.execute_script(newwindow)
        driver.switch_to.window(driver.window_handles[0])
    else:
        newwindow = 'window.open("https://translate.google.cn/")'
        driver.execute_script(newwindow)
        driver.switch_to.window(driver.window_handles[0])
    # 生成邮箱
    number = random.randrange(0, 9999999999)
    email = str(number) + '@outlook.com'
    # 打开帮助网页
    driver.get(
        'https://help.ea.com/in/contact-us/new/?product=origin&platform=pc&category=manage-my-account&issue=cant-log-in&isLoginForm=true&isContactForm=true')
    time.sleep(8)
    try:
        # 点击同意条款
        driver.find_element_by_xpath('//*[@id="truste-consent-button"]').click()
        time.sleep(1)
        # 输入firstname
        driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(firstname2)
        time.sleep(1)
        # 输入lastname
        driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lastname2)
        time.sleep(1)
        # 输入邮箱
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # 点击开始
        driver.find_element_by_xpath(
            '//*[@id="id"]/div/div/ea-section/ea-section-column/div/form/ea-form-row[6]/ea-form-item/div/a[1]/div/span').click()
        time.sleep(5)
        # 输入subject
        driver.find_element_by_xpath(
            '//*[@id="step4"]/ea-section[2]/ea-section-column/div/div/div[2]/form/div/ea-form-row[2]/ea-form-item/div/input').send_keys(
            'I need Help')
        time.sleep(2)
        # 点击请求实时聊天
        driver.find_element_by_xpath('//*[@id="chatSubmit"]/div/span').click()
    except:
        # 输入firstname
        driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(firstname2)
        time.sleep(1)
        # 输入lastname
        driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lastname2)
        time.sleep(1)
        # 输入邮箱
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # 点击开始
        driver.find_element_by_xpath(
            '//*[@id="id"]/div/div/ea-section/ea-section-column/div/form/ea-form-row[6]/ea-form-item/div/a[1]/div/span').click()
        time.sleep(5)
        # 输入subject
        driver.find_element_by_xpath(
            '//*[@id="step4"]/ea-section[2]/ea-section-column/div/div/div[2]/form/div/ea-form-row[2]/ea-form-item/div/input').send_keys(
            'I need Help')
        time.sleep(2)
        # 点击请求实时聊天
        driver.find_element_by_xpath('//*[@id="chatSubmit"]/div/span').click()


def openwebsite():
    if translate == 'y':
        newwindow = 'window.open("https://translate.google.com/")'
        driver.execute_script(newwindow)
        driver.switch_to.window(driver.window_handles[0])
        print('Firstname：' + firstname2)
        print('Lastname：' + lastname2)
    else:
        newwindow = 'window.open("https://translate.google.cn/")'
        driver.execute_script(newwindow)
        driver.switch_to.window(driver.window_handles[0])
        print('Firstname：' + firstname2)
        print('Lastname：' + lastname2)


if __name__ == '__main__':
    '''clearcookies()
    opengoogletranslate()
    getmyip()
    getloginpge()
    time.sleep(1)
    loginpage()
    time.sleep(1)
    getprofile()
    time.sleep(1)
    getcreditcard()
    time.sleep(1)
    getconnections()
    time.sleep(1)
    getorder()
    time.sleep(1)
    getbirthday()
    time.sleep(1)
    autosupport()
    os.system("pause");'''
    try:
        getmyip()
        getloginpge()
        time.sleep(1)
        loginpage()
        time.sleep(1)
        getprofile()
        time.sleep(1)
        getcreditcard()
        time.sleep(1)
        getorder()
        time.sleep(1)
        getconnections()
        time.sleep(1)
        autosupport()
        os.system("pause")
    except:
        print('网络延迟过高,请选择离你位置近的商店地区')
        os.system("pause")
