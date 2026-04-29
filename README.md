# Pretty Entrar Assignments Dashboard

> User-friendly assignments dashboard for all Entrar users! Check it out at [assignments.ronakbuilds.tech](https://assignments.ronakbuilds.tech)

## The Problem

It's difficult to find entrar assignments with ease, especially if you're in a hurry. They are hidden behind multiple pages and dropdowns. Pretty Entrar Dashboard comes in and saves you from all the trouble. Simply login with your credentials and find all assignments instantly! No hunting needed anymore.

## Structure

```
pretty-entrar-dashboard/
├── templates/
│   └── index.html
├── utils/
│   └── assignment_extractor.py
├── .gitignore
├── app.py
├── assignment_extractor_pipeline.py
├── README.md
└── requirements.txt
```

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                             PYTHON BACKEND                          │
│                                                                     │
│   ┌──────────────────────┐                                          │
│   │   requests.Session() │                                          │
│   │                      │                                          │
│   │  POST /login/auth/   │──────────────────────►  entrar.in       │
│   │  { username, pass }  │                                          │
│   │                      │◄──────────────────────  Set-Cookie:     │
│   │  session cookie ✓    │                          session_id      │
│   └──────────┬───────────┘                                          │
│              │                                                       │
│              │ session.post(/pp_assignment/classassignment)          │
│              │ { search_assignment: true }                           │
│              │                                                       │
│              ▼                                                       │
│   ┌──────────────────────┐                                          │
│   │   BeautifulSoup      │◄──── raw HTML (AJAX response)            │
│   │                      │                                          │
│   │  find_all("a",       │                                          │
│   │   class_=            │                                          │
│   │  "attachment_display"│                                          │
│   │   style="color:red") │                                          │
│   └──────────┬───────────┘                                          │
│              │                                                       │
│              │  [ { title, url }, { title, url }, ... ]             │
│              │                                                       │
│              ▼                                                       │
│   ┌──────────────────────┐                                          │
│   │   FastAPI            │                                          │
│   │                      │                                          │
│   │  POST                │                                          │
│   │  /fetch-assignments  │                                          │
│   │                      │                                          │
│   │  return assignment   │                                          │
│   │  _list  →  JSON ✓    │                                          │
│   └──────────┬───────────┘                                          │
│              │                                                       │
└──────────────┼──────────────────────────────────────────────────────┘
               │
               │  HTTP  application/json
               │
               ▼
   ┌───────────────────────────────────────────────┐
   │   https://assignments.ronakbuilds.tech/       │
   │                                               │
   │   index.html                                  │
   │   fetch("/fetch-assignments")                 │
   │                                               │ 
   │   renderCards(data)                           │
   │   [ PDF ]  title  ↗                           │
   │   [DOCX]  title  ↗                            │
   └───────────────────────────────────────────────┘
```

## Running locally

To run the project on your local machine, open your terminal and run the following commands:

```bash
git clone https://github.com/fourtysevencode/pretty-entrar-dashboard.git

cd pretty-entrar-dashboard

uvicorn app:app --reload
```

Update `base` in templates/index.html to `http://localhost:8000` (line 343)

Then head to `http://localhost:8000` on your preferred web browser.

## Endpoints

| Endpoint | Description |
| :--- | :--- |
| `/` | Homepage |
| `/fetch-assignments` | Runs the fetch assignment pipeline and returns a structured result |

## License

MIT

*with 💗 from fourtysevencode*
