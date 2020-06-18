# proxy-test-for-requests
Python3使用Requests抓取和检测电光代理API,并查询ip代理是否成功

#使用方法（以没有安装Python3虚拟环境的Windows为例）

进入命令窗口

1.安装虚拟环境  pip install virtualenv(Linux和MacOS使用 pip3 install virtualenv)

2.在项目目录下创建虚拟环境 virtualenv venv

3.激活虚拟环境 venv\Scripts\activate(Linux和MacOS使用 . venv/bin/activate)

4.激活后安装所需依赖 pip install -r requirements.txt(Linux和MacOS使用 pip3 install -r requirements.txt)

5.编辑ip.py文件，将64行链接改为您获取的代理API地址（此处API为电光代理返回的JSON格式，如果您未修改代码，暂时只能用电光代理https://www.cyberlight.xyz/ip ）(如果您是开发者，代码可自行编辑，支持请求任何类型的API)

6.运行该程序即可 python ip.py(Linux和MacOS使用 python3 ip.py)

7.运行程序后，如果您的API设置返回http代理，请选择1，如果设置返回https代理，请选择2


源码来自电光笔记官网测试 https://www.cyberlight.xyz/
