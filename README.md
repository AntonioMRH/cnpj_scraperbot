# CNPJ Scraper Bot

Este scraper bot tem como objetivo verificar a existência de informações relacionadas a um dado CNPJ. Para isso ele utiliza a página pública de pesquisa de CNPJs da Receita Federal. Caso ele não encontre informações retornará um aviso.

## Instalação

1. Clonar o repositório em sua máquina local.
2. Navegar até a pasta do ambiente virtual venv usando `cd ˜/desafio` e usar o comando `source bin/activate` para ativar o ambiente.
3. Instalar as bibliotecas usadas com `pip install 2captcha-python playwright fastapi uvicorn` ou `pip install -r requirements.txt`.

4. Iniciar o servidor com `uvicorn main:app --reload`.
5. Visitar `http://localhost:8000/{cnpj_aqui}` no seu navegador para usar a API.
6. Para maior facilidade no uso da API recomenda-se usar o `http://localhost:8000\docs` que dispõe da interface Swagger.

## Uso

Para usar basta seguir os passos descritos na seção de instalação e acessar o `http://localhost:8000/{cnpj_aqui}` e aguardar o retorno das informações.

## Stack

- [Python](https://www.python.org/)
- `Pip` Python package manager
- [2captcha](https://2captcha.com/)
- [Playwright](https://playwright.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)

## Observações

1. O app foi desenvolvido usando MacOS, não foi testado em ambiente Windows. É possível que ocorram problemas de compatibilidade.

2. A solução foi desenvolvida utilizando uma serviço tercerizado para resolução de captchas, da empresa 2captcha.

3. O maior desafio do desenvolvimento foi criar um bypass para o captcha presente na página. Existem diversas soluções para esse problema, como por exemplo usar Machine Learning. No entanto, a solução encontrada foi desenvolvida levando em consideração o tempo disponível para o desafio e o custo-benefício.
