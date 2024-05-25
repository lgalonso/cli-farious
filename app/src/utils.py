import json
from collections import Counter

def least_repeated_item(data):
  """Finds the least repeated item in a list.

  Args:
      data: A list of any data type.

  Returns:
      The item in the list that appears the fewest times, or None if all items
      appear the same number of times.
  """

  if not data:
    return None

  counts = Counter(data)
  min_count = min(counts.values())
  least_repeated = [item for item, count in counts.items() if count == min_count]

  # If multiple items have the same minimum count, return the first one.
  return least_repeated[0]

def most_repeated_item(data):
  """Finds the most repeated item in a list.

  Args:
      data: A list of any data type.

  Returns:
      The item in the list that appears the most times, or None if all items
      appear the same number of times.
  """

  if not data:
    return None
  else:
    return Counter(data).most_common(1)[0][0]

def create_file(filepath):
  """
  This function creates a new file at the specified filepath if it doesn't exist.

  Args:
      filepath (str): The path to the file to be created.
  """
  try:
    with open(filepath, "x") as f:
      pass

    print(f"File '{filepath}' created successfully!")

  except FileExistsError:
    print(f"File '{filepath}' already exists.")

def write_data_to_file(key, data, path="/home/dev/Downloads/output.json"):
  """Writes data in JSON format to a specific file.

  Args:
      key: key to store data in dict.
      data: data to store.
      path: path location of file to write data.

  """
  # Define new data as a Python dictionary
  new_data = {
    key : data
  }

  # Try to open existing file to append data
  try:
    with open(path, "r") as infile:
      existing_data = json.load(infile)
    existing_data[key] = data

    with open("/home/dev/Downloads/output.json", "w") as outfile:
      json_string = json.dumps(existing_data, indent=4)
      outfile.write(json_string)

  except FileNotFoundError:
    create_file(path)
    # Open a file for writing in text mode
    with open(path, "w") as outfile:
      # Convert dictionary to JSON string (optional for human-readable output)
      json_string = json.dumps(new_data, indent=4)  # indent for readability (optional)
    
      # Write JSON string to the file
      outfile.write(json_string)

  print(f"Data written to {path}!")