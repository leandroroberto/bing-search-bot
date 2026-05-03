from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

#Inicializa o webdriver com chrome
navegador = webdriver.Chrome()

#Abre o site do Bing para a pesquisa
navegador.get("https://www.bing.com/")

#Maximiza a janela do Bing
navegador.maximize_window()

#Clica no botão de aceitar os termos
WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.ID, "bnp_btn_accept"))).click()

#Armazena o elemento "barra de pesquisa na variável" e aguarda esse elemento aparecer na tela
barra_pesquisa = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.ID, "sb_form_q")))

#Digita na barra de pesquisa do google um texto para pesquisar
barra_pesquisa.send_keys("Automação com python")

#Executa o submit na página e faz a pesquisa
barra_pesquisa.submit()

#Aguarda resultados aparecerem
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.b_algo h2")))

#Lista para armazenar os titulos
titulos = []

#Captura os títulos da página
resultados = navegador.find_elements(By.CSS_SELECTOR, "li.b_algo h2")

#Itera sobre a lista resultados e adiciona os resultados na lista Titulos
for resultado in resultados:
    titulos.append(resultado.text)

#Rola a página até o final
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#Clica na segunda página da pesquisa
navegador.find_element(By.CLASS_NAME, "sb_bp").click()

#Aguarda os elementos da próxima página
WebDriverWait(navegador, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.b_algo h2")))

novos_resultados= navegador.find_elements(By.CSS_SELECTOR, "li.b_algo h2")

for novo_titulo in novos_resultados:
    titulos.append(novo_titulo.text)


for titulo in titulos:
    print(titulo)

time.sleep(30)