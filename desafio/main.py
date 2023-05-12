from fastapi import FastAPI
from scraper import Scraper
from playwright.async_api import async_playwright
from twocaptcha import TwoCaptcha
import asyncio
import time
import os
import re


# Iniciando FastAPI
app = FastAPI()
# Criando uma instancia da classe scraper
scraper = Scraper()

# Definiçao da rota de busca de cnpj
@app.get("/{cnpj}")
async def get_cnpj_info(cnpj):
    # Usando o metodo da classe scraper que inicia o bot para o cnpj escolhido
    data = await scraper.scraperdata(cnpj)
    return data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
