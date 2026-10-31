from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
@app.get("/info")
def info() -> dict[str, str]:
    return {"name": "学习记录管理器与AI助手"}
