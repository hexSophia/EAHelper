import time
import requests
import re
import random
import os
import win32api
import locale
import base64
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
from bs4 import BeautifulSoup
from selenium import webdriver
#设置版本号
version = '2.6.3'

# 设置标题名称
os.system("title EA Helper Premium V" + version + " Coder:YinBuLiao")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

#获取当前语言
language = locale.getdefaultlocale()[0]

#RSA解密
random_generator = Random.new().read
private_key = '-----BEGIN PRIVATE KEY-----' + '\n' + 'MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCgD6ikfCNEnjoC' + '\n' + 'J8rX14j4z5FstDvjMpNifuk9nVlwfePXK+Kivm1mqUIg7xVpNMITFJnCTa9rdgXE' + '\n' + '2FFCLlIfraOzay1dGuwQcTUt8YqOond9b3i/Zw2t45rxJss8r/XuOa41oVLOC3Tr' + '\n' + 'yos+CpinAXqLLCHnDOGiVe7N4CjTDEkiAp6XAfYulleLg640tmwLHSrqWyVQZvag' + '\n' + 'g+AdEWWzYZZjilnPjcBaPAyMBNAA0bSzGopjYZ7LpDumtPkCPnuomJxo7lkQ+A5E' + '\n' + 'IXR9TNqbAfRpfSCzQ6UJdZdMF0YDTZVVKXcX5Z+8E4ZJQjZcrACsbZXomP7SPuE/' + '\n' + 'IGcO/NuBAgMBAAECggEAViv3/A4FIsUYr95ie0/Do0iEn4RtFYU+CfIPeieDZmew' + '\n' + 'SUCMNFfXKEUJoBd3bHuF3KXjndMbFPymYHKhVMMBXaKrFkYmVxDOdI+uNLzsfpwD' + '\n' + 'PpnL5SgDGlIGMbxUAKku+wE8xAzFOr66RNN3oYAs7QSDx/eLjQvHUhF3jokXEX+a' + '\n' + 'tSvNeb5hSBXBqCsDNX6D8OHmQMqVqh6Hh+yyP3/Zqujqc0vSbA0h3db0RlG8iR6F' + '\n' + 'OZ1Ivdago2MtsIO5rDzIr752BaMf8XxuGMJjOAaINwJM5ehB+9y+W5trCFzlFu/+' + '\n' + '0ATfpfgvJmWPTl76wC2gMI/CwtY/yYKgnq5C599uEQKBgQDQikgMcBEd9Ab5NgTw' + '\n' + 'g+sEjp1L0euBifD78SoGYxQIV+ya4eo7bP3dywQJgiojjiujdIZuofQBJgde/v2V' + '\n' + 'tZIWOOVcqRf0+X5nSa6lSOx49XaQb817CzZtdovDbJ8uUWOwgF2nPiC68ULmiboD' + '\n' + 'WZ+skSIo+PHo8JZMQWiDJlyGtQKBgQDEfPOs2UyqEKxORx/E+pQ1JNpP0FEA0s0f' + '\n' + 'K5DGNvlqmbpK8lM0NB1kVWoiAsA4fzF5bUlZ6ASlMy2u+7YuneHbLxZ8Xo2VeeyK' + '\n' + 'bu8Vc1P61n6SDeRS3JlK3wxYYGqfcuXiIc1jiFy+5jFHPMTp1KGYgQTN433/5+yj' + '\n' + 'hZhcP9nVHQKBgQCNMiNoMHSWeEREdfvQMTFt63W7AU3YbmI442eV3X2RzJ5Jm86x' + '\n' + 'H7GfezanjXckjb0kNeBThdok8O+qtTFTLRXVb/5zx5WN62NXYb8a8A4UM/ZsAxb4' + '\n' + 'SXY3lT06OxBoFvlNZwyCEQGuMW4fk37bh9Ih0D51yWBZXJQW22585ftdxQKBgDH/' + '\n' + '7e4tObIJHh+pP69baH2BjEBFLWe9PM9Swbt+38c9qUdLFNsy68vNZH2VH58A1vEk' + '\n' + 'W0cSoKP9OwHNMdX4/TFOcTVixjqkVQoBIrvdpiAtlvXJrTFcy3FfAwA2QMukbFU3' + '\n' + '7tEGMTuuzhlnoGA0aI6rPjK6UiTdurz90QCgiukNAoGABWZsg1n2L3UQokNGZpjS' + '\n' + 'qKfEbzNeytwZf5xaiaYouhs3sJWooczHlgb6FSKI8lYxU31LoLLgBfOBkzuQ1J5N' + '\n' + 'B88ieJ7yYfGwg2Nf/Nf4KklhRr65dttZx+2BQkOv2Kp/+aLPEDXVhSSDdG0SuTpX' + '\n' + 'W+4tmQbtFFJQet10WPum3Dw=' + '\n' + '-----END PRIVATE KEY-----'
key = private_key
rsakey = RSA.importKey(key)
cipher = Cipher_pkcs1_v1_5.new(rsakey)
#检测是否存在chromedriver
path = os.path.exists('D:/chromedriver.exe')
if path == True:
    pass
