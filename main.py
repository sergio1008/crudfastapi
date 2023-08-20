import uvicorn
from typing import Union
from api.UserApi import router as apiUsers

from fastapi import FastAPI

app = FastAPI()

app.include_router(apiUsers)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
