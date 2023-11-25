from wenxin_llm import Wenxin_LLM

from dotenv import find_dotenv, load_dotenv
import os

# 读取本地/项目的环境变量。

# find_dotenv()寻找并定位.env文件的路径
# load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv())

# 获取环境变量 OPENAI_API_KEY
api_key = "zhPq4W1evhrYYmK3iy3DfK0G"
secret_key = "IfB7GZT6BuvgcGRRckyCnCNpk99T7Wdt"

wenxin_api_key = api_key
wenxin_secret_key = secret_key
llm = Wenxin_LLM(api_key=wenxin_api_key, secret_key=wenxin_secret_key)
print(llm("你好"))
