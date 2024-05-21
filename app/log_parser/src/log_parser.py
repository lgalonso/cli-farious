import re

from .Constants import SQUID_PATTERN
from .utils import least_repeated_item, most_repeated_item

def match_pattern_from_line(log_line="1157689320.327   2864 10.105.21.199 TCP_MISS/200 10182 GET http://www.goonernews.com/ badeyek DIRECT/207.58.145.61 text/html", pattern=SQUID_PATTERN):
    """Returns dict with fields of a log line with a specific pattern.

        Args:
            log_line: line from log file to parse.
            pattern: specific line pattern

        Returns:
            dict with the different fields of a log line.
    """

    match = re.search(pattern, log_line)

    if match:
        dict = match.groupdict()
        return dict
    else:
        #Log somewhere the unmatched line to debug and adapt pattern
        return None


def get_ips_from_log(path="/home/dev/Downloads/access.log"):
    """Returns a list of all IPs in a log file.

        Args:
            path: path location of log file.

        Returns:
            list of IPs.
    """

    ip_list = []
    print("Processing...")
    with open(path, 'r') as file:
        for line in file:
            if match_pattern_from_line(line, SQUID_PATTERN) != None:
                ip_list.append(match_pattern_from_line(line, SQUID_PATTERN)["client_ip_address"])
    return ip_list

print(most_repeated_item(get_ips_from_log()))
print(least_repeated_item(get_ips_from_log()))