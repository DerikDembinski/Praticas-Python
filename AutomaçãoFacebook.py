from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import random
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,900', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

def digitar_naturalmente(texto,elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)

driver = iniciar_driver()
#Navegar ate o site
driver.get('https://facebook.com')


#-----------INSIRA SEUS DADOS ABAIXO---------------------->
email = 'Email/Telefone'
senha = 'Senha'
texto_postagem = 'Sua Mensagem'
#--------------------------------------------------------->





#Encontrar e clicar e preencher campo de email 
campo_email = driver.find_element(By.XPATH,'//input[@placeholder="Email ou telefone"]')
campo_email.click()
sleep(2)
#Digitar com naturalidade o email
digitar_naturalmente(email,campo_email)
sleep(2)

#Pular para o preenchimento de senha
campo_email.send_keys(Keys.TAB)

#Encontrar e clicar e preencher campo de senha
campo_senha = driver.find_element(By.XPATH,'//input[@placeholder="Senha"]') 
#Digitar com naturallidade no campo senha
digitar_naturalmente(senha,campo_senha)
sleep(2)

#Encontrar e clicar no campo entrar
campo_entrar = driver.find_element(By.XPATH,'//button[@name="login"]')
campo_entrar.click()
sleep(3)

#Encontrar o campo de  postagem e clicar nele
campo_postagem = driver.find_element(By.XPATH,'//span[starts-with(text(),"No que você está pensando")]')
campo_postagem.click()
sleep(3)

#Clicar na insercao de texto
inserir_texto = driver.find_element(By.XPATH,'//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]')
inserir_texto.click()
sleep(2)

#Inserir texto para postagem
digitar_naturalmente(texto_postagem,inserir_texto)
sleep(2)

#Clicar em publicar
campo_publicar = driver.find_element(By.XPATH,'//span[starts-with(text(),"Publicar")]')
campo_publicar.click()
sleep(10)

driver.close()
print('Mensagem postada com sucesso')
