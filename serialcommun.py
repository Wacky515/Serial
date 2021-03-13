# !/usr/bin/python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Name:        serialcommun.py
# Purpose:     In README.md
#
# Author:      Kilo11
#
# Created:     20/06/2016
# Last Change: 2021/03/13 20:16:37.
# Copyright:   (c) SkyDog 2016
# Licence:     SDS10010
# -----------------------------------------------------------------------------
""" シリアル通信 処理 """

# モジュールインポート
import sys
import importlib
import serialcommun as sc

# Python2 用設定
if sys.version_info.major == 2:
    # sysモジュール リロード
    importlib.reload(sys)
    # デフォルトの文字コード 出力
    sys.setdefaultencoding("utf-8")


class SerialCom:
    """ シリアル通信クラス """

    def __init__(self):
        pass

    def send_tsc(self, text, port_no):
        """ バーコードプリンタにテキストデータを送信 """
        # !!!: "port_no" はデバイスマネージャーで調べた
        # COM番号から1引いた値を指定する
        com = sc(port=port_no - 1,
                 baudrate=9600,
                 bytesize=8,
                 parity="N",
                 stopbits=1,
                 timeout=None,
                 xonxoff=0,
                 rtscts=0,
                 writeTimeout=None,
                 dsrdtr=None)

        print(">> Port: {}".format(com.portstr))
        com.write(" >> {}\r\n".format(text))
        com.close()

    def receive(self, port_no):
        """ シリアル通信のデータを受信 """
        com = sc(port_no - 1)

        print(">> Port: {}".format(com.portstr))
        while True:
            data = com.readline()
            char = data.decode("utf-8")
            print(char.strip())
        com.close()


def main():
    src = SerialCom()
    src.send_tsc("Test", 1)
    src.receive(2)


if __name__ == "__main__":
    main()
