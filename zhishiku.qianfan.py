
#coding=utf-8
# 
'''
https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/plugin/720xzhsvxd76scx5/
https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/plugin/720xzhsvxd76scx5/
# 用户需求总结：\n1. 对AI感兴趣，但只了解神经网络和深度学习。\n2. 想了解Sam Altman和Agent相关的信息。\n用户水平评估：\n该用户是 一位计算机专业的大四学生，对AI有一定了解，但只了解神经网络和深度学习，对最前沿的术语不太了解。该用户对AI感兴趣，并希望了解更多相关信息。
API Key:
zhPq4W1evhrYYmK3iy3DfK0G


Secret Key:


IfB7GZT6BuvgcGRRckyCnCNpk99T7Wdt


'''
import requests
import json

API_KEY = "zhPq4W1evhrYYmK3iy3DfK0G"
SECRET_KEY = "IfB7GZT6BuvgcGRRckyCnCNpk99T7Wdt"


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
        
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=zhPq4W1evhrYYmK3iy3DfK0G&client_secret=IfB7GZT6BuvgcGRRckyCnCNpk99T7Wdt"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json().get("access_token"))
    return response.json().get("access_token")

def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/plugin/720xzhsvxd76scx5/?access_token=" + get_access_token()
    
    # payload = json.dumps({
    #     "query": "用户需求总结：\n1. 对AI感兴趣，但只了解神经网络和深度学习。\n2. 想了解Sam Altman和Agent相关的信息。\n用户水平评估：\n该用户是 一位计算机专业的大四学生，对AI有一定了解，但只了解神经网络和深度学习，对最前沿的术语不太了解。该用户对AI感兴趣，并希望了解更多相关信息。",
    #     "plugins":["uuid-zhishiku"],
    #     "verbose":True
    # })
    # headers = {
    #     'Content-Type': 'application/json'
    # }
    # response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    
    payload = json.dumps({
        "query": "请给出 sam 演讲中 经常使用的10个 英文专业术语，科学术语，去掉常用词， 以中文和英文对照的形式输出，且用中文给出每一个单词的解释，以及使用场景，包含(alignment ,agent)。",
        "plugins":["uuid-zhishiku"],
        "verbose":True
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    
def get_sam_wordlists_zhishiku():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/plugin/720xzhsvxd76scx5/?access_token=" + get_access_token()
    
    payload = json.dumps({
        "query": "请给出 sam 演讲中 经常使用的10个 英文专业术语，科学术语，去掉常用词， 以中文和英文对照的形式输出，且用中文给出每一个单词的解释，以及使用场景，包含(alignment ,agent)。",
        "plugins":["uuid-zhishiku"],
        "verbose":True
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    print(response.text)
    
    
      

if __name__ == '__main__':
    main()