import re

#From input: path file we need to parse a log file into fields

def match_pattern_from_line(line):
    
    log_line = line

    pattern = r"^(?P<timestamp>\d+\.\d+)\s+(?P<response_header>\d+)\s+(?P<client_ip_address>\d+\.\d+\.\d+\.\d+)\s+(?P<http_response_code>\w+/\d+)\s+(?P<response_size_bytes>\d+)\s+(?P<method>\w+)\s+(?P<url>.+)\s+(?P<user>\w+)\s+(?P<access_type>\w+)/(?P<destination_ip>\d+\.\d+\.\d+\.\d+)(?:\s*(?P<content>.*))?\s*$"

    match = re.search(pattern, log_line)

    if match:
        dict = match.groupdict()
        print(dict)
    else:
        print("Log line does not match the pattern.")