#coding=utf-8
# # API信息
# 请求地址: https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro
# API Key: zhPq4W1evhrYYmK3iy3DfK0G
# Secret Key: IfB7GZT6BuvgcGRRckyCnCNpk99T7Wdt
# 模型名称: ERNIE-Bot 4.0
# 应用名称: 起居注
# https://console.bce.baidu.com/tools/?u=bce-head#/api?product=AI&project=%E5%8D%83%E5%B8%86%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%B9%B3%E5%8F%B0&parent=ERNIE-Bot-4&api=rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro&method=post
# 用户需求总结：\n1. 对AI感兴趣，但只了解神经网络和深度学习。\n2. 想了解Sam Altman和Agent相关的信息。\n用户水平评估：\n该用户是 一位计算机专业的大四学生，对AI有一定了解，但只了解神经网络和深度学习，对最前沿的术语不太了解。该用户对AI感兴趣，并希望了解更多相关信息。
# 请给出 sam 演讲中 经常使用的10个 英文专业术语，科学术语，去掉常用词，以中文和英文对照的形式输出，且每一个单词都换行。

import requests
import json

API_KEY = "zhPq4W1evhrYYmK3iy3DfK0G"
SECRET_KEY = "IfB7GZT6BuvgcGRRckyCnCNpk99T7Wdt"

def main():
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "请给出 sam 演讲中 经常使用的10个 英文专业术语，科学术语，去掉常用词，以中文和英文对照的形式输出，且每一个单词都换行。"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == '__main__':
    main()
