# Django 博客系统

## 📋 项目概述

本项目是一个基于 Django 框架开发的完整博客系统，实现了用户认证、文章发布与编辑、权限控制和后台管理等功能，符合数据结构课程 19-1 与 19-5 项目要求，并在系统设计中体现了树形数据结构的应用思想。

---

## 🎯 项目功能

### 用户认证系统
- 用户登录 / 退出
- 会话状态管理
- 权限验证机制

### 博客文章管理
- 发布与编辑文章
- 按时间倒序显示文章
- 文章内容详情展示

### 权限控制系统
- 所有文章对访客公开可读
- 仅登录用户可发布文章
- 仅作者可编辑自己的文章

### 管理员后台
- 用户管理
- 文章管理
- 权限分配

---

## 📁 项目结构

MyBlog/
├── Blog/                      # Django 项目配置
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── blogs/                     # 博客应用
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── blogs/
│           ├── base.html
│           ├── home.html
│           ├── login.html
│           ├── new_post.html
│           └── edit_post.html
└── manage.py

---

## 🚀 快速开始

### 环境要求
- Python 3.9+
- Django 6.0
- Pillow

### 安装步骤

1. 克隆项目
git clone <项目地址>
cd MyBlog/Blog

2. 创建虚拟环境
conda create -n myproject python=3.9
conda activate myproject

3. 安装依赖
pip install django pillow

4. 数据库初始化
python manage.py makemigrations
python manage.py migrate

5. 创建超级用户
python manage.py createsuperuser

6. 启动服务器
python manage.py runserver

### 访问地址
- 前台首页：http://127.0.0.1:8000/
- 管理后台：http://127.0.0.1:8000/admin/

---

## 🔧 使用说明

### 普通用户
- 浏览首页文章
- 登录后发布新文章
- 编辑自己发布的文章
- 退出登录

### 管理员用户
- 登录后台管理系统
- 管理用户和文章
- 分配用户权限

### 访客用户
- 可查看所有文章
- 无法发布或编辑文章

---

## 🌳 树结构应用说明

### URL 路由树
/
├── admin/
├── login/
├── logout/
├── new/
└── edit/<id>/

### 模板继承树
base.html
├── home.html
├── login.html
├── new_post.html
└── edit_post.html

### 权限结构树
系统权限
├── 超级用户
├── 管理员
├── 注册用户
└── 访客

---

## 🧪 功能测试

### 未登录用户
- 查看文章：通过
- 写文章页面：重定向到登录页
- 编辑按钮：不可见

### 登录用户
- 发布文章：成功
- 编辑本人文章：成功
- 编辑他人文章：禁止

### 管理员
- 用户与文章管理：成功

---

## 📊 项目要求完成情况

### 19-1 要求
- 创建 Django 项目与 blogs 应用
- 创建 BlogPost 模型
- 使用 Admin 添加文章
- 实现文章新增与编辑功能

### 19-5 要求
- 文章关联用户（owner）
- 所有文章公开访问
- 编辑前进行权限校验

---

## 🔍 技术要点

- Django MVT 架构
- ORM 数据库操作
- ModelForm 表单验证
- Django 内置用户认证系统
- 视图函数与装饰器权限控制

---

## 🛠️ 常见问题

密码重置：
进入 Django shell 修改用户密码

数据库迁移失败：
重新执行 makemigrations 与 migrate

模板无法加载：
确认路径为 blogs/templates/blogs/

---

## 📝 开发记录

2025-12-28
- 完成项目环境搭建
- 实现博客核心功能
- 完成权限控制
- 完成功能测试
- 整理项目文档

---

## 👥 项目信息

开发者：林永源
学号：2024401014
学院：深圳大学人工智能学院

说明：
本项目为数据结构课程实验项目，展示了树结构在 Web 系统设计中的实际应用。
