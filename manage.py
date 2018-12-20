#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # 設置配置文件的路徑
    # 同时设置DJANGO_SETTINGS_MODULE环境变量为当前project的setting.py文件
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FasterRunner.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print(sys.argv)
    execute_from_command_line(sys.argv)
    # excute_from_command_line()函数会根据命令行参数解析出命令的名称，
    # 根据命令名称调用相应的Command执行命令。Command位于各个管理模块的commands模块下面。