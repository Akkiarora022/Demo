from selenium import webdriver
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


# This class contains basic selenium methods to be used globally
class BasePage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = BasePage()
        return cls.instance
    
    def __init__(self):
        pathToChromeExecutable = 'Provide path of chrome driver here'
        self.driver = webdriver.Chrome(pathToChromeExecutable)
        self.driver.maximize_window()
        
    def get_driver(self):
        return self.driver    
    
    def loadWebsite(self):
        self.driver.get('http://haptik.ai/')
        
    def waitTillElementVisible(self, element):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of(element))
        
    def clickOnElement(self, element):
        self.waitTillElementVisible(element)
        element.click()    
        
    def highlightElement(self, element):
        self.get_driver().execute_script("arguments[0].setAttribute('style', 'background: green; border: 1px solid black;');", element)       

    
basePage = BasePage.get_instance()    
 
