import os

import requests
import json

# 添加 server 酱通知
server_key = os.environ["SERVER_KEY"]

# 获取掘金 cookie
jj_cookie = os.environ["JJ_COOKIE"]

# 掘金 api_url
baseUrl = 'https://api.juejin.cn/'
checkInUrl = baseUrl + 'growth_api/v1/check_in'
lotteryUrl = baseUrl + 'growth_api/v1/lottery/draw'
postShortMsgUrl = baseUrl + 'content_api/v1/short_msg/publish?aid=2608&uuid=6901905951083841032&spider=0'

# user-agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}

# shortMsgContent
shortMsg = {"content":"[7163537723910225960#JUEJIN FRIENDS 好好生活计划#] [黑脸]好好生活，签到签到","sync_to_org":False,"theme_id":"7163537723910225960"}

# server 酱消息推送
def send_server(title, content):
    url = "https://sctapi.ftqq.com/%s.send" % server_key
    params = {'text': title, 'desp': content}
    resp = requests.post(url, params=params)
    print('server 酱推送状态码: %s' % resp.status_code)

# 入口
if __name__ == '__main__':
    checkInResp = requests.post(checkInUrl, headers=headers, cookies={'Cookie': jj_cookie})
    lotteryResp = requests.post(lotteryUrl, headers=headers, cookies={'Cookie': jj_cookie})
    shortMsgResp = requests.post(postShortMsgUrl, data=json.dumps(shortMsg), headers=headers, cookies={'Cookie': jj_cookie})
    resultMsg = "掘金签到结果\n" + checkInResp.text + "\n 掘金抽奖结果\n" + lotteryResp.text + "\n 沸点结果\n" + shortMsgResp.text
    if server_key:
        send_server('掘金签到+每日抽奖', resultMsg)
    else:
        print('未启用 server 酱通知')
    print('本次签到与抽奖结果信息:\n %s' % resultMsg)
