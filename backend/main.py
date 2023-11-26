from fastapi import FastAPI, HTTPException, Request
from models import UserAnswers
from fastapi.middleware.cors import CORSMiddleware
from api import call_external_api

app = FastAPI()

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # 允许的源列表
    allow_credentials=True,
    allow_methods=["*"],  # 允许的方法
    allow_headers=["*"],  # 允许的头部
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AGInsider API!"}

@app.post("/get_demand/")
async def process_demand(request: Request):
    # 从请求中读取原始文本体
    body = await request.body()
    answer = body.decode("utf-8")  # 确保正确解码为字符串
    processed_demand = "处理后的需求: " + answer
    return {"response": processed_demand}

@app.post("/process_input/")
async def process_input(request: Request):
    body = await request.body()
    user_input = body.decode("utf-8")

    if not user_input:
        raise HTTPException(status_code=400, detail="No input provided")

    # 调用外部 API
    external_api_response = call_external_api(user_input)
    res = external_api_response["result"]
    print(res)

    # 处理返回的数据并构造响应
    processed_response = res # 或根据需求进行更具体的处理
    return {"response": processed_response}

@app.post("/test/")
async def test(tmp:str):
    return {"response": tmp+"123"}