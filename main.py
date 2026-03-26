import requests

# ===================== 【你的配置】=====================
PUSHPLUS_TOKEN = "e3826170cac44de0a3cc33be2cee48e3"
# 你的火山引擎 API Key（无需修改，通用模型已适配）
DOUBAO_API_KEY = "f0b4eaf8-5f15-4614-8c59-d041814a3cd4"
# =======================================================

def test_push(content):
    """测试微信推送（带日志详细输出）"""
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "✅ 豆包AI测试成功",
        "content": content
    }
    try:
        response = requests.post("https://www.pushplus.plus/send", json=data, timeout=15)
        print("✅ 推送请求已发送！")
        print("📌 推送状态码:", response.status_code)
        print("📌 推送返回内容:", response.text[:200])
    except Exception as e:
        print("❌ 推送异常:", str(e))

def get_real_doubao_info():
    """调用火山引擎豆包真实通用模型（无版本限制，必有权限）"""
    url = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    headers = {
        "Authorization": f"Bearer {DOUBAO_API_KEY}",
        "Content-Type": "application/json"
    }
    # 🔥 使用官方通用模型，无需指定具体版本，避免模型不存在报错
    payload = {
        "model": "doubao",  # 通用模型名称，无需带 2.0 后缀
        "messages": [
            {
                "role": "user",
                "content": "请给我发送一条测试消息，内容仅写：测试成功 - 豆包通用模型调用成功"
            }
        ],
        "temperature": 0.1,
        "max_tokens": 100
    }
    
    try:
        print("🔄 正在调用火山引擎豆包通用模型...")
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        print("📄 AI原始返回内容:", response.text[:500])  # 打印原始内容，方便排查
        
        # 解析 JSON 响应
        res = response.json()
        # 兼容所有返回结构，避免 'choices' 报错
        if "choices" in res and res["choices"]:
            ai_content = res["choices"][0]["message"]["content"]
            print("✅ AI解析完成:", ai_content)
            return ai_content
        else:
            return f"⚠️ AI无返回内容：{str(res)}"
    
    except Exception as e:
        error_msg = f"❌ AI调用失败：{str(e)}"
        print(error_msg)
        return error_msg

if __name__ == "__main__":
    # 1. 调用真实豆包 AI
    ai_result = get_real_doubao_info()
    # 2. 推送给微信
    test_push(ai_result)
    print("\n🎉 全部执行完成！")
