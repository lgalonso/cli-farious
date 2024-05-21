import re
from collections import Counter

SQUID_PATTERN = r"^(?:(?P<timestamp>\d+\.\d+)|-)\s+(?:(?P<response_header>(?:(\d+)|(-\d+)))|-)\s+(?:(?P<client_ip_address>\d+\.\d+\.\d+\.\d+)|-)\s+(?P<http_response_code>(?:(\w+)|-)/(?:(\d+)|-))\s+(?:(?P<response_size_bytes>\d+)|-)\s+(?:(?P<method>\w+)|-)\s+(?:(?P<url>.+)|-)\s+(?:(?P<user>\w+)|-)\s+(?P<access_type>\w+)/(?:(?P<destination_ip>\d+\.\d+\.\d+\.\d+)|-)(?:\s*(?P<content>.*))?\s*$"

#Receives a line from a log file and a pattern
#Returns a dict with the different fields of a log line
#By default pattern passed is a squid proxy line pattern

def match_pattern_from_line(log_line="1157689320.327   2864 10.105.21.199 TCP_MISS/200 10182 GET http://www.goonernews.com/ badeyek DIRECT/207.58.145.61 text/html", pattern=SQUID_PATTERN):
    
    match = re.search(pattern, log_line)

    if match:
        dict = match.groupdict()
        return dict
    else:
        #Log somewhere the unmatched line to debug and adapt pattern
        return None

#Receives a path to a log file
#Returns a dict with the different IPs from the log

def get_ips_from_log(path="/home/dev/Downloads/access.log"):
    ip_list = []
    #open the file
    print("Processing...")
    with open(path, 'r') as file:
        for line in file:
            
            ip_list.append(match_pattern_from_line(line, SQUID_PATTERN)["client_ip_address"]) if match_pattern_from_line(line, SQUID_PATTERN) != None else ""
    print(len(ip_list))
    return ip_list

print(Counter(get_ips_from_log()).most_common(1)[0][0])