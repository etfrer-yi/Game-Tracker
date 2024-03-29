<div align="center">

# Game-Tracker

</div>

<div align="center">

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/etfrer-yi/Game-Tracker?color=blue)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/etfrer-yi/Game-Tracker?color=red)
![GitHub language count](https://img.shields.io/github/languages/count/etfrer-yi/Game-Tracker?color=purple)
![GitHub top language](https://img.shields.io/github/languages/top/etfrer-yi/Game-Tracker?color=orange)

</div>

<div align="center">

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript Badge](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000&style=for-the-badge)
![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)
![pandas Badge](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=fff&style=for-the-badge)
![Plotly Badge](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=fff&style=for-the-badge)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

</div>

# Introduction
This is a Django project meant to display player records and data analytics results from 3 Battlefield games: Battlefield 1, Battlefield 4, and Battlefield Hardline. The data were scraped in the `game_tracker_scraper` folder using Python's Scrapy. Its source is Battlefield Leaderboards that are sorted by Game Score: https://battlefieldtracker.com/bf4/leaderboards/all, https://battlefieldtracker.com/bf1/leaderboards/all/Score, and https://battlefieldtracker.com/bfh/leaderboards/all. The final website is hosted at **https://yihengwang-game-tracker.herokuapp.com/**   

# Installation Notes
To have a local version of the project running,
1. Clone the repository into a local directory.
2. Run `pip install -r requirements.txt`, or consider setting up a virtual environment (in PyCharm, for example) to sync up with the dependencies.
3. Download PostgreSQL (14.1 or 14.2). Take a look at the `configurations.env` file and set up the database according to its configurations. Create 3 tables within the `GameTracker` database: `Battlefield1Stats`, `Battlefield4Stats`, and `BattlefieldHardlineStats`.
4. Navigate to the `game_tracker_scraper` directory and run `postgres_migration.py`. This will populate the database based on the scraped data contained in the `.json` files.
5. Run `python manage.py runserver` to ensure that the project can be run. 

# Demo
https://github.com/etfrer-yi/Game-Tracker/assets/77317763/462dd453-0464-408b-a540-d6d709ccd45a


# Data scraping
To re-scrape the data from Battlefield Leaderboards with the latest changes, navigate to the `game_tracker_scraper` directory and run the following commands to repopulate the `.json` files.
```
scrapy crawl battlefield1 -O battlefield1stats.json
scrapy crawl battlefield4 -O battlefield4stats.json
scrapy crawl battlefield_hardline -O battlefield_hardline_stats.json
```

# Resources used for hosting
- https://www.youtube.com/watch?v=TFFtDLZnbSs&t=612s
- https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database

# Running project locally
```
source venv/Scripts/activate
python manage.py runserver
```
