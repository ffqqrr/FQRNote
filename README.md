本项目受 <https://note.ms> 的启发，用 `django` 框架实现了类似功能的云剪贴板。

项目地址：<https://note.fqr-qwq.cn>

## 功能

- 访问 `网址/id`，即可跳转到 `id` 对应的剪贴板。可以在此界面查看和修改剪贴板的内容。
![image](https://github.com/user-attachments/assets/1e78cb5f-8529-4e08-b4f8-a4d1b840bac5)

- 访问 `网址/backend/list`，可以查看剪贴板的列表。
![image](https://github.com/user-attachments/assets/2204c512-1cd3-4468-a1dd-0dd836e62c7a)

## 快速开始

环境：Python。

- 安装 `django`
```
pip install django
```

- 配置数据库
```
python manage.py makemigrations
python manage.py migrate
```

- 运行项目
```
python manage.py runserver 端口号
```

即可在本地的指定端口号运行该项目。
