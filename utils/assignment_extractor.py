import requests
from bs4 import BeautifulSoup

def extract_assignments(username, password):

    session = requests.Session()

    session.post("https://entrar.in/login/auth/", data={
        'username': username,
        'password': password
    })

    assignments = session.post(
        'https://entrar.in/pp_assignment/classassignment',
        data={'search_assignment': 'true'}
    )

    soup = BeautifulSoup(assignments.text, "html.parser")

    items = soup.find_all("a", class_="attachment_display", style="color: red;")

    assignment_list = []
    for item in items:
        title = item.get_text(strip=True)
        url = item["href"]
        assignment_list.append({"title": title, "url": url})

    return assignment_list