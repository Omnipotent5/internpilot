from fastapi import FastAPI

app = FastAPI(title="InternPilot API")

@app.get("/")
def read<｜begin▁of▁sentence｜> read_root():
    return {"message": "InternPilot backend running"}
