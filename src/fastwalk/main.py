import uvicorn
from fastapi import FastAPI

from fastwalk.configs import router_config

app = FastAPI(
    title="FastWalk",
    description="Simple API to try out functionality described in FastAPI tutorial",
    version="0.1.1"
    # More application metadata specification options can be found at https://fastapi.tiangolo.com/tutorial/metadata/
)

app.include_router(router_config.router)

if __name__ == '__main__':
    uvicorn.run(
        app="fastwalk.main:app",
        host="127.0.0.1",
        port=1234,
        reload=True,
        reload_dirs=["src"]
    )
