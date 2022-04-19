import os
import time
import sys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from os import system
system("title " + 'TwitterFlooder')
options = webdriver.ChromeOptions()
options.add_argument("--nogpu")
options.add_argument('--headless')
driver=webdriver.Chrome("chromedriver.exe",options=options)
os.system('cls')
os.system('color d')

print("""
▄▄▄█████▓ █     █░ ██▓▄▄▄█████▓▄▄▄█████▓▓█████  ██▀███       █████▒██▓     ▒█████   ▒█████  ▓█████▄ ▓█████  ██▀███  
▓  ██▒ ▓▒▓█░ █ ░█░▓██▒▓  ██▒ ▓▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒   ▓██   ▒▓██▒    ▒██▒  ██▒▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒█░ █ ░█ ▒██▒▒ ▓██░ ▒░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒   ▒████ ░▒██░    ▒██░  ██▒▒██░  ██▒░██   █▌▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ░█░ █ ░█ ░██░░ ▓██▓ ░ ░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄     ░▓█▒  ░▒██░    ▒██   ██░▒██   ██░░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░░██▒██▓ ░██░  ▒██▒ ░   ▒██▒ ░ ░▒████▒░██▓ ▒██▒   ░▒█░   ░██████▒░ ████▓▒░░ ████▓▒░░▒████▓ ░▒████▒░██▓ ▒██▒
  ▒ ░░   ░ ▓░▒ ▒  ░▓    ▒ ░░     ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░    ▒ ░   ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░      ▒ ░ ░   ▒ ░    ░        ░     ░ ░  ░  ░▒ ░ ▒░    ░     ░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
  ░        ░   ░   ▒ ░  ░        ░         ░     ░░   ░     ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░  ░    ░     ░░   ░ 
             ░     ░                       ░  ░   ░                   ░  ░    ░ ░      ░ ░     ░       ░  ░   ░     
                                                                                             ░                      
                TwitterFlooder is a tool to spam/flood a tweet! created by github.com/ReallyFighter

""")
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

email = typingInput("""What's your email?
""")
password = typingInput ("""what's  your password?
""")
username = typingInput ("""What's your username?(ex:@elonmusk)
""")
tweet = typingInput("""what's the tweet you want to flood?
""")
nombre = typingInput("""How many tweets do you want to send?
""")
content=typingInput("""what do you want to send?
""")
os.system('cls')
typingPrint('''trying to connect with your account...
''')
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
driver.get("https://twitter.com/i/flow/login")
time.sleep(3)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input').click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input").send_keys(email)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div').click()
time.sleep(1)
try:
  driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").click()
  driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys(username)
  driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
except:
  pass
time.sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(password)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
time.sleep(2)
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
os.system('cls')
typingPrint('sucessfully connected as '+username)
sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
driver.execute_script("window.open('about:blank','secondtab');")
driver.switch_to.window("secondtab")
driver.get(tweet)
time.sleep(2)
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
typingPrint("""
sending tweets...""")
#sys.stdout = open(os.devnull, "w")
#sys.stderr = open(os.devnull, "w")
count = 1
while count < int(nombre) :
    system("title " + 'TwitterFlooder︱'+str(count)+" tweets sent︱connected as "+str(username))
    driver.refresh()
    time.sleep(1)
    driver.refresh()
    driver.refresh()
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="reply"]'))))
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div').send_keys(content,' ',count)
    time.sleep(2)
    driver.find_element(By.XPATH,'//div[@data-testid="tweetButton"]').click()
    time.sleep(1)
    count = count + 1
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
os.system('cls')
typingPrint('''Finished!
''')
typingPrint('Sent all tweets, dont forget to check github.com/ReallyFighter to more tool like that!')
