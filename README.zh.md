# 📝 FastAPI JournalBlog

一个基于 FastAPI 框架构建的轻量级博客系统，支持用户注册、登录、文章创建、修改和删除等核心功能。适合作为学习 FastAPI、JWT 认证、SQLAlchemy ORM 的实践项目。

---

## 🚀 项目特性

- ✨ 使用 FastAPI 构建异步高性能 RESTful API
- 🧱 SQLAlchemy 作为 ORM 处理数据库交互
- 🔐 集成 JWT（Json Web Token）身份认证机制
- 🧪 结构清晰，便于扩展与测试
- 📄 自动生成 API 文档（Swagger UI & Redoc）

---

## 📦 技术栈

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- JWT

---

## 📁 项目结构

```text
fastapi_journalblog/
├── app/
│   ├── __init__.py
│   ├── main.py              # 项目入口，FastAPI 实例定义
│   ├── models/              # SQLAlchemy 模型
│   ├── routers/             # 路由模块（如用户、文章等）
│   ├── schemas/             # Pydantic 数据校验模型
│   └── services/            # 业务逻辑封装
├── tests/                   # 单元测试目录
├── requirements.txt         # 项目依赖
└── README.md                # 项目说明文件
