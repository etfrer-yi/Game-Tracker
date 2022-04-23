
# Introduction
This is a Django project meant to display player records and data analytics results from 3 Battlefield games: Battlefield 1, Battlefield 4, and Battlefield Hardline. The data were scraped in the `game_tracker_scraper` folder using Python's Scrapy. Its source is Battlefield Leaderboards that are sorted by Game Score: https://battlefieldtracker.com/bf4/leaderboards/all, https://battlefieldtracker.com/bf1/leaderboards/all/Score, and https://battlefieldtracker.com/bfh/leaderboards/all. The final website is hosted at **https://yihengwang-game-tracker.herokuapp.com/**   

# Installation Notes
To have a local version of the project running,
1. Clone the repository into a local directory.
2. Run `pip install -r requirements.txt`, or consider setting up a virtual environment (in PyCharm, for example) to sync up with the dependencies.
3. Download PostgreSQL (14.1 or 14.2). Take a look at the `configurations.env` file and set up the database according to its configurations. Create 3 tables within the `GameTracker` database: `Battlefield1Stats`, `Battlefield4Stats`, and `BattlefieldHardlineStats`.
4. Navigate to the `game_tracker_scraper` directory and run `postgres_migration.py`. This will populate the database based on the scraped data contained in the `.json` files.
5. Run `python manage.py runserver` to ensure that the project can be run. 

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