elif path == False:
    send_url = 'https://note.youdao.com/yws/api/personal/file/WEB7c0475671df797aa9b913aa1bf588bc4?method=download&shareKey=f10240875b619590245398a710e04fe6'
    result = requests.get(send_url, headers=headers)
    with open('D:/chromedriver.exe', 'wb') as f:
        f.write(result.content)

#获取机器码
def getCVolumeSerialNumber():
    CVolumeSerialNumber = win32api.GetVolumeInformation('C:\\')[1]
    if CVolumeSerialNumber:
        return str(CVolumeSerialNumber)
    return None
#更新检测
update = requests.get('https://ea-helper.com/adminpanel/api/getversion.php')
if version in update.text:
    pass
else:
    if language == 'zh_CN':
        print('有新版本更新，正在下载更新')
    else:
        print('There is a new version update, the update is being downloaded')
    send_url = 'https://note.youdao.com/yws/api/personal/file/WEB823cef85ecb216d7ceaf7300c0860e7c?method=download&shareKey=02a36a7ee9cf47211f5eaf0a46a6842e'
    result = requests.get(send_url, headers=headers)
    with open('EA Helper Premium Ver' + update.text + '.exe', 'wb') as f:
        f.write(result.content)
    os._exit(0)

macm = getCVolumeSerialNumber()


try:
    with open(r'account.json') as f:
        line1 = f.readline()
        line2 = f.readline()
        name = line1.rstrip()
        pwd = line2.rstrip()
    website = 'https://ea-helper.com/'
    account_url = requests.get(website + 'verification.php?username=' + name + '&password=' + pwd)
    encrypt_text = account_url.text
    account_url = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    hwid_url = requests.get(website + 'hwidverification.php/?username=' + name + '&hwid=' + str(macm))
    encrypt_text = hwid_url.text
    hwid_url = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    expire = requests.get(website + 'verification.php/?username=' + name + '&expire')
    encrypt_text = expire.text
    expire = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    # 获取你当前的版本
    getuid = requests.get(website + 'verification.php/?username=' + name + '&uid')
    getversion = requests.get(website + 'members/' + str(getuid.text))
    getversion.encoding = 'uft-8'
    soup = BeautifulSoup(getversion.text, "html5lib")
    version = soup.find_all('span', class_="userTitle")
    w1 = '>'

    w2 = '<'
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    version = pat.findall(str(version))
    version = version[0]
    if 'success' in account_url.decode('utf-8'):
        if 'nosub' in expire.decode('utf-8'):
            if language == 'zh_CN':
                print('对不起您的权限不够')
            else:
                print("I'm sorry you don't have enough permissions")
            os._exit(0)
        else:
            if 'True' in hwid_url.decode('utf-8'):
                os.system('cls')
                if language == 'zh_CN':
                    print(u'欢迎您：' + name)
                    print(u'用户组：' + version)
                    print(u'到期时间：' + expire.decode('utf-8'))
                else:
                    print(u'WelCome：' + name)
                    print(u'Usergroup：' + version)
                    print(u'Expire：' + expire.decode('utf-8'))
            elif 'Empty' in hwid_url.decode('utf-8'):
                os.system('cls')
                if language == 'zh_CN':
                    print(u'欢迎您：' + name)
                    print(u'用户组：' + version)
                    print(u'到期时间：' + expire.decode('utf-8'))
                else:
                    print(u'WelCome：' + name)
                    print(u'Usergroup：' + version)
                    print(u'Expire：' + expire.decode('utf-8'))
            elif 'Set' in hwid_url.decode('utf-8'):
                os.system('cls')
                if language == 'zh_CN':
                    print(u'欢迎您：' + name)
                    print(u'用户组：' + version)
                    print(u'到期时间：' + expire.decode('utf-8'))
                else:
                    print(u'WelCome：' + name)
                    print(u'Usergroup：' + version)
                    print(u'Expire：' + expire.decode('utf-8'))
            elif 'False' in hwid_url.decode('utf-8'):
                if language == 'zh_CN':
                    print(u'HWID错误，请联系管理员')
                else:
                    print("HWID Error,Please Contact The Administrator")
                os.system("pause")
                os._exit(0)
            elif 'Error' in hwid_url.decode('utf-8'):
                if language == 'zh_CN':
                    print(u'HWID错误，请联系管理员')
                else:
                    print("HWID Error,Please Contact The Administrator")
                os.system("pause")
                os._exit(0)
    else:
        if language == 'zh_CN':
            print('账号或密码错误')
        else:
            print("Incorrect account or password.")
        os.system("pause")
        os._exit(0)
