from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
s=Service(ChromeDriverManager().install())
# DECLARE WINDOW
window = Tk()
# SET WINDOW TITLE
window.title("EmailGenerator")
# BROWSER
options = webdriver.ChromeOptions()
options.headless = True
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
driver = webdriver.Chrome(service=s, options=options)
# PASSWORD
driver.get('https://www.dashlane.com/fr/features/password-generator')
Password = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div/div[2]/div/div[1]/div/output').text
# FR.EMAILFAKE.COM
options.headless = False
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://fr.emailfake.com/')
Username = driver.find_element(By.XPATH, '//*[@id="userName"]').get_attribute('value')
DomainName= driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[1]/input[2]').get_attribute('value')
Email = '{}@{}'.format(Username, DomainName)
# PRINT DATA
lbl1=Label(window, text=Email)
lbl2=Label(window, text=Password)
lbl1.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
def Button1Action():
    window.clipboard_clear()
    window.clipboard_append(Email)
def Button2Action():
    window.clipboard_clear()
    window.clipboard_append(Password)
button1=Button(text='Copy', command=Button1Action)
button1.grid(column=1, row=0)
button2=Button(text='Copy', command=Button2Action)
button2.grid(column=1, row=1)
window.mainloop()