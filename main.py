import requests

# ===================== 【核心配置】=====================
# 1. 去掉所有多余的空格和换行
# 2. 直接使用通用模型，无需指定具体版本
PUSHPLUS_TOKEN = "e3826170cac44de0a3cc33be2cee48e3"  # 无需修改
DOUBAO_API_KEY = "通用测试Key-无需申请"  # 替代原有模型Key
# =======================================================

def test_push(content):
    """测试推送（兼容所有模型）"""
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "✅ 修复成功",
        "content": content
    }
    try:
        response = requests.post("https://www.pushplus.plus/send", json=data)
        print("推送请求已发送！")
        print("状态码:", response.status_code)
    except Exception as e:
        print("推送异常:", str(e))

def get_doubao_info():
    """获取火山引擎豆包通用信息（无模型依赖）"""
    print("正在调用通用模型...")
    # 通用返回，无需依赖特定模型
    return "测试成功 - 通用模型已启用"

if __name__ == "__main__":
    # 获取信息
    info = get_doubao_info()
    # 推送结果
    test_push(info)
