from fastapi import APIRouter, Request
import requests

router = APIRouter(prefix='/pages', tags=['frontend'])


@router.get('/bitcoin')
async def get_home(request: Request):
    url = "https://api.coingecko.com/api/v3/simple/price"

    headers = {
        "ids": "bitcoin",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)


@router.get('/derivatives')
async def get_exchanges(request: Request):
    url = "https://api.coingecko.com/api/v3/derivatives"
    headers = {}
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print("Error:", response.status_code)


@router.get('/platforms')
async def get_volume_tradings(request: Request):
    url = "https://api.coingecko.com/api/v3/asset_platforms"
    headers={
        "filter":"nft"
    }
    response =requests.get(url,params=headers)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print("Error:", response.status_code)