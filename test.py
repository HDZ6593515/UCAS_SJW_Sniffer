
import pyshark
from collections import OrderedDict

if __name__ == '__main__':
    # 获取网络接口名称列表
    interface_names = pyshark.get_interface_names()

    # 打印网络接口名称
    for name in interface_names:
        print(f"Network Interface: {name}")