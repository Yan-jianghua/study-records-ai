# 学习记录管理器与 AI 助手

本地单用户应用，用于管理学习记录，并逐步加入 AI 问答和工具调用。

## 计划功能

- 学习记录的新增、查询、修改和删除
- 学习时长统计
- AI 知识点问答与问答保存
- 受控的只读工具调用

## 当前状态

已实现GET /health健康接口，返回{"status":"ok"}。
学习记录CRUD和AI功能仍在计划中。
已实现GET /info项目信息接口，返回项目名称。

## 安装依赖

先按照docs/dev-setup.md创建虚拟环境，再在项目根目录执行：

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 启动服务

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

健康接口：http://127.0.0.1:8000/health
接口文档：http://127.0.0.1:8000/docs
项目信息：http://127.0.0.1:8000/info

## 运行测试

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```