from selenium.webdriver.common.by import By

from Pages.BasePage import basePage


# This class contains webelements and methods for actions on chat bot window
class ChatBotPage():
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = ChatBotPage()
        return cls.instance

#getters for all webelements for the chatbot page    
    def getChatFrame(self): 
        basePage.get_driver().switch_to.frame("haptik-js-sdk")
        
    def getChatBubble(self):
        return basePage.get_driver().find_element(By.ID, 'my-app')
       
    def getChatMenu(self):
        return basePage.get_driver().find_element(By.CLASS_NAME, 'taskbox-tasks')

    def getViewMoreIcon(self):
        return basePage.get_driver().find_element_by_class_name("taskbox-show-more-title")

    def getChatMenuOptions(self):
        return basePage.get_driver().find_elements_by_class_name('task-title')
    
    def getChatBotName(self):
        return basePage.get_driver().find_element_by_xpath("//div[contains(@class,'slick-slide ')]")
    
    def getNextArrowIcon(self):
        return basePage.get_driver().find_element_by_css_selector(".slick-arrow.slick-next")
    
    def getKnowMoreText(self):
        return basePage.get_driver().find_element_by_xpath("//div[@class='slick-slide slick-active']//div[text()='Know More']")
    
    def getBotMessage1(self):
        return basePage.get_driver().find_element_by_xpath("//div[text()='Get in touch' and @class='qr-item']")
    
    def getBotMessage2(self):
        return basePage.get_driver().find_element_by_xpath("//div[text()='See an example' and @class='qr-item']")
    
    def getBotMessage3(self):    
        return basePage.get_driver().find_element_by_xpath("//div[text()='See another Bot' and @class='qr-item']")
        
    def getExampleMessage1(self):
        return basePage.get_driver().find_element_by_xpath("//div[text()='Get in touch' and @class='qr-item']")    
    
    def getExampleMessage2(self):
        return basePage.get_driver().find_element_by_xpath("//div[text()='Other options' and @class='qr-item']")   
        
    def getMenu(self):
        return basePage.get_driver().find_element_by_id("Path-2")
    
    def getCloseChatIcon(self):
        return basePage.get_driver().find_element_by_class_name("minimized-view  ")    
    

#All methods for chatbot page required to perform actions
                 
    def clickOnChatBotBubble(self):
        self.getChatFrame()
        basePage.clickOnElement(self.getChatBubble())   
        
    def validateChatMenu(self):
        basePage.get_driver().implicitly_wait(5)
        basePage.waitTillElementVisible(self.getChatMenu()) 
        
    def selectViewMore(self):
        basePage.get_driver().implicitly_wait(5)
        basePage.clickOnElement(self.getViewMoreIcon())    
        
    def selectChatMenuOption(self, option):
        basePage.get_driver().implicitly_wait(10)
        elements = self.getChatMenuOptions()
        for element in elements:
            if option in element.text:
                basePage.clickOnElement(element)
                break 
        
    def selectBot(self, botName):
        basePage.get_driver().implicitly_wait(10)
        element = self.getChatBotName()
        arrow = self.getNextArrowIcon()
        while botName not in element.text:
            basePage.clickOnElement(arrow)
            basePage.get_driver().implicitly_wait(10)
            element = self.getChatBotName()
        basePage.clickOnElement(self.getKnowMoreText())       

    def verifyOptionsForBot(self):
        basePage.waitTillElementVisible(self.getBotMessage1())
        basePage.waitTillElementVisible(self.getBotMessage2())
        basePage.waitTillElementVisible(self.getBotMessage3())
        
    def selectBotOption(self, option):
        element = basePage.get_driver().find_element_by_xpath("//div[text()=" + option + " and @class='qr-item']")
        basePage.clickOnElement(element)
        
    def verifyOptionsForExample(self):
        basePage.waitTillElementVisible(self.getExampleMessage1())
        basePage.waitTillElementVisible(self.getExampleMessage2())    
        
    def clickOnMenu(self):
        basePage.get_driver().implicitly_wait(5)
        basePage.clickOnElement(self.getMenu())
        
    def verifyBotTitle(self, title):
        element = basePage.get_driver().find_element_by_xpath("//div[@class='header-top-left-text-title' and text() = " + title + "]")
        basePage.waitTillElementVisible(element)
        basePage.highlightElement(element)
        
    def verifySubTitle(self, subTitle):
        element = basePage.get_driver().find_element_by_xpath("//div[@class='header-top-left-text-credentials' and text() = " + subTitle + "]")
        basePage.waitTillElementVisible(element)
        basePage.highlightElement(element)
        
    def verifyChatMessage(self, message):
        element = basePage.get_driver().find_element_by_xpath("//span[@class='pre-line-span' and text() = " + message + "]")
        basePage.waitTillElementVisible(element)
        basePage.highlightElement(element)
        
    def closeChatWindow(self):  
        basePage.clickOnElement(self.getCloseChatIcon())
        basePage.get_driver().quit()  

        
chatBotPage = ChatBotPage.get_instance()