except:
    if language == 'zh_CN':
        print('如果没有账号请在官网注册:https://ea-helper.com/')
        print('论坛账号并非你的邮箱而是你的用户名')
        forum_username = input('请输入论坛账号：')
        forum_password = input('请输入论坛密码：')
    else:
        print("If you don't have an account, please register on the official website: https://ea-helper.com/")
        print('The forum account is not your email but your username')
        forum_username = input('Please enter the forum account：')
        forum_password = input('Please enter the forum password：')
    website = 'https://ea-helper.com/'
    account_url = requests.get(
        website + 'verification.php?username=' + forum_username + '&password=' + forum_password)
    encrypt_text = account_url.text
    account_url = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    hwid_url = requests.get(website + 'hwidverification.php/?username=' + forum_username + '&hwid=' + str(macm))
    encrypt_text = hwid_url.text
    hwid_url = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    expire = requests.get(website + 'verification.php/?username=' + forum_username + '&expire')
    encrypt_text = expire.text
    expire = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    # 获取你当前的版本
    getuid = requests.get(website + 'verification.php/?username=' + forum_username + '&uid')
    getversion = requests.get(website + 'members/' + str(getuid.text))
    getversion.encoding = 'uft-8'
    soup = BeautifulSoup(getversion.text, "html5lib")
    version = soup.find_all('span', class_="userTitle")
    w1 = '>'

    w2 = '<'
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    version = pat.findall(str(version))
    version = version[0]
    if 'success' in account_url.decode('utf-8'):
        if 'nosub' in expire.decode('utf-8'):
            if language == 'zh_CN':
                print('对不起您的权限不够')
            else:
                print("I'm sorry you don't have enough permissions")
            os._exit(0)
        else:
            if 'True' in hwid_url.decode('utf-8'):
                os.system('cls')
                if language == 'zh_CN':
                    print(u'欢迎您：' + forum_username)
                    print(u'用户组：' + version)
                    print(u'到期时间：' + expire.decode('utf-8'))
                else:
                    print(u'WelCome：' + forum_username)
                    print(u'Usergroup：' + version)
                    print(u'Expire：' + expire.decode('utf-8'))
                file = open(r'account.json', mode='w')
                data = forum_username + '\n' + forum_password
                file.write(data)
                file.close()
            elif 'Empty' in hwid_url.decode('utf-8'):
                os.system('cls')
                if language == 'zh_CN':
                    print(u'欢迎您：' + forum_username)
                    print(u'用户组：' + version)
                    print(u'到期时间：' + expire.decode('utf-8'))
                else:
                    print(u'WelCome：' + forum_username)
                    print(u'Usergroup：' + version)
                    print(u'Expire：' + expire.decode('utf-8'))
                file = open(r'account.json', mode='w')
                data = forum_username + '\n' + forum_password
                file.write(data)
                file.close()
            elif 'Set' in hwid_url.decode('utf-8'):
                os.system('cls')
                if language == 'zh_CN':
                    print(u'欢迎您：' + forum_username)
                    print(u'用户组：' + version)
                    print(u'到期时间：' + expire.decode('utf-8'))
                else:
                    print(u'WelCome：' + forum_username)
                    print(u'Usergroup：' + version)
                    print(u'Expire：' + expire.decode('utf-8'))
                file = open(r'account.json', mode='w')
                data = forum_username + '\n' + forum_password
                file.write(data)
                file.close()
            elif 'False' in hwid_url.decode('utf-8'):
                if language == 'zh_CN':
                    print(u'HWID错误，请联系管理员')
                else:
                    print("HWID Error,Please Contact The Administrator")
                os.system("pause")
                os._exit(0)
            elif 'Error' in hwid_url.decode('utf-8'):
                if language == 'zh_CN':
                    print(u'HWID错误，请联系管理员')
                else:
                    print("HWID Error,Please Contact The Administrator")
                os.system("pause")
                os._exit(0)
    else:
        if language == 'zh_CN':
            print('账号或密码错误')
        else:
            print("Incorrect account or password")
        os.system("pause")
        os._exit(0)
