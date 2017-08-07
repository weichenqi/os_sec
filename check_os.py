#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 2017-08-04 13:41 
# @Author  : George Wei (weichenqi@gmail.com)
# @Link    : http://weichenqi.com
# @Version : 0.2

'''
title：centos 7操作系统安全检查
base ：python 2.7
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
    return line

print "OS Release's version is:"
ShellCommand('cat /etc/redhat-release ')
print "OS kernel's version is:"
ShellCommand('uname -r')
(status, output) = commands.getstatusoutput('yum list kernel.x86_64 -q')
reObj1 = re.compile('kernel\.x86_64\s+(.*?)\s+updates')
s = reObj1.findall(output)[0]
print "The newest kernel version is----> "+str(s)

(status, output) = commands.getstatusoutput('yum list-sec -q')
print "The newest software sec update----> "+output

content = open('/etc/passwd').read()
reObj1 = re.compile('(\w+).*?/bin/bash')
s = reObj1.findall(content)
for i in range(len(s)):
    print "User's shell is /bin/bash with user: "+s[i]


(status, output) = commands.getstatusoutput('netstat -tunlp')
r = re.sub("Active Internet connections \(only servers\)", "", output)
s = re.sub("Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name ", "", r)
print "Listen Tcp and Udp port details: "+s
