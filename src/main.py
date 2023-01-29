import aioredis
from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from api.v1 import films, genre, person
from core.config import settings
from db import elastic, redis


app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
)


@app.on_event("startup")
async def startup():
    redis.redis = await aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        encoding="utf8",
        decode_responses=True,
    )
    FastAPICache.init(RedisBackend(redis.redis), prefix="fastapi-cache")

    elastic.es = AsyncElasticsearch(
        hosts=[
            f"{settings.ELASTIC_SCHEMA}://{settings.ELASTIC_HOST}:{settings.ELASTIC_PORT}"
        ]
    )


@app.on_event("shutdown")
async def shutdown():
    await redis.redis.close()
    await redis.redis.wait_closed()
    await elastic.es.close()


app.include_router(films.router, prefix="/api/v1/films")
app.include_router(genre.router, prefix="/api/v1/genre")
app.include_router(person.router, prefix="/api/v1/person")
