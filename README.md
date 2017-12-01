# django

 搭建的内容大部分参考自实验楼，修改部分是网上各类教程；
 
 主体包括 nginx搭建django + bootstrap简单布置；前端太渣，只是套用而已，主要还是学习python，目前手机横屏才能完全适应。平板跟电脑倒还没什么问题

代码及教程全部都放这里了，没有域名备案，只是供学习参考： http://120.24.66.185:8082/
也可以参考源码myblog目录
# 简介
article目录是博客的主要内容：

[root@ali my_blog]# tree article
article
|-- admin.py
|-- apps.py
|-- blog.css
|-- __init__.py
|-- migrations
|   |-- 0001_initial.py
|   |-- __init__.py
|   `-- __pycache__
|       |-- 0001_initial.cpython-35.pyc
|       `-- __init__.cpython-35.pyc
|-- models.py
|-- __pycache__
|   |-- admin.cpython-35.pyc
|   |-- custom_markdown.cpython-35.pyc
|   |-- __init__.cpython-35.pyc
|   |-- models.cpython-35.pyc
|   `-- views.cpython-35.pyc
|-- templates
|   |-- index.html
|   |-- mybase.html
|   |-- myhome.html
|   |-- mypost.html
|   |-- oldhtml
|   |   |-- base.html
|   |   |-- base.html.bak
|   |   |-- home.html
|   |   |-- home.html.bak
|   |   `-- post.html
|   `-- oldhtml\344\270\272\344\273\245\345\211\215html\346\226\207\344\273\266_\345\267\262\345\272\237\345\274\203
|-- tests.py
`-- views.py
其他的是一开始学习的一些测试，代码可参考，login那里是模拟用户登录
