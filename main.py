
# 直接推送测试消息
def test_push():
    try:
        content = "✅ 测试消息：你的系统部署成功！"
        data = {
            "token": PUSHPLUS_TOKEN,
            "title": "✅ 部署成功",
            "content": content
        }
        requests.post("http://www.pushplus.plus/send", json=data)
        print("推送成功！")
    except:
        print("推送失败")

test_push()


# 超简测试代码 100% 必出日志
import requests

# 把你自己的 Token 填在这里
PUSHPLUS_TOKEN  = "e3826170cac44de0a3cc33be2cee48e3"

# 推送测试消息
def test():
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "微信测试",
        "content": "如果收到这条消息，说明推送正常！"
    }
    try:
        requests.post("https://www.pushplus.plus/send", json=data)
        print("=== 推送代码已执行 ===")
    except:
        print("=== 推送失败 ===")

test()
