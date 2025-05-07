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
│   ├── main.py
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   └── services/
├── tests/
├── requirements.txt
├── README.md
└── README.zh.md
