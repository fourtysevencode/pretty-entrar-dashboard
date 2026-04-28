import requests
from bs4 import BeautifulSoup
import json

session = requests.Session()

# login
username = "" # fill these
password = ""
res = session.post("https://entrar.in/login/auth/", data={
    'username':username,
    'password':password
})

# extract assignments
assignments = session.post(
    'https://entrar.in/pp_assignment/classassignment',
    data={'search_assignment': 'true'} # entrar loads the assignments via AJAX after the page loads via a POST request to the backend saying search_assignments = True
) # AJAX -> Asynchonous Jvacript and XML == allows updating of webpages by exchanging data with a server without reloading the page.

with open("assignments.html", "w") as f:
    f.write(assignments.text) # .text attribute returns the body as a string

with open("assignments.html", "r", encoding="utf-8") as f:
    content = f.read()

# initialize BeautifulSoup on the extracted HTML file and parsing
soup = BeautifulSoup(content, "html.parser")

# saving all assignment details
items = soup.find_all("a", class_="attachment_display", style="color: red;")

assignment_list = []
for item in items:
    title=item.get_text(strip=True) # inner text
    url = item["href"]
    assignment_list.append({"title": title, "url": url})
    print(f"{title}\n{url}\n")

# dumping to json
with open("assignments.json", "w", encoding="utf-8") as f:
    json.dump(assignment_list, f, indent=4)