from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException


# Monitora o elemento selecionado a cada interval_minut minutos e dá trigger na classe Action
class monitor:

    def __init__(self, selection, action, interval_minut):

        self.__selection = selection
        self.__interval_sec = interval_minut * 60
        self.__is_active = True
        self.__last_occurence = ""

        while self.__is_active:
            try:

                options = Options()
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")

                driver = webdriver.Chrome(options=options)
                driver.implicitly_wait(10)
                driver.get(self.__selection.url)

                element = driver.find_element("xpath", self.__selection.xpath)
                if element.text != self.__selection.conteudo:
                    self.__last_occurence = element.text
                    action.trigger()

            except NoSuchElementException:
                print("Erro: O elemento selecionado não foi encontrado na página.")
            except TimeoutException:
                print("Erro: A página demorou demais para carregar")
            except WebDriverException:
                print("Erro: O navegador foi fechado ou perdeu a conexão.")
            except KeyboardInterrupt:
                print("\nInterrompido pelo usuário (Ctrl+C).")

            finally:
                driver.quit()

            sleep(self.__interval_sec + randint(0, 2) * 60)

    def stop(self):
        self.__is_active = False

    def resume(self):
        self.__is_active = True

    def change_interval(self, interval_minut):
        self.__interval_sec = interval_minut * 60

    @property
    def interval(self):
        return self.__interval_sec / 60

    @property
    def selection(self):
        return self.__selection

    @property
    def target_modified(self):
        return self.__target_modified
    
    @property
    def last_occurence(self):
        return self.__last_occurence
