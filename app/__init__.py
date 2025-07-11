import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import MySQLDatabase
from jinja2 import Environment, PackageLoader, select_autoescape
from playhouse.shortcuts import model_to_dict

# Initialize Jinja2 environment

env = Environment(
    loader=PackageLoader("app", "templates"),
    autoescape=select_autoescape()
)

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

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
    
    return template.render(title="Zidanni Clerigo", url=os.getenv("URL"), map="./static/img/zidanni-map.jpg", nav_items=nav_data, profile_picture="./static/img/zidanni.jpg", education=EDUCATION, experience=EXPERIENCE, about_me_text="Hello! I'm Zidanni Clerigo, an incoming second year Computer Science student at Stevens Institute of Technology. I'm super passionate about building projects and pitching them to other people! Deployment and maintenance has always been a roadblock for me so I'm very excited to be in the Production Engineering track.")


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
    template = env.get_template("profile.html")

    EXPERIENCE = [
        {'company': 'CU Boulder', 'title': 'Research Assistant', 'date': 'December 2024 - May 2025'},
        {'company': 'Remaster.IO', 'title': 'Software Engineer', 'date': 'June 2022 - Aug 2024'},
        {'company': 'Vedantu', 'title': 'Software Engineer', 'date': 'June 2021 - June 2022'},
    ]

    EDUCATION = [
        {'school': 'University of Colorado, Boulder', 'title': 'Computer Science'},
    ]
    
    return template.render(title="Deeptanshu", url=os.getenv("URL"), nav_items=nav_data, profile_picture="./static/img/deeptanshu.jpg", education=EDUCATION, experience=EXPERIENCE, map="./static/img/deeptanshu-map.jpg", about_me_text="I am Deeptanshu Sankhwar, I study Computer Science at the University of Colorado, Boulder. I am passionate about full stack development, distributed systems and infrstructures. I'm thrilled to join the MLH Fellowship's Production Engineering track to sharpen my skills in infrastructure, reliability, and DevOps while contributing to high-impact systems. I actively contribute to open source and have worked on projects like OpenStreetMap, Langfuse, and more focusing on performance, scalability, and developer experience. Open source excites me because it blends collaboration, transparency, and real-world engineering challenges. Technically, I enjoy working with Go, TypeScript, and Python to build scalable systems and automate complex workflows.")


@app.route('/hobbies')
def hobbies():
    nav_data = get_nav_data('hobbies')
    
    # Manav's hobbies
    MANAV_HOBBIES = [
        {'title': 'Sports', 'about': 'I enjoy playing sports in my free time, from Soccer to Badminton!', 'icon': 'https://cdn-icons-png.flaticon.com/512/11438/11438126.png'},
        {'title': 'Gaming', 'about': 'Video games can be fun! You can sometimes catch me playing games from Paradox Studios or Rocket League!', 'icon': 'https://cdn-icons-png.flaticon.com/512/5260/5260498.png'},
        {'title': 'Movies & TV', 'about': 'I love a good movie or show! One of my favourite shows is Succession!', 'icon': 'https://thumbs.dreamstime.com/b/big-open-clapper-board-movie-reel-cinema-icon-set-movie-film-elements-flat-design-cinema-movie-time-flat-icons-f-95500226.jpg'},
    ]
    
    # Zidanni's hobbies
    ZIDANNI_HOBBIES = [
        {'title': 'Game Development', 'about': 'I like building story games in my free time and doing game jams.', 'icon': 'https://cdn-icons-png.flaticon.com/512/1005/1005141.png'},
        {'title': 'Reading', 'about': 'My favorite book series is the Three Body Problem. I also like reading fantasy like The Hobbit.', 'icon': 'https://cdn-icons-png.flaticon.com/512/2436/2436882.png'},
        {'title': 'Photography', 'about': 'I like taking goofy pictures of my friends lol!', 'icon': 'https://cdn-icons-png.flaticon.com/512/1042/1042390.png'},
    ]
    
    # Deeptanshu's hobbies
    DEEPTANSHU_HOBBIES = [
        {'title': 'Open Source', 'about': 'I actively contribute to open source projects in my free time.', 'icon': 'https://cdn-icons-png.flaticon.com/512/2111/2111432.png'},
        {'title': 'Hiking', 'about': 'I enjoy exploring nature and going on hikes in Colorado and biking in Boulder!', 'icon': 'https://cdn-icons-png.flaticon.com/512/71/71423.png'},
        {'title': 'Coding', 'about': 'I enjoy working with Go, TypeScript, and Python to build scalable systems.', 'icon': 'https://cdn-icons-png.flaticon.com/512/6132/6132221.png'},
    ]

    about_text = "We all have various hobbies and interests that help us recharge and grow outside of our professional lives. Here's a glimpse into what we enjoy doing in our free time."
    
    return render_template('hobbies.html', 
                          title="Our Hobbies", 
                          url=os.getenv("URL"), 
                          nav_items=nav_data, 
                          manav_hobbies=MANAV_HOBBIES,
                          zidanni_hobbies=ZIDANNI_HOBBIES,
                          deeptanshu_hobbies=DEEPTANSHU_HOBBIES,
                          about_me_text=about_text)


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.json['name']
    email = request.json['email']
    content = request.json['content']

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(post)
            for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }