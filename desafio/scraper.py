from playwright.async_api import async_playwright
from twocaptcha import TwoCaptcha
import asyncio
import time
import os
import re

class Scraper():
    
    async def scraperdata(self, cnpj):
      solver = TwoCaptcha('520dfa64322a8805141561e35bf80442')
      url = 'https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao_CS.asp'
      
      try:
          async with async_playwright() as playwright:
              chromium = playwright.chromium
              browser = await chromium.launch()
              page = await browser.new_page()
              await page.goto(url)
              await page.locator('//html/body/div/div[1]/div/div/div/form/div[1]/div[2]/div/div[1]/div[1]/img').screenshot(path='captchas/captcha.png')
              await page.fill('#cnpj', str(cnpj))
              
              
              result = solver.normal('captchas/captcha.png')
              # Aguardando retorno da resoluçao do captcha
              time.sleep(20)
          
              if result:
                  code = result['code']
                  await page.locator('//html/body/div/div[1]/div/div/div/form/div[1]/div[2]/div/div[2]/input').fill(code)
                  await page.locator('//*[@id="frmConsulta"]/div[3]/div/button[1]').click()
                  os.remove('captchas/captcha.png')

              await asyncio.sleep(2)
              info = await page.locator('//html/body/div[1]/div/div/div/div/div[2]/div/div').evaluate("""el => el.innerText""")

              if info: 
                  await browser.close()
                  return {"info": re.sub(r'\r?\n|\r|\t', ' ', info)}
              else:
                  return {
                  "status": "error", 
                  "message": "NÃO FORAM ENCONTRADAS INFORMAÇÕES PARA O CNPJ INFORMADO", 
                  "code": "204"
                  }
      except:
          return {
                  "status": "error", 
                  "message": "NÃO FORAM ENCONTRADAS INFORMAÇÕES PARA O CNPJ INFORMADO", 
                  "code": "204"
                  }



        


