import requests
import random
import telnetlib
import threading
import time

#浏览器请求头，用于请求访问
user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
	"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]


#多线程锁
lock=threading.Lock()

#arr是被分割的list，n是每个chunk中含n元素。
def chunks(arr, n):
    return [arr[i:i+n] for i in range(0, len(arr), n)]



class Ip:
    #构造方法
    def __init__(self, proxy_type):
        #初始化电光代理API（JSON格式） #此API仅为测试链接，需要输入实际有效API
        self.api_json = 'https://api.super.xyz/oNtl30618YdXol/1000-china-0-http-high_anonymous-json'
        self.ips = [] #储存有效ip的列表
        self.proxy_type = proxy_type #代理类型

    #抓取并测试ip的方法
    def get_api(self):
        temporary = requests.get(self.api_json).json()['proxy'] #获取API的ip
        proxy_lists = chunks(temporary, 20) #将大列表分成小列表，每个列表含20个元素

        #多线程检测ip
        print('正在检测代理')
        ts = [] #新建列表，用于存放所有线程
        for proxy_list in proxy_lists: #遍历每个ip列表
            t = threading.Thread(target=self.test, args=(proxy_list,)) #创建线程
            t.start() #线程运行
            ts.append(t) #将线程添加到ts

        #等待线程结束
        for t in ts: #遍历每个线程
            t.join() #等待线程结束

        print('代理检测结束，检测总数:' + str(len(temporary)) + ',有效数量:' + str(len(self.ips)))

    #ip测试方法
    def test(self, proxy_list):
        #检测有效的ip
        for ip in proxy_list: #遍历每个ip
            address, port = ip.split(':') #分割ip和端口

            try:
                telnetlib.Telnet(address,port,timeout=0.4) #检测代理ip是否有效，0.4秒超时
                print("\033[32m" + str(ip) + "\033[0m") #输出绿色字体 #仅Linux有效
                self.ips.append(ip) #添加到列表  

            except:
                print("\033[31m" + str(ip) + "\033[0m") #输出红色字体 #仅Linux有效





    #多线程运行select_ip_imformation 方法
    def select_start(self):
        ts = [] #新建列表，用于存放所有线程
        for i in range(30): #随机查询30个ip
            t = threading.Thread(target=self.select_ip_imformation, args=()) #创建线程
            t.start() #线程运行
            ts.append(t) #将线程添加到ts

        #等待线程结束
        for t in ts: #遍历每个线程
            t.join() #等待线程结束

        print('ip查询结束')

                


    #查询代理ip的地址 方法
    def select_ip_imformation(self):
        ip = random.choice(self.ips) #随机选取一个ip

        #输出查询的ip信息，并删除超时ip
        #proxies为代理ip, headers为随机请求头， timeout超时时间为10秒
        try:
            r = requests.get("http://ip-api.com/json/?lang=zh-CN", 
            proxies = { self.proxy_type : self.proxy_type + '://' + ip }, 
            headers = {'User-Agent': random.choice(user_agent)}, timeout = 10  )      
        except Exception as e:
            r = str(e)
            pass
        
        #输出 查询到的ip信息 和 查询失败的信息
        if hasattr(r, 'status_code') and r.status_code == 200: #如果 r对象中有status_code 且 返回200
            try: #检测r是否有json
                print("\033[32m" + ' ' + str(ip) + ' ' + str(r.json()) + ' ' + str(r) + "\033[0m") #输出绿色字体 #仅Linux有效
            except: #如果没有返回json
                print("\033[31m" + ' ' + str(ip) + ' ' + str(r) + "\033[0m") #输出红色字体 #仅Linux有效
                pass

        else: #如果查询失败
            print("\033[31m" + ' ' + str(ip) + ' ' + str(r) + "\033[0m") #输出红色字体 #仅Linux有效



def main():
    print('代理API返回类型')
    print('1.http')
    print('2.https')
    in_ = input('请输入序号选择API返回的代理类型:')

    if in_ == '1':
        proxy_type = 'http'
    elif in_ == '2':
        proxy_type = 'https'
    else:
        print('您的输入有误')
        return main()
    
    ip = Ip(proxy_type) #创建ip实例
    ip.get_api() #获取 并 多线程检测ip
    ip.select_start() #多线程查询ip地址

    


if __name__ == '__main__':
    main()
        
### 电光笔记 https://cyberlight.xyz 
### 电光代理 https://cyberlight.xyz/ip
### Cyberbolt
