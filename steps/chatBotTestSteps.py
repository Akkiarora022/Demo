from behave import given, when, then

from Pages.BasePage import basePage 
from Pages.ChatBotPage import chatBotPage


@given('I am on Haptik HomePage')
def load_home_page(context):
    basePage.loadWebsite()


@when('I click on the chat bubble')
def clcik_on_chat_bubble(context):
    chatBotPage.clickOnChatBotBubble()


@then('I validate the menu')
def validate_chat_menu(context):
    chatBotPage.validateChatMenu()


@when('I select view more')
def select_viewMore(context):
    chatBotPage.selectViewMore()


@when('I select "{option}" from chat options')
def select_chat_menu_option(context, option):
    chatBotPage.selectChatMenuOption(option)

 
@when('I choose "{bot}"')
def select_bot(context, bot):
    chatBotPage.selectBot(bot)

 
@then('I verify the given options after bot selection')
def verify_bot_options(context):
    chatBotPage.verifyOptionsForBot()


@when('I click on chat option {option}')
def select_bot_option(context, option):
    chatBotPage.selectBotOption(option)

 
@then('I verify the given options after choosing for example')
def verify_options_for_example(context):
    chatBotPage.verifyOptionsForExample()

 
@when('I click on the bottom Menu')
def click_on_menu(context):
    chatBotPage.clickOnMenu()

 
@then('I verify chat window title is {title}')
def verify_title(context, title):
    chatBotPage.verifyBotTitle(title)

 
@then('I verify chat window subtitle is {subTitle}')
def verify_subTitle(context, subTitle):
    chatBotPage.verifySubTitle(subTitle)

    
@then('I verify chat message is {message}')
def verify_chat_message(context, message):
    chatBotPage.verifyChatMessage(message)

     
@then('I close chat window')
def close_chat_window(context):
    chatBotPage.closeChatWindow()