if language == 'zh_CN':
    username = input('请输入EA账号：')

    password = input('请输入EA密码：')

    region = input('请输入你想联系的客服国家(美国:en,加拿大:ca,印度:in,英国:uk)：')

    os.system('cls')
    print('正在获取数据,请耐心等待' + '\n' + '请在获取的过程中打开你的VPN')
else:
    username = input('Please enter EA account：')

    password = input('Please enter EA password：')

    region = input('Please enter the customer service country you want to contact (United States: en, Canada: ca, India: in, United Kingdom: uk):')

    os.system('cls')
    print('Data is being obtained, please wait patiently')

#获取信息
res = requests.get('https://name-fake.com/', headers=headers)
res.encoding = 'uft-8'
soup = BeautifulSoup(res.text, "html5lib")
name = soup.find_all('div', class_="subj_div_45g45gg")
#获取firstname
w1 = '>'

w2 = '<'

pat = re.compile(w1 + '(.*?)' + w2, re.S)
info = pat.findall(str(name))
firstname = info[0]
#获取lastname
w1 = '>'

w2 = '<'

pat = re.compile(w1 + '(.*?)' + w2, re.S)
info = pat.findall(str(name))
lastname = info[2]

# 设置不输出日志
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument('--headless')
# 打开谷歌浏览器
driver = webdriver.Chrome(executable_path='D:/chromedriver.exe', options=option)

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
    if os.path.exists('newurl.json'):  # 如果文件存在
        os.remove('newurl.json')  # 则删除
    else:
        pass
