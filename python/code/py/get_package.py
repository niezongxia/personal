#!/usr/bin/env python
#coding:utf-8
import requests
import json
import zipfile
import os
import sys
import re
import time
import asyncio
import shutil
import datetime

#倒计时函数
def Windows_close(close_times):
    for x in range(close_times,-1,-1):
        mystr = "程序执行完毕！窗口将在" + str(x) + "秒后关闭！！！"
        print(mystr,end = "")
        print("\b" * (len(mystr)*2),end = "",flush=True)
        time.sleep(1)

def update_package(boot_url,timeout,home,packages,package_bak,package_zip):
    try:
        code = requests.get(boot_url,timeout=timeout).status_code
    except:
        code = 404
    if code == 200:
        print('正在备份package...')
        if os.path.exists(home):
            packages_path = [[home+i,package_bak+i] for i in packages]
            for package_path in packages_path:
                if os.path.exists(package_path[0]):
                    shutil.move(package_path[0],package_path[1])
                else:
                    continue
        print('正在获取package...')
        r = requests.get(boot_url)
        with open(package_zip,'wb') as code:
            code.write(r.content)
        with zipfile.ZipFile(package_zip) as azip:
            azip.extractall(home)
            print('正在解压package...')
        if os.path.exists(file_source) is False:
            os.mkdir(file_source)
        os.remove(package_zip)
    else:
        print('请检查网络或联系服务器管理员检查服务是否正常可用')


def host_port(host_list,port_list):
    for in_IP in host_list:
        IP = in_IP.replace('..','.')
        for port in port_list:
            for i in range(1,256):
                host = IP %(str(i))
                url_tup = (host,port)
                url_list.append(url_tup)
    
async def browser(host, port, semaphore):
    # 连接host
    async with semaphore:
        reader, writer = await asyncio.open_connection(host, port)
        print(host,port,'已被识别到！！！')
        boot_url = 'http://'+host+':'+str(port)+'/ewm/uploads/tools/package_local.zip'
        update_package(boot_url,timeout,home,packages,package_bak,package_zip)

def run(limit_num):
    semaphore = asyncio.Semaphore(limit_num) # 限制并发量
    loop = asyncio.get_event_loop()
    tasks = [browser(host, port, semaphore) for host,port in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()   

def get_time_stamp(ct):
    local_time = time.localtime(ct)
    time_stamp = "%s_%03d" % (time.strftime("%M:%S", local_time), (ct - int(ct)) * 1000)
    return time_stamp

if __name__ == '__main__':
    home = os.getcwd().replace('\\','/') + '/'#获取当前工作目录
    file_source = home + 'file_source'
    packages = ['install_book','model','creat_package.bat','creat_package.exe']
    dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+'/'
    package_bak = home + 'bak_package/'+dt
    package_zip = home + 'package_local.zip'
    timeout = 5
    url_list = []
    host_list = ['22.11.236.%s','22.11.235.%s']
    port_list = [89]
    host_port(host_list,port_list)
    start_time = time.time()
    run(509)
    end_time = time.time()
    td = get_time_stamp(end_time - start_time)
    print('更新已完成。')
    print('耗时：',td)
    Windows_close(60)
