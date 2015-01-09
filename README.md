# python

示例代码

    import os
    from ipip import IP
    from ipip import IPX

    IP.load(os.path.abspath("mydata4vipday2.dat"))
    print IP.find("118.28.8.8")

    IPX.load(os.path.abspath("mydata4vipday2.datx"))
    print IPX.find("118.28.8.8")


执行输出

    中国	天津	天津		鹏博士
    中国	天津	天津		鹏博士	39.128399	117.185112	Asia/Shanghai	UTC+8	120000


使用说明

	 IP[X].load 方法可以在应用程序入库加载库文件