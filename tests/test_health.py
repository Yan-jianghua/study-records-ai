from fastapi.testclient import TestClient  # 导入测试客户端类，用来向应用发送测试请求
from app.main import app  # 导入app/main.py中创建的应用对象app

client = TestClient(app)  # 创建测试客户端，将请求交给这个应用处理


def test_health_returns_ok() -> None:  # 定义测试函数；test_前缀让pytest发现它，None表示不返回结果
    response = client.get("/health")  # 发送GET请求，将响应保存到本函数的局部变量response
    assert response.status_code == 200  # 检查响应状态码是否等于200，不相等则测试失败
    assert response.json() == {"status": "ok"}  # 将响应JSON解析成字典，检查其内容是否符合接口约定


def test_unknown_path_returns_404() -> None:  # 定义另一个测试，验证不存在的路径
    response = client.get("/not-a-route")  # 请求未定义的路径；这里的response属于这个函数
    assert response.status_code == 404  # 检查是否返回“找不到资源”的404状态码
    assert response.json() == {"detail": "Not Found"}  # 检查错误响应的具体内容
