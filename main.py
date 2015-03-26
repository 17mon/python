# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os

from ipip import IP
from ipip import IPX

IP.load(os.path.abspath("mydata4vipday2.dat"))
print IP.find("118.28.8.8")

IPX.load(os.path.abspath("mydata4vipday2.datx"))
print IPX.find("118.28.8.8")
