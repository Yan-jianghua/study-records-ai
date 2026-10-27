# 开发环境

- 操作系统：Windows
- 终端：PowerShell
- Python版本：3.12.10

## 创建虚拟环境

在项目根目录执行：

```powershell
python -m venv .venv
```

## 编辑器解释器

PyCharm和VS Code使用同一个项目虚拟环境，解释器路径为：

```text
.venv\Scripts\python.exe
```

## 检查解释器版本

在项目根目录执行：

```powershell
.\.venv\Scripts\python.exe --version
```

预期输出：Python 3.12.10。

## 版本管理

.venv目录由.gitignore忽略，不提交到Git。
其他开发环境需要按上述步骤重新创建虚拟环境。