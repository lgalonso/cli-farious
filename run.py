from app.log_parser import parse_line_with_pattern, get_ips_from_log, get_events_per_second, get_total_bytes_exchanged
from app.log_parser.src.utils import least_repeated_item, most_repeated_item

print("Most frequent IP: " + most_repeated_item(get_ips_from_log()))
print("Least frequent IP: " + least_repeated_item(get_ips_from_log()))
print("EPS: " + str(get_events_per_second()))
print("Total amount of bytes exchanged: " + str(get_total_bytes_exchanged()))