from fastapi import FastAPI
from pages.router import router as router_coins

app = FastAPI()
app.include_router(router_coins)