import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

from jinja2 import Environment, PackageLoader, select_autoescape

# Initialize Jinja2 environment

env = Environment(
    loader=PackageLoader("app", "templates"),
    autoescape=select_autoescape()
)

load_dotenv()
app = Flask(__name__)

NAV_ITEMS = [
    {'name': 'Zidanni', 'url': '/', 'route': 'index'},
    {'name': 'Manav', 'url': '/manav', 'route': 'manav'},
    {'name': 'Deeptanshu', 'url': '/deeptanshu', 'route': 'deeptanshu'},
    {'name': 'Hobbies', 'url': '/hobbies', 'route': 'hobbies'}
]

def get_nav_data(current_route):
    nav_data = []
    for item in NAV_ITEMS:
        nav_item = item.copy()
        nav_item['is_current'] = (item['route'] == current_route)
        nav_data.append(nav_item)
    return nav_data


@app.route('/')
def index():
    nav_data = get_nav_data('index')
    template = env.get_template("profile.html")
    
    EXPERIENCE = [
        {'company': 'Independent', 'title': 'Software Developer', 'date': 'September 2024 – Present'},
        {'company': 'Elmhurst Care Center Nursing Home', 'title': 'Software Developer', 'date': 'July 2022 – August 2023'},
        {'company': 'NYU Tandon School of Engineering', 'title': 'Researcher and Game Developer', 'date': 'April 2022 – June 2024'},
    ]

    EDUCATION = [
        {'school': 'Stevens Institute of Technology', 'title': 'Bachelor of Science in Computer Science'},
    ]
    
    return template.render(title="Zidanni Clerigo", url=os.getenv("URL"), nav_items=nav_data, profile_picture="./static/img/zidanni.jpg", education=EDUCATION, experience=EXPERIENCE, map="./static/img/zidanni-map.jpg", about_me_text="Hello! I'm Zidanni Clerigo, an incoming second year Computer Science student at Stevens Institute of Technology. I'm super passionate about building projects and pitching them to other people! Deployment and maintenance has always been a roadblock for me so I'm very excited to be in the Production Engineering track.")


@app.route('/manav')
def manav():
    nav_data = get_nav_data('manav')
    template = env.get_template("profile.html")

    EXPERIENCE = [
        {'company': 'CN', 'title': 'Operational Technology Intern', 'date': 'May 2024 - Aug 2024'},
        {'company': 'Jam', 'title': 'Full Stack Developer Intern', 'date': 'Dec 2023 - Feb 2024'},
        {'company': 'University of Alberta', 'title': 'Research Assistant', 'date': 'May 2023 - Aug 2023'},
    ]

    EDUCATION = [
        {'school': 'University of Alberta', 'title': 'Electrical Engineering'},
        {'school': 'Old Scona Academic', 'title': 'International Baccalaureate Diploma'},
    ]

    return template.render(title="Manav", url=os.getenv("URL"), nav_items=nav_data, profile_picture="./static/img/manav.jpg", education=EDUCATION, experience=EXPERIENCE, map="./static/img/manav-map.png", about_me_text="Hi there! I'm Manav, a third-year Electrical Engineering student at the University of Alberta. Planning, building, and deploying projects has been a pursuit of mine for a long time, and I'm excited to be part of the Production Engineering track. I love working on projects that involve hardware and software integration, and I'm always looking for new challenges to tackle.")

@app.route('/deeptanshu')
def deeptanshu():
    nav_data = get_nav_data('deeptanshu')
    return render_template('deeptanshu.html', title="Deeptanshu Sankhwar", url=os.getenv("URL"), nav_items=nav_data)


@app.route('/hobbies')
def hobbies():
    nav_data = get_nav_data('hobbies')
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), nav_items=nav_data)
