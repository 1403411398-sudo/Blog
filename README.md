
一个简洁现代的 Django 博客应用，支持用户认证和文章管理。

## ✨ 核心功能

### 🔐 用户认证
- 登录/退出系统
- 权限验证
- 会话管理

### 📝 文章管理
- 创建、编辑文章
- 文章列表展示
- 作者权限控制

### 🎨 现代化界面
- 响应式设计
- 卡片式布局
- 移动端适配

## 🚀 快速开始

### 环境要求
- Python 3.9+
- Django 6.0


## 🚀 快速开始

### 环境要求
- Python 3.9+
- Django 6.0
- Pillow

### 安装步骤

1. 克隆项目
git clone <https://github.com/1403411398-sudo/Blog>
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

## 使用说明

### 1. 访客用户（未登录）
- 可直接访问博客首页，浏览所有已发布的文章
- 无法进入文章发布页面
- 无法编辑任何博客文章

### 2. 注册 / 登录用户
- 使用系统提供的登录页面进行登录
- 登录成功后可进入文章发布页面
- 可以新建博客文章并提交发布
- 仅可编辑本人创建的博客文章
- 可通过退出按钮安全退出当前账号

### 3. 管理员用户
- 管理员通过 Django 后台系统登录
- 可查看和管理系统中的所有用户信息
- 可对博客文章进行统一管理和维护
- 负责系统运行与数据安全

### 4. 基本操作流程
1. 访客访问博客首页浏览文章内容  
2. 用户登录系统  
3. 登录后发布新的博客文章  
4. 作者可对已发布的文章进行编辑  
5. 操作完成后可退出登录
