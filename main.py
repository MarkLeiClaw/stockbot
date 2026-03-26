import requests

# ===================== 【你的配置】 =====================
PUSHPLUS_TOKEN = "e3826170cac44de0a3cc33be2cee48e3"
DOUBAO_API_KEY = "f0b4eaf8-5f15-4614-8c59-d041814a3cd4"
# =======================================================

def test_push(content):
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "✅ AI情报推送成功",
        "content": content
    }
    try:
        response = requests.post("https://www.pushplus.plus/send", json=data)
        print("推送成功，状态码：", response.status_code)
    except Exception as e:
        print("推送失败：", e)

def get_stock_info():
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    headers = {
        "Authorization": f"Bearer {DOUBAO_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        # ✅✅✅ 这里已经修复为正确模型名称 ✅✅✅
        "model": "doubao-seed-2.0-pro",  
        "messages": [
            {
                "role": "user",
                "content": "请只回复一句话：测试成功"
            }
        ],
        "temperature": 0.1
    }
    
    try:
        print("正在调用火山引擎AI...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        # 打印返回结果，方便排查
        print("AI返回原始内容：", response.text)
        
        res = response.json()
        ai_content = res["choices"][0]["message"]["content"]
        print("AI返回内容：", ai_content)
        return ai_content
    
    except Exception as e:
        return f"调用失败：{str(e)}"

if __name__ == "__main__":
    info = get_stock_info()
    test_push(info)
