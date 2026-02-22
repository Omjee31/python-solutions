def median(values):
  values_sorted = sorted(values)   # sort Values
  n = len(values_sorted)   # set n = length of values
  mid = int(n/2)  # find mid index
  if n%2 == 0:  # if length of values is even
    return (values_sorted[mid]+values_sorted[mid+1])/2

  else:  #odd
    return values_sorted[mid]

val = [23,56,78,98,45,63,22,12]
result = median(val)
print(result)
