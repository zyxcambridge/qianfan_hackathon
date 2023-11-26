import requests
import json

API_KEY = "zhPq4W1evhrYYmK3iy3DfK0G"
SECRET_KEY = "IfB7GZT6BuvgcGRRckyCnCNpk99T7Wdt"

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def call_external_api(user_input):
    access_token = get_access_token()
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/plugin/720xzhsvxd76scx5/?access_token=" + access_token
    content = f"请根据用户当前对AI了解的水平和他感兴趣的方面，结合知识库的信息，给出5个AI相关的英文专业术语，去掉常用词如machine learning，deep learning，neural network,保留等有关专业术语，用户输入的单词 解释排名在第一，如果上一次出现过，就删除该单词，增加多个换行符号，每个单词以中文和英文对照的形式输出，并给出例句和使用场景。\n用户信息：'{user_input}'。"

    # content = f"请根据用户当前对AI了解的水平和他感兴趣的方面，结合知识库的信息， 给出5个AI相关的英文专业术语，去掉常用词如machine learning，deep learning，neural network等。请以中英对照的方式列出第一行单词、第二行例句和第三行使用场景，以便用户更好地理解这些术语的意义和用途。请注意，你的回答应该清晰、准确，并提供足够的细节来支持你的观点。\n用户信息：'{user_input}'。"
    
    # content = f"请根据用户当前对AI了解的水平和他感兴趣的方面，结合知识库的信息， 给出3个AI相关的英文专业术语，去掉常用词如machine learning，deep learning，neural network等。保留 Align ，每一个标题前面增加2个\n换行，每个单词以中文和英文对照的形式输出 并给出例句和使用场景。\n用户信息：'{user_input}'。"

    payload = json.dumps({
        "query": content,
        "plugins":["uuid-zhishiku"],
        "verbose":True
    })
    headers = {'Content-Type': 'application/json'}
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()  # 假设返回值是 JSON
