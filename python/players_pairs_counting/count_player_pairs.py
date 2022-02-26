def possible_player_pairs(array) :
  lenArr = len(array)
  if (lenArr <= 0):
    return []

  if (lenArr == 1):
    return array

  results = []
  for i in range(0, lenArr - 1):
      for j in range(i + 1, lenArr):
        results.append(array[i] + array[j])

  return results

def count_player_pairs(n) :
  if (n <= 0):
    return 0

  if (n == 1):
    return 1

  count = 0
  for i in range(0, n - 1):
      for j in range(i + 1, n):
        count = count + 1

  return count
