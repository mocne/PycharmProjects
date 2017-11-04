# -*- coding: utf-8 -*-

from appium import webdriver
import time
import xlrd
import paramiko

desired_caps = {'platformName': 'Android',
                'platformVersion': '5.1.1',
                'deviceName': '127.0.0.1:21503',
                'appPackage': 'cn.phaidai.loan',
                'appActivity': 'com.rd.zdbao.adwjk.activity.SplashActivity',
                'noReset': True
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def start_to_register(filename):
    global registerData
    print('jump to register')
    time.sleep(3)
    try:
        driver.find_element_by_id('cn.phaidai.loan:id/rb_mine')
        print('id')
    except:
        try:
            driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
        except:
            return 'can not jump to mine'
        else:
            driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
            print('text')
    else:
        driver.find_element_by_id('cn.phaidai.loan:id/rb_mine').click()

    print(filename)
    userData = xlrd.open_workbook(r'%s' % filename)
    print('open user file success')

    registerSheet = userData.sheet_by_name('register')


    registerUsername = str(registerSheet.cell_value(1, 0))
    registerPassword = str(registerSheet.cell_value(1, 1))

    print(registerUsername.split('.')[0], registerPassword)

    currentAC = driver.current_activity

    try:
        driver.find_element_by_id('cn.phaidai.loan:id/tv_click')
    except:
        try:
            driver.find_element_by_id('cn.phaidai.loan:id/iv_avatar')
        except:
            return 'can not check status'
        else:
            driver.find_element_by_id('cn.phaidai.loan:id/iv_avatar').click()
    else:
        driver.find_element_by_id('cn.phaidai.loan:id/tv_click').click()
        try:
            driver.find_element_by_id('cn.phaidai.loan:id/tv_login_registered')
        except:
            return 'can not click to register'
        else:
            driver.find_element_by_id('cn.phaidai.loan:id/tv_login_registered').click()
    finally:
        if driver.current_activity == currentAC:
            return 'can not jump to register page'

    time.sleep(1)
    try:
        driver.find_element_by_id('cn.phaidai.loan:id/et_register_phone')
    except:
        return 'can not input phoneNumber'
    else:
        driver.find_element_by_id('cn.phaidai.loan:id/et_register_phone').send_keys(registerUsername.split('.')[0])
        try:
            driver.find_element_by_id('cn.phaidai.loan:id/et_register_password')
        except:
            return 'can not input password'
        else:
            driver.find_element_by_id('cn.phaidai.loan:id/et_register_password').send_keys(registerPassword)
    finally:
        username = driver.find_element_by_id('cn.phaidai.loan:id/et_register_phone')
        password = driver.find_element_by_id('cn.phaidai.loan:id/et_register_password')
        if username == '您的手机号' or password == '':
            return 'username or password is not input'
        else:
            driver.find_element_by_id('cn.phaidai.loan:id/bt_register_into').click()

            #***********************************************************************

            # SSH远程连接
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect("192.168.18.197", port=22, username="u1", password="admin123")
            # 待执行的命令
            swithch_path = "cd /usr/local/web/tomcat-2/logs"
            search_contents = "grep \'\"username\"\:\"\"\,\"phone\"\:\"18244440000\"\' catalina.out | tail -n 1"
            # 注意：依次执行多条命令时，命令之间用分号隔开
            command = swithch_path + ";" + search_contents
            # 执行命令
            stdin, stdout, stderr = ssh.exec_command(command)
            err = stderr.readlines()
            # out = stdout.readlines()
            if len(err) != 0:
                print("==execute command[", command, "] failed: ", err)
            else:
                print("==execute command[", command, "] success: ", out)
            ssh.close()

            #***********************************************************************

            # client = ssh.SSHClient()
            # client.set_missing_host_key_policy(ssh.AutoAddPolicy())
            # client.connect("192.168.18.197", port=22, username="u1", password="admin123")
            # stdin, stdout, stderr = client.exec_command("grep \'\"username\"\:\"\"\,\"phone\"\:\"18244440000\"\' /usr/local/web/tomcat-2/logs/catalina.out | tail -n 1")
            a = stdout.read()
            nPos = a.index('"code":"')
            phoneCode = a[nPos + 8:nPos + 14]

            driver.find_element_by_id('cn.phaidai.loan:id/et_register_authcode').send_keys(phoneCode)
            driver.find_element_by_id('cn.phaidai.loan:id/bt_register_submit').click()

            driver.find_element_by_id('cn.phaidai.loan:id/iv_cancel').click()
            return 'success'
