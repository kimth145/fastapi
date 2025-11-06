# uvicorn main:app --host 0.0.0.0 --port $PORT
import uvicorn
import os
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
CORSMiddleware,
# すべてのoriginを許可するように設定（実際の展開では必要に応じて変更）
allow_origins=["*"],
# Cookie使用設定
allow_credentials=False, 
# すべてのHTTPメソッドを許可するように設定
allow_methods=["*"], 
# すべてのヘッダーを許可するように設定
allow_headers=["*"], 
)

@app.get('/')
async def read_root():
    return {"Hello": "World"}

@app.get('/order/apple')
async def read_apple(color:str = Query(max_length=5)):
    if color == "red":
        ee = "🍎"
    else:
        ee = "🍏"
    return {"msg":ee+"が注文されました。"}

@app.get('/banana')
async def read_banana():
    return "🍌が注文されました。"

@app.get('/pineapple')
async def read_pineapple():
    return "🍍が注文されました。"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000)) # RenderはPORTを設定します
    uvicorn.run(app, host="0.0.0.0", port=port)