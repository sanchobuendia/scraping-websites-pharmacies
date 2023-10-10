# Projeto Achè

## Arquivo dict_url.json

Criamos um arquivo json com as informações necessárias para fazer o scrawper para cada site. O json possui, atualmente, os seguintes campos:

"drogariasaopaulo": {
        "url": "https://www.drogariasaopaulo.com.br/",
        "dom": " ",
        "css_result": " ",
        "searchbox": "https://www.drogariasaopaulo.com.br/pesquisa?q=",
        "searchresults": "/html/body/main/div[2]/div/div/div/div[2]/div[1]/ul/li[1]",
        "banner_xpath": "/html/body/main/div[6]/div/div/div[1]/div[2]/ul",
        "url_category": "https://www.drogariasaopaulo.com.br/medicamentos",
        "category_xpath": "/html/body",
        "urlsubcategory": " ",
        "subcategory_xpath": " ",
	"carousel_button_xpath": " ",
        "cookie_button_css": " ",
        "iframe_css": " "},

"PACHECO": {
        "url": "https://www.drogariaspacheco.com.br/",
        "dom": " ",
        "css_result": " ",
        "searchbox": "https://www.drogariaspacheco.com.br/pesquisa?q=",
        "searchresults": "/html/body/main/div[2]/div/div/div/div[2]/div[1]/ul/li[1]",
        "banner_xpath": "/html/body/main/div[6]/div/div/div[1]/div[2]/ul",
        "url_category": "https://www.drogariaspacheco.com.br/medicamentos",
        "category_xpath": "/html/body",
        "urlsubcategory": " ",
        "subcategory_xpath": " ",
	"carousel_button_xpath": " ",
        "cookie_button_css": " ",
        "iframe_css": " "
    }

Coloquei estes dois exemplos para exemplificar. Os nomes das drogarias esão escritos em caixa alta no excel que a empresa enviou, como é o caso da **PACHECO**. No entanto, algumasa drogarias não aparecem nas promoções programadas para o mês de Outubro, são elas: drogariasaopaulo, drogasmil e farmalife. As descrições dos campos são as seguintes:

"url": url da drogaria
"dom": 
"css_result": 
"searchbox": url do buscador do site
"searchresults": Xpath da descição do produto procurado
"banner_xpath": Xpath do banner da homepage,
"url_category": url da aba de categoria da drogaria,
"category_xpath": Xpath da aba de categoria,
"urlsubcategory": url da aba de subcategoria da drogaria,
"subcategory_xpath": Xpath da aba de subcategoria,
"carousel_button_xpath": Xpath do botão da direita do carrossel do banner,
"cookie_button_css": Css selector do botão de rejeitar cookies,
"iframe_css": Css selector da localização do iframe do site

## Arquivo get_prices.py

No arquivo get_prices.py estão as funções necessárias para encontrar a descrição e o preço de um produto nos sites mapeados. 

Basta importar a função check_price:

from get_prices import check_price

E passar como parâmetro o arquivo que eles vão enviar. Este arquivo deve ter as colunas:
  * "BANDEIRA": com os nomes das drogarias 
  * "SKU": com a descrição do produto
  * "PARA": como o preço que deve ser anunciado

 Esses são os nomes das colunas no arquivo **CONSOLIDADO OFERTA PROMO_OUTUBRO.xlsx**. Pode ser que no arquivo novo que eles vão enviar os nomes sejam alterados.

 Para fazer o teste eu criei um novo arquivo chamado **OFERTA_OUTUBRO.csv**, porque o arquivo deles estava todo desconfigurado. Talvez seja interessante eles formatarem melhor o excel deles.

 Voltando para a função check_price. Ao chamar a função passando o dataframe ela retorna o mesmo dataframe mais as segunites colunas:
  * "descricao": descrição do produto encontrada no site. Contendo nome e preço.
  * "name_found": nome do produto extraído com o OpenAI
  * "price_found": preço do produto extraído com o OpenAI
  * "Match": coluna com True ou False. True quando o valor anunciado é o esperado e False quando não é

## Arquivo match_images.py

No arquivo match_images.py estão as funções necessárias para extrair as imagens do site e verificar se a imagem desejada é uma delas, ou seja, baixamos todas as imagens da página principal ou página de medicamentos e verificamos o **match** com a imagem que foi passada para nós.

