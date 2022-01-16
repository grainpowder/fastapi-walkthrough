from fastapi import APIRouter

ROUTER_PREFIX = "/health"
router = APIRouter(prefix=ROUTER_PREFIX, tags=["health check"])


@router.get(
    path="/ping",
    summary="Health check with ping-pong-ing!",
    response_description="As 'ping' is sent, 'pong' will be returned as a response!",
    deprecated=False  # in case you want to deprecate the path operation rather than remove it, set this param to True
)
async def ping():
    return "pong"
