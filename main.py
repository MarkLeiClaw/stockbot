import requests

# ===================== 【你的配置】 =====================
PUSHPLUS_TOKEN = "e3826170cac44de0a3cc33be2cee48e3"
# 🔥 关键修复：去掉 API Key 末尾的所有空格！！！
DOUBAO_API_KEY = "f0b4eaf8-5f15-4614-8c59-d041814a3cd4"  # 已删除末尾空格
# =======================================================

def test_push(content):
    """测试微信推送"""
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "✅ 情报测试成功",
        "content": content
    }
    try:
        response = requests.post("https://www.pushplus.plus/send", json=data)
        print("推送请求已发送")
        print("状态码:", response.status_code)
    except Exception as e:
        print("推送异常:", str(e))

def get_stock_info():
    """调用豆包AI获取情报"""
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    headers = {
        "Authorization": f"Bearer {DOUBAO_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "douban-seed-2.0-pro",
        "messages": [
            {
                "role": "user",
                "content": "请给我发送一条测试消息，内容只需要写：测试成功，无需其他内容。"
            }
        ],
        "temperature": 0.5
    }
    
    try:
        print("正在调用火山引擎豆包...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        res = response.json()
        # 解析返回内容
        ai_content = res["choices"][0]["message"]["content"]
        print("AI返回内容:", ai_content)
        return ai_content
    except Exception as e:
        error_msg = f"AI调用失败: {str(e)}"
        print(error_msg)
        return error_msg

if __name__ == "__main__":
    # 1. 获取AI信息
    info = get_stock_info()
    # 2. 推送给微信
    test_push(info)
