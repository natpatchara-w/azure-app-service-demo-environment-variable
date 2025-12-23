import os

import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
def home():
    return {"Hello"}

@app.get("/env/{env_var}")
def get_env(env_var: str):
    return {
            "var_name": env_var,
            "value": os.environ.get(env_var, "not found")
            }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
