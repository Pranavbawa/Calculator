import requests
from bs4 import BeautifulSoup as bs

url = "https://github.com/"
user = input("Please enter the user for search for profile pic: ").replace(" ", "")
profile = url + user
git_request = requests.get(profile)
print(git_request)
soup = bs(git_request.content, 'html.parser')
profile_pic = soup.find('img', {'alt': 'Avatar'})['src']
print(profile_pic)
