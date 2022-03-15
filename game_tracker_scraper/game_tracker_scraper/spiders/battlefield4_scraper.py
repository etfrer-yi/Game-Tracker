import scrapy

DOMAIN = "https://battlefieldtracker.com"


class Battlefield4Scraper(scrapy.Spider):
    name = "battlefield4"

    def start_requests(self):
        urls = ["https://battlefieldtracker.com/bf4/leaderboards/all"]
        urls += [
            f"https://battlefieldtracker.com/bf4/leaderboards/all/score?page={page}"
            for page in range(2, 21)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_scoreboard)

    def parse_scoreboard(self, response):
        for idx, player_record in enumerate(response.css("tr")):
            player_record_fields = player_record.css('td').getall()
            if len(player_record_fields) == 4:
                player_info = {
                    'Rank': int(self.convert_numerical_str_to_num(
                        player_record.css('td::text').getall()[0].replace(",", ""))),
                    'Gamer': player_record.css('td')[1].css("a::text").get(),
                    'Game Score': self.convert_numerical_str_to_num(
                        player_record.css('td')[2].css("div.pull-right::text").get()),
                    'Games': self.convert_numerical_str_to_num(player_record.css('td::text').getall()[-1])
                }
                player_profile_url = player_record.css("td")[1].css("a::attr(href)").get()
                if player_profile_url is not None:
                    player_profile_url = DOMAIN + player_profile_url
                    yield scrapy.Request(player_profile_url, callback=self.parse_player_profile,
                                         meta={'player_info': player_info})

    def parse_player_profile(self, response):
        # sometimes the website has trouble downloading data due to exceeding INT_MAX, so an alert shows up
        if response.css(".alert"):
            return

        relevant_stats = response.css(".table-condensed tr span.pull-right::text").getall()
        xpath_beginning = "//th[contains(text(), "
        xpath_ending = ")]/following-sibling::td[1]/following-sibling::td[1]//span/text()"
        player_info = response.meta.get("player_info")
        yield {
            'Rank': player_info['Rank'],
            'Gamer': player_info['Gamer'],
            'Game Score': player_info['Game Score'],
            'Games': player_info['Games'],
            'Score/min': self.convert_numerical_str_to_num(relevant_stats[2]),
            'Kill Ratio': self.convert_numerical_str_to_num(response.xpath(f"{xpath_beginning}'K/D'{xpath_ending}")
                                                            .getall()[0], False),
            'Win Percent': self.convert_numerical_str_to_num(response.xpath(f"{xpath_beginning}'Win %'{xpath_ending}")
                                                             .getall()[0], False) / 100,
            'BTR Score': self.convert_numerical_str_to_num(response.xpath(f"{xpath_beginning}'BTR Score'{xpath_ending}")
                                                           .getall()[0]),
            'Hours Played': self.convert_numerical_str_to_num(relevant_stats[1][:-1]),
        }

    def convert_numerical_str_to_num(self, numerical_str, round_int=True):
        processed_str = numerical_str.replace("\r\n", "").replace(",", "").replace("%", "").strip()
        if round_int:
            return round(int(processed_str))
        else:
            return round(float(processed_str), 3)

