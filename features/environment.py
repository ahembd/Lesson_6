from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application

def browser_init(context):

    context.driver.maximize_window()

    context.driver.implicitly_wait(4)
    context.wait = WebDriverWait(context.driver, 15)
    print('assigning context.app to Application(context.driver')
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    def before_step(context, step):
        pass
def after_step(context, step):
    if step.status == 'failed':
        # Screenshot:
        # context.driver.save_screenshot(f'step_failed_{step}.png')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()