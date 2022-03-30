import scrapy
from .battlefield_scraper import BattlefieldScraper

DOMAIN = "https://battlefieldtracker.com"


class Battlefield1Scraper(BattlefieldScraper):
    name = "battlefield1"

    def start_requests(self):
        urls = ["https://battlefieldtracker.com/bf1/leaderboards/all/Score"]
        urls += [
            f"https://battlefieldtracker.com/bf1/leaderboards/all/Score?page={page}"
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
                    player_info["Original Platform"] = player_profile_url.split("/")[-2]
                    player_info["Platform"] = self.get_console_platform(player_info["Original Platform"])
                    yield scrapy.Request(player_profile_url, callback=self.parse_player_profile,
                                         meta={'player_info': player_info})

    def parse_player_profile(self, response):
        # sometimes the website has trouble downloading data due to exceeding INT_MAX, so an alert shows up
        if response.css(".alert"):
            return

        relevant_stats = response.css("div.stats div.stat div.value::text").getall()
        player_info = response.meta.get("player_info")
        yield {
            'Rank': player_info['Rank'],
            'Gamer': player_info['Gamer'],
            'Game Score': player_info['Game Score'],
            'Games': player_info['Games'],
            'Platform': player_info['Platform'],
            'Original Platform': player_info['Original Platform'],
            # relevant_stats[0] is the content of an a tag
            'Score/min': self.convert_numerical_str_to_num(relevant_stats[1]),
            'Kill Ratio': self.convert_numerical_str_to_num(relevant_stats[2], False),
            'Win Percent': self.convert_numerical_str_to_num(relevant_stats[3], False) / 100,
            'BTR Score': self.convert_numerical_str_to_num(self.get_specific_selection(response, "SiteScore").get()),
            'Hours Played': self.get_hours_from_play_time(relevant_stats[5]),
            'Kills': self.convert_numerical_str_to_num(self.get_specific_selection(response, "Kills").get()),
            'Deaths': self.convert_numerical_str_to_num(self.get_specific_selection(response, "Deaths").get()),
            'Wins': self.convert_numerical_str_to_num(self.get_specific_selection(response, "Wins").get()),
            'Losses': self.convert_numerical_str_to_num(self.get_specific_selection(response, "Losses").get()),
            'Accuracy': self.convert_numerical_str_to_num(self.get_specific_selection(response, "AccuracyRatio").get(), False),
            'Flags Captured': self.convert_numerical_str_to_num(self.get_specific_selection(response, "FlagsCaptured").get()),
            'Flags Defended': self.convert_numerical_str_to_num(self.get_specific_selection(response, "FlagsDefended").get()),
            'Head Shots': self.convert_numerical_str_to_num(self.get_specific_selection(response, "HeadShots").get()),
        }

    def get_specific_selection(self, response, selection_name):
        return response.xpath(f"//div[@data-stat='{selection_name}']/text()")

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
