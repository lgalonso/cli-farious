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