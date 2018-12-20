"""
WSGI config for FasterRunner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FasterRunner.settings')


application = get_wsgi_application()
print("======================= {}".format(type(application)))

#  <class 'django.core.handlers.wsgi.WSGIHandler'>
#在Web应用启动后，会生成一个 WSGIHandler 实例(根据setting中的
# WSGI_APPLICATION = ‘dailyblog.wsgi.application’ 调用函数）
# 每次请求响应都用这个实例。 settings 里设置了 WSGI application。 返回实例代码