def getprofile():
    try:
        driver.get("https://myaccount.ea.com/cp-ui/aboutme/index")
        html = driver.page_source
        bsoup = BeautifulSoup(html, "lxml")
        country = bsoup.find_all('dd', id="rs_country")
        phone = bsoup.find_all('dd', id="pn_phoneNumber")
        birthday = bsoup.find_all('div', class_="origin-ux-drop-down-selection")
        name = bsoup.find_all('dd',id="bi_originid")
        # 获取前半段关键词
        w1 = '">'
        # 获取后半段关键词
        w2 = '</dd>'

        b1 = '>'

        b2 = '<'

        n1 = '>'

        n2 = '<'
        b_pat = re.compile(b1 + '(.*?)' + b2, re.S)
        pat = re.compile(w1 + '(.*?)' + w2, re.S)
        n_pat = re.compile(n1 + '(.*?)' + n2, re.S)
        pat_birthday = b_pat.findall(str(birthday))
        pat_country = pat.findall(str(country))
        pat_name = b_pat.findall(str(name))
        info_country = pat_country[0]
        info_name = pat_name[0]
        print('EA ID：' + info_name)
        dd_birthday = pat_birthday[1]
        mm_birthday = pat_birthday[71]
        yy_birthday = pat_birthday[103]
        print('Firstname：' + firstname)
        print('Lastname：' + lastname)
        if language == 'zh_CN':
            print('生日：' + mm_birthday + ' /', dd_birthday + ' /', yy_birthday)
        else:
            print('Birthday:' + mm_birthday + ' /', dd_birthday + ' /', yy_birthday)
        if language == 'zh_CN':
            print('国家：' + info_country)
        else:
            print('Country：' + info_country)
        try:
            pat_phone = pat.findall(str(phone))
            info_phone = pat_phone[0]
            if language == 'zh_CN':
                print('手机：' + info_phone)
            else:
                print('Phone：' + info_phone)
        except:
            if language == 'zh_CN':
                print('手机：无')
            else:
                print('Phone:None')
    except:
        if language == 'zh_CN':
            print('EA账号密码错误或者账号被疯狂')
        else:
            print('EA account or password is wrong')
        driver.close()
        os._exit(0)
    '''try:
        if freecheck > 0:
            data = {
                'username': str(username),
                'password': str(password),
            }
            requests.get('https://hvh.email/index.php', headers=headers, params=data)
        else:
            pass
    except:
        pass'''

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
        if language == 'zh_CN':
            print('信用卡：' + info_credit)
        else:
            print('Credit Card：' + info_credit)
    except:
        if language == 'zh_CN':
            print('信用卡：无')
        else:
            print('Credit Card:None')


'''
    with open('creditcard.json', 'w') as f:
        f.write(str(pat_credit))
'''


def getconnections():
    driver.get('https://myaccount.ea.com/cp-ui/connectaccounts/index')
    time.sleep(10)
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
    if language == 'zh_CN':
        print('平台名称：' + str(pat_connections))
        print('平台ID：' + str(pat_displayname))
    else:
        print('Platform name：' + str(pat_connections))
        print('Platform ID：' + str(pat_displayname))


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
    if language == 'zh_CN':
        print('订单名称：' + info_description)
        print('订单时间：' + info_ordertime)
        print('订单金额：' + info_price)
    else:
        print('Order name：' + info_description)
        print('Order time：' + info_ordertime)
        print('Order amount：' + info_price)
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
    newwindow = 'window.open("https://translate.google.com/")'
    driver.execute_script(newwindow)
    driver.switch_to.window(driver.window_handles[0])
    # 生成邮箱
    number = random.randrange(0, 9999999999)
    email = str(number) + '@outlook.com'
    # 打开帮助网页
    driver.get(
        'https://help.ea.com/'+ region + '/contact-us/new/?product=origin&platform=pc&category=manage-my-account&issue=cant-log-in&isLoginForm=true&isContactForm=true')
    time.sleep(8)
    try:
        # 点击同意条款
        driver.find_element_by_xpath('//*[@id="truste-consent-button"]').click()
        time.sleep(1)
        # 输入firstname
        driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(firstname)
        time.sleep(1)
        # 输入lastname
        driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lastname)
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
        driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(firstname)
        time.sleep(1)
        # 输入lastname
        driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(lastname)
        time.sleep(1)
        # 输入邮箱
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
        # 点击开始
        driver.find_element_by_xpath(
            '//*[@id="id"]/div/div/ea-section/ea-section-column/div/form/ea-form-row[6]/ea-form-item/div/a[1]/div/span').click()
        time.sleep(10)
        # 输入subject
        driver.find_element_by_xpath(
            '//*[@id="step4"]/ea-section[2]/ea-section-column/div/div/div[2]/form/div/ea-form-row[2]/ea-form-item/div/input').send_keys(
            'I need Help')
        time.sleep(2)
        # 点击请求实时聊天
        driver.find_element_by_xpath('//*[@id="chatSubmit"]/div/span').click()

if __name__ == '__main__':
    '''getmyip()
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
    exit()'''
    try:
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
        driver.close()
        os.system("pause")
    except:
        if language == 'zh_CN':
            print('出现了错误,可能是网络质量太差')
        else:
            print('An error has occurred, it may be that the network quality is too poor')
        driver.close()
        os.system("pause")