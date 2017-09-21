from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import yaml

driverLocation = 'D:/Program Files/Python/chromedriver_win32/chromedriver'
loginInfoLocation = 'D:/Program Files/Python/doc/ignore.yml'

# Initialise the web driver and send it to the gmail login page
driver = webdriver.Chrome(driverLocation)
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

# Read in external login data
conf = yaml.load(open(loginInfoLocation))
email = conf['user']['email']
pwd = conf['user']['password']

# Locate email field and enter stored email address
emailField = driver.find_element_by_name('identifier')
emailField.send_keys(email)
emailField.send_keys(Keys.RETURN)

# Necessary delay for following page to load
sleep(1)
 
 # Locate password field and enter stored password
passField = driver.find_element_by_name('password')
passField.send_keys(pwd)
passField.send_keys(Keys.RETURN)