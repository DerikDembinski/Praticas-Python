from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import random



def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,900',]
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


#Iniciar o driver
driver = iniciar_driver()
#Navegar ate o site
driver.get('https://pt.aliexpress.com')
sleep(1)


def digitar_naturalmente(texto,elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1,5)/30)

#---------------DEFINA SEU EMAIL E SENHA--------------------------
#(OBS USE UMA CONTA REAL - POIS SENÃO O ALI TENTA IR PARA A ABA DE CADASTRO E O TRATAMENTO DE ERRO NÃO ESTA COMPLETO)
email = 'INSIRA SEU EMAIL AKI'
senha = 'INSIRA SUA SENHA AKI'
#-----------------------------------------------------------------

#Encontrando e fechando o pop up automatico
fechar_popup = driver.find_element(By.CLASS_NAME,'pop-close-btn')
fechar_popup.click()
sleep(2)

#Encontrando e clicando na aba de usuario
campo_usuario = driver.find_element(By.CLASS_NAME,'my-account--menuItem--1GDZChA')
campo_usuario.click()
sleep(2)

#Encontrando e clicando em ENTRAR
campo_entrar_na_conta = driver.find_element(By.CLASS_NAME,'my-account--signin--RiPQVPB')
campo_entrar_na_conta.click()
sleep(2)

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
    digitar_naturalmente('derikdembinski@outlook.com',campo_email_2)
    sleep(3)
    clik_intermediario = driver.find_element(By.XPATH,'//span[@class="nfm-multiple-email-prefix"]')
    sleep(1)
    clik_intermediario.click()
    sleep(3)
    click_continuar = driver.find_element(By.XPATH,"//span[text()='Continuar']")
    sleep(2)
    click_continuar.click()
    sleep(4)

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




#-------------Resolvendo slide to verification--------------


# Encontrando o IFRAME usando ID
driver.switch_to.frame("baxia-dialog-content")
sleep(1)
#Iniciando o ActionChains
chain = ActionChains(driver)
sleep(2)

#Encontrando o elemento inicial do slide
slide = driver.find_element(By.XPATH,'//span[@id="nc_1_n1z"]')

#Clicando e arrastando o slide
chain.click_and_hold(slide).move_by_offset(400,0).release().perform()

#Aguardando fim da automação
sleep(2)
input('Aguardado para encerrar')
driver.close()

