import requests

# 这里填入你的 PushPlus Token
PUSHPLUS_TOKEN = "e3826170cac44de0a3cc33be2cee48e3"

# 测试函数
def send_test():
    url = "https://www.pushplus.plus/send"
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "测试推送",
        "content": "收到这条消息 = 推送功能正常"
    }

    try:
        response = requests.post(url, json=data)
        print("推送请求已发送")
        print("返回状态码:", response.status_code)
        print("返回内容:", response.text)
    except Exception as e:
        print("推送异常:", str(e))

# 执行
send_test()
