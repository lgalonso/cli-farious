import re
import subprocess

from .Constants import *

def remove_empty_lines(input_file, output_file):
  """
  Removes all empty lines from an input file and writes the result to an output file.

  Args:
      input_file: Path to the file containing lines to be processed.
      output_file: Path to the output file where the filtered lines will be written.
  """
  try:

    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
      for line in in_file:
        if line.strip():  # Check if line is not empty after stripping whitespace
          out_file.write(line)

  except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")

def match_pattern_from_line(log_line = "1157689320.327   2864 10.105.21.199 TCP_MISS/200 10182 GET http://www.goonernews.com/ badeyek DIRECT/207.58.145.61 text/html", pattern = SQUID_PATTERN_EXTENDED_2):
    """Returns dict with fields of a log line with a specific pattern.

        Args:
            log_line: line from log file to parse.
            pattern: specific line pattern

        Returns:
            Dict with the different fields of a log line.
    """

    match = re.search(pattern, log_line)

    if match:
        dict = match.groupdict()
        return dict
    else:
        #Log somewhere the unmatched line to debug
        return None

def get_ips_from_log(path = "/home/dev/Downloads/access.log"):
    """Returns a list of all IPs in a log file.

        Args:
            path: path location of log file.

        Returns:
            List of IPs, or None if the file is empty or not found.
    """
    try:
        ip_list = []

        print("Processing...")

        with open(path, 'r') as file:
            for line in file:
                if match_pattern_from_line(line, SQUID_PATTERN) != None:
                    ip_list.append(match_pattern_from_line(line, SQUID_PATTERN)["client_ip_address"])

        print(len(ip_list))

        return ip_list

    except FileNotFoundError:

        print(f"Error: File '{path}' not found.")

        return None

def count_lines(path = "/home/dev/Downloads/access.log"):
  """Counts the number of lines in a file using the 'wc' command.

  Args:
      path: path location of log file.

  Returns:
      The number of lines in the file, or None if an error occurs.
  """
  try:
    # Run the command with shell=True (careful with user input should Sanitize with specific functions)
    result = subprocess.run(["wc", "-l", path], capture_output=True)
    
    # Check for errors
    if result.returncode != 0:
      raise OSError(f"Error running wc command: {result.stderr}")
    
    # Decode output (assuming UTF-8 encoding)
    output = result.stdout.decode("utf-8").strip()

    # Extract the number of lines (first element in the output)
    return int(output.split()[0])
  
  except (OSError, ValueError) as e:
    print(f"Error counting lines: {e}")
    return None

def get_first_non_empty_line(path):
  """
  Returns the first non-empty line in a file.

  Args:
      path: path location of log file.

  Returns:
      The first non-empty line from the file, or None if the file is empty or not found.
  """
  try:

    with open(path, 'r') as in_file:
      for line in in_file:
        stripped_line = line.strip()
        if stripped_line:
          return stripped_line
        
  except FileNotFoundError:

    print(f"Error: File '{path}' not found.")

    return None

def get_last_line_subprocess(path):
  """
  Attempts to get the last line of a file using 'tail' command (may not work for all files).

  Args:
      path: path location of log file.

  Returns:
      The last line of the file (if successful), or None on error.
  """
  try:

    # Use 'tail -n 1' to get the last line
    result = subprocess.run(["tail", "-n", "1", path], capture_output=True)
    
    if result.returncode != 0:
      raise OSError(f"Error running tail command: {result.stderr}")

    output = result.stdout.decode("utf-8").strip()

    return output
  
  except (OSError, ValueError) as e:

    print(f"Error getting last line: {e}")

    return None

def get_seconds(path = "/home/dev/Downloads/access.log"):
   """Returns number of secons between first and last event logged.

  Args:
      path: path location of log file.

  Returns:
      The total seconds elapsed in log file, or None on error.
  """
   try:
    
    first_timestamp = float(match_pattern_from_line(get_first_non_empty_line(path), SQUID_PATTERN_EXTENDED)["timestamp"])
    last_timestamp = float(match_pattern_from_line(get_last_line_subprocess(path), SQUID_PATTERN_EXTENDED)["timestamp"])

    return abs(last_timestamp - first_timestamp)

   except (OSError, ValueError) as e:

    print(f"Error getting last line: {e}")

    return None

def get_events_per_second(path="/home/dev/Downloads/access.log"):
    """Returns the number of events per seconds from a log file.

        Args:
            path: path location of log file.

        Returns:
            int EPS (Events Per Second).
    """
    return float(count_lines(path)) / get_seconds(path)