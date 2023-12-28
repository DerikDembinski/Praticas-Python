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


def digitar_naturalmente(texto,elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)

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

    return driver

def fechar_popup():
    sleep(2)
    fechar_popup = driver.find_element(By.CLASS_NAME,'pop-close-btn')
    fechar_popup.click()
    sleep(2)

def switch_to_iframe(driver, iframe_id):
    try:
        # Encontrar o IFRAME usando ID
        driver.switch_to.frame(iframe_id)
        return True  # Retorna True se a mudança para o iframe foi bem-sucedida

    except Exception as e:
        return False  # Retorna False se houver uma exceção ao mudar para o iframe

def inserir_email():
    try:
        #Encontrando, clicando e inserindo email no campo de login
        entrada_email = driver.find_element(By.XPATH,'//input[@id="fm-login-id"]')
        entrada_email.click()
        sleep(1)
        digitar_naturalmente(email,entrada_email)
        sleep(3)
    except:
        campo_email_2 = driver.find_element(By.XPATH,'//input[@class="cosmos-input"]')
        campo_email_2.click()
        sleep(1)
        digitar_naturalmente(email,campo_email_2)
        sleep(3)
        clik_intermediario = driver.find_element(By.XPATH,'//span[@class="nfm-multiple-email-prefix"]')
        sleep(1)
        clik_intermediario.click()
        sleep(3)
        click_continuar = driver.find_element(By.XPATH,"//span[text()='Continuar']")
        sleep(2)
        click_continuar.click()
        sleep(4)

def inserir_senha():
    #Encontrando, clicando e inserindo senha no campo de senha
    entrada_senha = driver.find_element(By.XPATH,'//input[@aria-label="Senha"]')
    entrada_senha.click()
    sleep(1)
    digitar_naturalmente(senha,entrada_senha)
    sleep(5)


    #Encontrando e clicando no botao de entrar
    botton_entrar = driver.find_element(By.XPATH,'//button[@aria-label="Entrar"]')
    botton_entrar.click()
    sleep(3)

#---------------DEFINA SEU EMAIL E SENHA--------------------------
#(OBS USE UMA CONTA REAL - POIS SENÃO O ALI TENTA IR PARA A ABA DE CADASTRO E O TRATAMENTO DE ERRO NÃO ESTA COMPLETO)
email = 'derikdembinski@outlook.com'
senha = 'Dragonfly2021@'
#-----------------------------------------------------------------


#---------------Iniciar o driver----------------------------------
driver = iniciar_driver()
#Navegar ate o site
driver = uc.Chrome()
driver.get('https://pt.aliexpress.com')
sleep(1)
#-----------------------------------------------------------------


#---------------Fechando o pop up automatico----------------------
fechar_popup()
#-----------------------------------------------------------------


#---------------Clicando na aba de usuario------------------------
campo_usuario = driver.find_element(By.CLASS_NAME,'my-account--menuItem--1GDZChA')
campo_usuario.click()
sleep(2)
#-----------------------------------------------------------------


#---------------Clicando em entrar na conta-----------------------
campo_entrar_na_conta = driver.find_element(By.CLASS_NAME,'my-account--signin--RiPQVPB')
campo_entrar_na_conta.click()
sleep(2)
#-----------------------------------------------------------------

#---------------Clicando e inseririndo email----------------------
inserir_email()
#-----------------------------------------------------------------


#---------------Clicando e inseririndo senha----------------------
inserir_senha()
#-----------------------------------------------------------------


#---------------Clicando em entrar apos inserir as infos----------
#Encontrando e clicando no botao de entrar
botton_entrar = driver.find_element(By.XPATH,'//button[@aria-label="Entrar"]')
botton_entrar.click()
sleep(3)
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



#Aguardando fim da automação
sleep(2)
input('Aguardado para encerrar')
driver.close()

