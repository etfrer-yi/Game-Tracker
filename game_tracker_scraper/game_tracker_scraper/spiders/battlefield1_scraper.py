import scrapy

DOMAIN = "https://battlefieldtracker.com"


class Battlefield1Scraper(scrapy.Spider):
    name = "battlefield1"

    def start_requests(self):
        urls = ["https://battlefieldtracker.com/bf1/leaderboards/all/SiteScore"]
        urls += [
            f"https://battlefieldtracker.com/bf1/leaderboards/all/SiteScore?page={page}"
            for page in range(2, 5)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_scoreboard)

    def parse_scoreboard(self, response):
        for idx, player_record in enumerate(response.css("tr")):
            player_record_fields = player_record.css('td').getall()
            if len(player_record_fields) == 4:
                player_info = {
                    'Rank': self.convert_numerical_str_to_num(
                        player_record.css('td::text').getall()[0].replace(",", "")),
                    'Gamer': player_record.css('td')[1].css("a::text").get(),
                    'BTR Score': self.convert_numerical_str_to_num(
                        player_record.css('td')[2].css("div.pull-right::text").get()),
                    'Games': self.convert_numerical_str_to_num(player_record.css('td::text').getall()[-1])
                }
                player_profile_url = player_record.css("td")[1].css("a::attr(href)").get()
                if player_profile_url is not None:
                    player_profile_url = DOMAIN + player_profile_url
                    yield scrapy.Request(player_profile_url, callback=self.parse_player_profile,
                                         meta={'player_info': player_info})

    def parse_player_profile(self, response):
        if response.css(
                ".alert"):  # sometimes the website has trouble downloading data due to exceeding INT_MAX, so an alert shows up
            return

        relevant_stats = response.css("div.stats div.stat div.value::text").getall()
        player_info = response.meta.get("player_info")
        yield {
            'Rank': player_info['Rank'],
            'Gamer': player_info['Gamer'],
            'BTR Score': player_info['BTR Score'],
            'Games': player_info['Games'],
            'Score/min': self.convert_numerical_str_to_num(relevant_stats[1]),
            'Kill Ratio': self.convert_numerical_str_to_num(relevant_stats[2]),
            'Win Percent': self.convert_numerical_str_to_num(relevant_stats[3]) / 100,
            'Game Score': self.convert_numerical_str_to_num(relevant_stats[4]),
            'Hours Played': self.get_hours_from_play_time(relevant_stats[5]),
        }

    def convert_numerical_str_to_num(self, numerical_str):
        return round(float(numerical_str.replace("\r\n", "").replace(",", "").replace("%", "").strip()), 3)

    def get_hours_from_play_time(self, play_time):
        play_time = play_time.split()
        hours = 0
        for day_hour_min_sec_type in play_time:
            time_value = day_hour_min_sec_type[:-1]  # excludes the last character, which is 'd', 'h', 'm', or 's'
            if "d" in day_hour_min_sec_type:
                hours += 24 * float(time_value)
            elif "h" in day_hour_min_sec_type:
                hours += float(time_value)
            elif "m" in day_hour_min_sec_type:
                hours += float(time_value) / 60
            elif "s" in day_hour_min_sec_type:
                hours += float(time_value) / 3600
        return round(hours, 3)
