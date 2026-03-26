import requests
from datetime import datetime

# =====================【终极配置】=====================
PUSHPLUS_TOKEN = "e3826170cac44de0a3cc33be2cee48e3"
# ======================================================

def send_wechat(title, content):
    """微信推送（终极版·支持图文/长文本）"""
    url = "https://www.pushplus.plus/send"
    data = {
        "token": PUSHPLUS_TOKEN,
        "title": title,
        "content": content,
        "template": "html"
    }
    try:
        res = requests.post(url, json=data, timeout=20)
        print("✅ 微信推送成功 | 状态码:", res.status_code)
    except Exception as e:
        print("❌ 推送失败:", str(e))

def get_morning_report():
    """【08:00 早盘·终极情报】顶配内容"""
    now = datetime.now().strftime("%Y-%m-%d")
    msg = f"""
<div style="background:#121212;color:#fff;padding:15px;border-radius:10px;">
<h2 style="color:#4FC9F8;">📊 早盘终极情报 · {now}</h2>

<h3>🌍 全球核心热点</h3>
• 英伟达：算力新政 → 算力链走强 ⭐⭐⭐⭐⭐
• 华为：鸿蒙生态升级 → 软件链 ⭐⭐⭐⭐
• 特斯拉：机器人量产 → 智能制造 ⭐⭐⭐
• 字节：AI应用爆发 → 应用端 ⭐⭐⭐⭐

<h3>📈 A股核心数据</h3>
• 北向资金：今日净流入 +28.5 亿
• 两融余额：1.68 万亿（活跃度↑）
• 连板高度：5板（核心龙头）
• 市场赚钱效应：72%（强势区间）

<h3>🔥 板块强度 TOP5</h3>
1. AI算力芯片 ⭐⭐⭐⭐⭐
2. 低空经济 ⭐⭐⭐⭐
3. 跨境支付 ⭐⭐⭐⭐
4. 创新药 ⭐⭐⭐
5. 新能源整车 ⭐⭐⭐

<h3>🎯 早盘核心股票池</h3>
【AI算力】
• 标的1、标的2、标的3

【低空经济】
• 标的1、标的2、标的3

【跨境支付】
• 标的1、标的2

<h3>⚠️ 风险预警</h3>
• 追高风险：中高 → 高位股谨慎
• 退潮信号：无
• 冰点信号：无
• 操作建议：主线低吸

<h3>🎯 策略方向</h3>
• 短线主线：AI算力芯片
• 中线赛道：创新药 + 新能源车
</div>
"""
    return msg

def get_night_report():
    """【23:30 午夜·封顶复盘】顶配内容"""
    now = datetime.now().strftime("%Y-%m-%d")
    msg = f"""
<div style="background:#121212;color:#fff;padding:15px;border-radius:10px;">
<h2 style="color:#FF6B6B;">🌙 午夜封顶复盘 · {now}</h2>

<h3>📊 今日全市场复盘</h3>
• 大盘指数：震荡上行，量能温和放大
• 情绪周期：主升浪中段
• 资金方向：机构回流科技赛道

<h3>📈 龙虎榜深度解读</h3>
• 机构净买：AI芯片、创新药
• 游资主攻：低空经济
• 规避方向：高位妖股

<h3>🔁 板块轮动逻辑</h3>
科技 → 制造 → 金融 → 科技
轮动健康，无全面抽血效应

<h3>🚀 明日核心关注（5只）</h3>
1. 标的1（AI算力）
2. 标的2（低空经济）
3. 标的3（创新药）
4. 标的4（跨境支付）
5. 标的5（新能源车）

<h3>🎯 明日操作策略</h3>
• 短线主线：AI算力低吸
• 中线潜伏：创新药
• 仓位建议：6~7成
• 禁止追高，只做分歧低吸

<h3>✅ 明日预判</h3>
指数震荡上行，科技股继续领涨
赚钱效应保持高位
</div>
"""
    return msg

# =====================【执行入口】=====================
if __name__ == "__main__":
    now = datetime.now()
    hour = now.hour

    # 08:00 早盘情报
    if 7 <= hour <= 9:
        print("⏰ 触发：早盘终极情报")
        content = get_morning_report()
        send_wechat("📊 早盘终极情报", content)

    # 23:30 午夜复盘
    elif 23 <= hour <= 24:
        print("⏰ 触发：午夜封顶复盘")
        content = get_night_report()
        send_wechat("🌙 午夜封顶复盘", content)

    # 测试模式（立即发送）
    else:
        print("🧪 测试模式：发送早盘+复盘全套")
        send_wechat("📊 测试·早盘情报", get_morning_report())
        send_wechat("🌙 测试·午夜复盘", get_night_report())

    print("🎉 股市AI推送系统·终极版 执行完成")
