from selenium import webdriver

# before all
def before_all(context):
   context.driver = webdriver.Chrome()
# before every scenario
def before_scenario(scenario, context):
   print('Before scenario executed')
# after every feature
def after_feature(scenario, context):
   print('After feature executed')
# after all
def after_all(context):
   context.driver.quit()