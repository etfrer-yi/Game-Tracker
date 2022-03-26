import scrapy

class BattlefieldScraper(scrapy.Spider):
    def convert_numerical_str_to_num(self, numerical_str, round_int=True):
        processed_str = numerical_str.replace("\r\n", "").replace(",", "").replace("%", "").strip()
        if round_int:
            return round(int(processed_str))
        else:
            return round(float(processed_str), 3)

    def get_console_platform(self, platform):
        if "xbox" in platform:
            return "xbox"
        elif "ps" in platform:
            return "psn"
        else:
            return platform