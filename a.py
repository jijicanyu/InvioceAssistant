# -*- coding: cp936 -*-

import re
import os


raw_input("�뽫��Ҫ����� txt �ļ�������inputĿ¼��, ���»س�����ʼ�Զ�����..")
print "ע��:���԰汾�����������һλ�� * ������"
open("error.txt", "w").write("")

s = ""
for n in os.listdir("./input/"):
    fn = "./input/" + n
    t = open(fn).read()
    try:
        t = t.decode("utf8")[1:].encode("gbk", "replace")
    except:
        pass
    s += t + "\n"

snum = 0
enum = 0
outstr = ""
ss = s.split("���˻�ִ")
for s in ss:
    if len(s) < 100:
        continue
    s0 = s
    try:
        s = s.replace("\n", " ").replace("\r", " ").replace(":", "��").replace(" ", "")
        a1 = re.findall(r"�������ڣ�(.*?)�����ˮ", s)[0].strip()
        a2 = re.findall(r"�����кţ�(.*?)�տ����˺�", s)[0].strip()
        a3 = re.findall(r"����������(.*?)�����к�", s)[0].strip()
        a4 = re.findall(r"���������ƣ�(.*?)���ı��", s)[0].strip()
        a5 = re.findall(r"�������˺ţ�(.*?)�����˵�ַ", s)[0].strip()
        a6 = re.findall(r"�տ������ƣ�(.*?)����", s)[0].strip()
        a7 = re.findall(r"�տ����˺ţ�(.*?)�տ���", s)[0].strip()
        a8 = re.findall(r"ժҪ��(.*?)Ʊ������", s)[0].strip() + re.findall(r"���ԣ�(.*?)ժҪ", s)[0].strip()
        a9 = re.findall(r"��(.*?)����д", s)[0].replace(",", "").replace("��", "").replace("һ", "").replace("��", "").replace("_", ".").strip()
        a1 = a1.replace("��", ",").replace("��", ",").replace("��", ",")
        a1 = a1.split(",")
        a10 = a1[0].strip()
        a11 = a1[1].strip()
        a12 = a1[2].strip()
        a1 = a10 + a11.zfill(2) + a12.zfill(2)
        a1 = a1[:-1] + "*"
        a = "%s ~ %s ~ 00000000 ~ %s ~ %s ~ %s ~ %s ~ %s ~ %s ~ %s ~ %s ~ 00" % (
            a1, a1, a2, a3, a4, a5, a6, a7, a8, a9
            )
        print a
        outstr += a + "\n"
        snum += 1
    except:
        print "============== error ================="
        print s0
        print "======================================"
        open("error.txt", "a").write(s0 + "\n\n")
        enum += 1

open("output.txt", "w").write(outstr)

print "�ɹ����� %d ������, ʧ�� %d ��." % (snum, enum)
raw_input("���!��������� output.txt �ļ���, ���»س����˳�...")



