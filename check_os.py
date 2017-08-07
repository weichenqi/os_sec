#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2017-08-04 13:41 
# @Author  : George Wei (weichenqi@gmail.com)
# @Link    : http://weichenqi.com
# @Version : 0.2

'''
title：centos 7操作系统安全检查
1.操作系统版本
2.内核版本
3.yum最新安全更新
4.可登陆用户
5.可登陆且无密码用户
6.监听端口
7.防火墙是否启用
8.本机时间是否准确
9.ssh是否默认22端口
10.密码登录还是秘钥登录
11.是否允许root登录
12.selinux是否启用
13.密码过期时间
14.文件基线检测/etc/  6个bin目录
15.内核安全参数检测
16.开启启动任务检查
17.crontab任务检查
18.最近登录日志审计（最近一周登录的时间，源ip）
19.ipmi检查
'''

import subprocess, re, commands

def ShellCommand(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    line = popen.stdout.readline().strip()
    print line

ShellCommand('cat /etc/redhat-release ')
ShellCommand('uname -r')

(status, output) = commands.getstatusoutput('yum list-sec')
r = re.sub("Loaded plugins: fastestmirror", "", output)
s = re.sub("updateinfo list done", "", r)
print s

content = open('/etc/passwd').read()
reObj1 = re.compile('(\w+).*?/bin/bash')
s = reObj1.findall(content)
print s


ShellCommand('netstat -tunlp')