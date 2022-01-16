import uvicorn
from fastapi import FastAPI

from fastwalk.configs import router_config

app = FastAPI(title="FastWalk", version="0.1.1")

app.include_router(router_config.router)

if __name__ == '__main__':
    uvicorn.run(
        app="fastwalk.main:app",
        host="127.0.0.1",
        port=1234,
        reload=True,
        reload_dirs=["src"]
    )
