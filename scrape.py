from tkinter.font import names
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from colorama import init
import time
import threading
from pyfiglet import figlet_format
from termcolor import cprint
init()

cprint(figlet_format("REPO FINDER", font='starwars'),
       'yellow', attrs=['bold'])

username = str(input(f"enter the username that you want to find: {Fore.BLACK}"))
print(f"{Fore.YELLOW} Finding repos [+]")


print("*")
time.sleep(1)
print("**")
time.sleep(1)
print("***")



base_url = f"https://github.com/{username}"
repository_url = f"https://github.com/{username}?tab=repositories"
html_base = requests.get(base_url)
if html_base.status_code == 404:
    print(f"{Fore.RED} Could not found the username [!]")
else:
    print(f"{Fore.GREEN} Found The Username = {username} [+]")
    repo_html=requests.get(repository_url)
    soup = BeautifulSoup(repo_html.text,"lxml")
    repos = soup.find_all("li",class_ = "col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source")
    for alt_repo in repos:
        class1 =soup.find_all("div",class_="col-10 col-lg-9 d-inline-block")
        for element in class1:
            alt_name_class = soup.find_all("h3",class_="wb-break-all")
    
size = len(alt_name_class)
print(f"{Fore.MAGENTA} There is {size} repos!")

start = 0
while start <=size-1:
    html_code = alt_name_class[start]
    start = start+1

   
for a in soup.find_all('a', href=True):
        if a["href"].startswith(f"/{username}/"):
           print("*******************")
           print(a["href"])
           
