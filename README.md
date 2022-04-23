
# Useful commands:
- source ./venv/Scripts/activate
- scrapy shell "[url]"
- scrapy crawl [spider_name]

- scrapy crawl battlefield1 -O battlefield1stats.json
- scrapy crawl battlefield4 -O battlefield4stats.json
- scrapy crawl battlefield_hardline -O battlefield_hardline_stats.json

# Resources used for hosting
- https://www.youtube.com/watch?v=TFFtDLZnbSs&t=612s
- https://devcenter.heroku.com/articles/getting-started-with-python#provision-a-database


https://stackoverflow.com/questions/62351724/error-cannot-execute-truncate-table-in-a-read-only-transaction-in-heroku-post
begin;
set transaction read write;
COMMIT;  