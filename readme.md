# 使用方法:
- 安装pipenv
- 使用pipenv安装虚拟环境
- 初始化数据库
- 运行flask
```bash
$ pip install pipenv 
$ pipenv install
$ pipenv shell
$ flask init_db
$ flask fake --count 20
$ falsk run
```

## 可选
- 创建.env文件
- 设置SECRET_KEY 和 DATABASE_URI
```.env
SECRET_KEY = 'secret-key'
DATABASE_URI = 'sqlite:///data.sqlite3'
```