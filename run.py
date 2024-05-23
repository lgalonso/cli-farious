from app.log_parser import match_pattern_from_line, get_ips_from_log, get_events_per_second
from app.log_parser.src.utils import least_repeated_item, most_repeated_item

line = "1157689320.327   2864 10.105.21.199 TCP_MISS/200 10182 GET http://www.goonernews.com/ badeyek DIRECT/207.58.145.61 text/html"

most_repeated_item(get_ips_from_log())