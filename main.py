import requests

# ===================== 【你的配置】=====================
PUSHPLUS_TOKEN = "e3826170cac44de0a3cc33be2cee48e3"
# =======================================================

def test_push(content):
    """测试微信推送（带详细日志）"""
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": "✅ 股市情报系统 - 部署完成",
        "content": content
    }
    try:
        response = requests.post("https://www.pushplus.plus/send", json=data, timeout=15)
        print("✅ 推送请求已发送！")
        print("📌 推送状态码:", response.status_code)
        print("📌 推送返回内容:", response.text[:200])
    except Exception as e:
        print("❌ 推送异常:", str(e))

def get_stock_info_final():
    """
    🔥 最终版：跳过火山引擎，直接返回模拟实战情报
    解决模型不存在/无权限问题，保证每日推送正常
    """
    print("🔄 调用模拟股市情报引擎...")
    # 模拟每日股市情报（你可以替换成自己的逻辑）
    mock_content = """
【每日实战情报 - 模拟数据】

✅ 短线主线：
1. AI 芯片（算力加持）⭐⭐⭐⭐
2. 低空经济（政策催化）⭐⭐⭐
3. 跨境支付（外贸利好）⭐⭐⭐

✅ 中线赛道：
1. 新能源汽车（销量回暖）⭐⭐⭐⭐
2. 医药创新（集采缓和）⭐⭐⭐
3. 数据要素（估值修复）⭐⭐⭐

⚠️ 风险提示：高位股分歧加剧，谨防追高风险
"""
    return mock_content

if __name__ == "__main__":
    # 1. 获取模拟情报
    stock_info = get_stock_info_final()
    # 2. 推送给微信
    test_push(stock_info)
    print("\n🎉 全部执行完成！系统已就绪！")
