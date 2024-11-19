# API Mini lab Krekhov Danil 5030102/20201

This API is designed to provide information about the most popular cryptocurrencies, NFTs and exchange platforms.

# Application deployment and configuration

## Requirements
    Python 3
    Postman

## Installation
1. Clone the repository:
```
git clone https://github.com/Hukker/minilab_2024.git
```
2. Install requirements
```
pip install -r requirements.txt
```

## Run application

To run the application:

``` uvicorn main:app ```

# Endpoints

## NFT
- **Endpoint**: ```/pages/bitcoin```
- **Description**: This endpoint allows you to query the prices of one or more coins by using their unique Coin API IDs.

## Exchanges
- **Endpoint**: ```/pages/derivatives```
-  **Description**: This endpoint allows you to query all the tickers from derivatives exchanges on CoinGecko.

## Coins
- **Endpoint**: ```/pages/platforms``
- **Description**: This endpoint allows you to query all the asset platforms on CoinGecko.
# Postman

Postman workplace: [click](https://www.postman.com/hukker/minilab2024/collection/l37ovmx/new-collection)
