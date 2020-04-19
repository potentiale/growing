# Python端口扫描器

## 实现思路

```
1、一次完整的TCP握手作为TCP端口是否开放的判断依据。
2、输入：给定一个IP和端口列表进行判断端口是否开放。输出：开放的端口列表。
3、利用多线程实现高性能扫描，利用信号量防止线程冲突导致打印结果混乱。
```

## 主要内容

```python
# 调用模块
import optparse # 解析命令行参数选项
import socket  # Tcp连接
from threading import Thread # 线程处理
# 处理函数
def connectport(Host,Port) # 端口建立连接
def scanport(Host,Ports) # 扫描主机的端口列表
# 线程处理
for Port in Ports:
  t = Thread(target=connectport, args=(Host,int(Port)))
  t.start()
```

## Nmap工具

```python
# 主要调用模块
import nmap  # python-nmap是一个帮助使用nmap端口扫描器的python库。
# 操纵nmap扫描,为需要自动完成扫描任务的系统管理员提供的工具并报告。
# 支持nmap脚本输出。

import optparse
from threading import *
from socket import *

# main函数
def nmapScan(tHost,tPort):
def main():
```

