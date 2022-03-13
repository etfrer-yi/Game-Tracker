import scrapy

class Battlefield1Scraper(scrapy.Spider):
    name = "battlefield1"

    def start_requests(self):
        # start_urls = ["https://battlefieldtracker.com/bf1/leaderboards/all/SiteScore"]
        # start_urls += [
        #     f"https://battlefieldtracker.com/bf1/leaderboards/all/SiteScore?page={page}"
        #     for page in range(2, 51)
        # ]
        urls = [
            "https://battlefieldtracker.com/bf1/leaderboards/all/SiteScore"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for idx, player_record in enumerate(response.css("tr")):
            player_record_fields = player_record.css('td').getall()
            player_record_fields
            if len(player_record_fields) == 4:
                yield {
                    'Rank': int(player_record.css('td::text').getall()[0]),
                    'Gamer': player_record.css('td')[1].css("a::text").get(),
                    'BTR Score': int(player_record.css('td')[2].css("div.pull-right::text").get()
                                     .replace("\r\n", "").replace(",", "").strip()),
                    'Games': int(player_record.css('td::text').getall()[-1])
                }
                print(1)



# For a row of valid record,
#  player_record.css('td') returns 4 Selectors
#  player_record.css('td').getall() returns 4 innerHTMLs (kind of) as str
#  player_record.css('td::text') returns 7 Selectors, potentially the td's along with their children
#  player_record.css('td::text').getall() returns 7 selectors but with the innerHTMLs (kind of) as str