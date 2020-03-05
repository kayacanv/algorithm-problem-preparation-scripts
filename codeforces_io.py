## Get Inputs Outputs Avaiable from Codeforces. Not working Cf has changed
from bs4 import BeautifulSoup
import requests
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

url = input("Please enter the submission url: ")
problem_name = input("Please enter name of the problem: ")
dir_name = input("Please enter the io directory: ")

response = requests.get(url)
 
data = response.text
 
soup = BeautifulSoup(data, 'html.parser')
cnt = 1

if not os.path.isdir(os.path.join(os.getcwd(), dir_name)):
    os.mkdir(dir_name)

for inp in soup.findAll("div", {"class": "file input-view"}):
    
    inp = inp.find("pre").text
    
    if len(inp) > 0:
        
        print(cnt)
        
        with open(os.path.join(dir_name, problem_name + '.' + str(cnt) + '.gir'), "w") as f:
            f.write(inp)
        
        cnt += 1