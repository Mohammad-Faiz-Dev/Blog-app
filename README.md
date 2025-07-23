# Flask Blog App 📝

A simple Flask web application that displays blog posts dynamically fetched from a public API. This project demonstrates server-side rendering, routing, and clean HTML/CSS styling.

---

## 🚀 Features

- Home page with a list of blog posts (fetched via external API)
- Individual blog post pages with full content
- Responsive UI using plain HTML & CSS
- Clean routing with Flask
- Basic separation of concerns (templates, routes, logic)

---

## 🛠️ Tech Stack

- **Backend**: [Flask](https://flask.palletsprojects.com/)
- **Frontend**: HTML, CSS (with media queries for responsiveness)
- **Data Source**: Public API from [npoint.io](https://www.npoint.io)
- **Tools Used**:
  - Python 3.x
  - `requests` library for API calls
  - Jinja2 templating via Flask

---

## 📂 Project Structure
.
├── app.py
├── templates/
│ ├── home.html
│ ├── blog_1.html
│ ├── blog_2.html
│ └── blog_3.html
├── static/
│ └── (optional: stylesheets or assets)
└── README.md

📌 Notes
All blog content is loaded live from the API (https://api.npoint.io/971c9cfc653c1062838f)

No database is used in this version (API acts as the data store)

Each blog page is routed via Flask (e.g., /blog/1, /blog/2, etc.)

📸 Screenshots

Homepage
<img width="1920" height="1080" alt="My-Blog_site" src="https://github.com/user-attachments/assets/22dccb2e-509d-4da7-801b-bf74102f29d2" />
