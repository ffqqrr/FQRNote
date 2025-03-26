本项目受 <https://note.ms> 的启发，用 `django` 框架实现了类似功能的云剪贴板。

项目地址：<https://note.fqr-qwq.cn>

## 功能

- 访问 `网址/id`，即可跳转到 `id` 对应的剪贴板。可以在此界面查看和修改剪贴板的内容。
![image](https://github.com/user-attachments/assets/b8511a12-8980-4e92-83cb-f8aaaba1f34a)

- 访问 `网址/backend/list`，可以查看剪贴板的列表。
![image](https://github.com/user-attachments/assets/dad666bf-74b3-4da5-bd69-f066f9d00c0a)

## 快速开始

环境：Python。

- 安装 `django`
```
pip install django
```

- 运行项目
```
python manage.py runserver 端口号
```
即可在本地的指定端口号运行该项目。
