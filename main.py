from fastapi import FastAPI, Query, Path
import os
import uvicorn

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/ramen")
async def hello():
    return "짬뽕 보내요~"

@app.get("/order/{menu}/{spycy_lev}")
async def hello(menu: str, spycy_lev: str ):
    return menu + "を辛さ" + spycy_lev + "で予約しました。"

@app.get("/order/{menu}")
async def hello(menu: str = Path(max_length=3), spycy_lev: str = Query(None, max_length=3)):
    return menu + "を辛さ" + "普通" if spycy_lev == None else spycy_lev + "で予約しました。"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000)) # RenderはPORTを設定します
    uvicorn.run(app, host="0.0.0.0", port=port)