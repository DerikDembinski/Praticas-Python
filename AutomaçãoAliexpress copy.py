from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random
import undetected_chromedriver as uc 
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions


#---------------DEFINA SEU EMAIL E SENHA--------------------------
#(OBS USE UMA CONTA REAL - POIS SENÃO O ALI TENTA IR PARA A ABA DE CADASTRO E O TRATAMENTO DE ERRO NÃO ESTA COMPLETO)
email = 'derikdembinski@outlook.com'
senha = 'Dragonfly2021@'
#-----------------------------------------------------------------


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,900','--incognito','--headless']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException,
        ]
    )
    return driver, wait

def digitar_naturalmente(texto,elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)

def fechar_popup():
    sleep(1)
    fechar_popup = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'pop-close-btn')))
    fechar_popup.click()

def switch_to_iframe(driver, iframe_id):
    try:
        # Encontrar o IFRAME usando ID
        driver.switch_to.frame(iframe_id)
        return True  # Retorna True se a mudança para o iframe foi bem-sucedida

    except Exception as e:
        return False  # Retorna False se houver uma exceção ao mudar para o iframe

def inserir_email(email):
    try:
        #Encontrando, clicando e inserindo email no campo de login
        entrada_email = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//input[@id="fm-login-id"]')))
        entrada_email.click()
        sleep(1)
        digitar_naturalmente(email,entrada_email)
        sleep(1)
    except:
        campo_email_2 = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//input[@class="cosmos-input"]')))
        campo_email_2.click()
        sleep(1)
        digitar_naturalmente(email,campo_email_2)
        sleep(1)
        clik_intermediario = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//span[@class="nfm-multiple-email-prefix"]')))
        clik_intermediario.click()
        sleep(1)
        click_continuar = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//span[text()='Continuar']")))
        click_continuar.click()
        sleep(1)

def inserir_senha(senha):
    #Encontrando, clicando e inserindo senha no campo de senha
    entrada_senha = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//input[@aria-label="Senha"]')))
    entrada_senha.click()
    sleep(1)
    digitar_naturalmente(senha,entrada_senha)
    sleep(3)

def hover_usuario():
    campo_usuario = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'my-account--menuItem--1GDZChA')))
    campo_usuario.click()
    sleep(1)





#---------------Navegar ate o site--------------------------------
driver, wait = iniciar_driver()
driver = uc.Chrome()
driver.get('https://pt.aliexpress.com')
sleep(1)
#-----------------------------------------------------------------


#---------------Fechando o pop up automatico----------------------
fechar_popup()
#-----------------------------------------------------------------


#---------------Clicando na aba de usuario------------------------
#Fase 01
hover_usuario()
#-----------------------------------------------------------------


#---------------Clicando em entrar na conta-----------------------
campo_entrar_na_conta = wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,'my-account--signin--RiPQVPB')))
campo_entrar_na_conta.click()
sleep(1)
#-----------------------------------------------------------------

#---------------Clicando e inseririndo email----------------------
inserir_email(email)
#-----------------------------------------------------------------


#---------------Clicando e inseririndo senha----------------------
inserir_senha(senha)
#-----------------------------------------------------------------


#---------------Clicando em entrar apos inserir asinfos----------
#Encontrando e clicando no botao de entrar
botton_entrar = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//button[@aria-label="Entrar"]')))
botton_entrar.click()
sleep(1)
#-----------------------------------------------------------------


#-------------Resolvendo slide to verification--------------
#Aqui foi criado uma funcao, para quando o aliexpress pede para fazer o 'slide toverify'
#Se a função retornar True significa que foi possivel mudar para o iframe da verificação
#Em seguida o if executa os comandos necessarios para resolver a verificação
if switch_to_iframe(driver,"baxia-dialog-content") == True:
    sleep(2)
    #Iniciando o ActionChains
    chain = ActionChains(driver)
    #Encontrando o elemento inicial do slide
    slide = driver.find_element(By.XPATH,'//span[@id="nc_1_n1z"]')
    sleep(2)
    #Clicando e arrastando o slide
    chain.click_and_hold(slide).move_by_offset(400,0).release().perform()
#-----------------------------------------------------------------

#---------------Fechando o pop up automatico----------------------
fechar_popup()
#-----------------------------------------------------------------

#---------------Clicando na aba de usuario------------------------
#Fase 02
hover_usuario()
#-----------------------------------------------------------------


#---------------Clicando na aba de pedidos------------------------
lista_hover = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,"//span[@class='my-account--menuText--1km-qni']")))
lista_hover[0].click()
#-----------------------------------------------------------------

#---------------Clicando na pedidos enviados----------------------
elementos_minha_conta = wait.until(expected_conditions.visibility_of_all_elements_located((By.XPATH,'//div[@class="comet-tabs-nav-item"]')))
elementos_minha_conta[2].click()
#-----------------------------------------------------------------


pedidos_enviados = driver.find_elements(By.XPATH,'//div[@class="order-item"]')

quantidade_pedidos = len(pedidos_enviados)







ids_pedidos = []
lista_pedidos = []
for pedido in pedidos_enviados:
    lista_pedidos.append(pedido.text)

ids_pedidos_produtos = {}

for pedido in lista_pedidos:
    order_info = pedido 
    match = re.search(r'ID do pedido: (\d+)', order_info)
    if match:
        order_id = match.group(1)
        ids_pedidos.append(order_id)
        produto_match = re.search(r'Detalhes do pedido\n([\s\S]*?)\nR\$', order_info)
    if produto_match:
        produto_nome = produto_match.group(1).strip()


        ids_pedidos_produtos[order_id] = produto_nome




for pedido, produto_nome in ids_pedidos_produtos.items():
    print("ID do Pedido:", pedido)
    print("Nome do Produto:", produto_nome)
    print()

for pedido in ids_pedidos:
    print(pedido)








#Aguardando fim da automação
sleep(2)
input('Aguardado para encerrar')
driver.close()
