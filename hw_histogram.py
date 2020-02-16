def letter_count(counts):
  letter_count_num={}
  for word in counts:
    for letter in word:
      keys=letter_count_num.keys()
      if letter in keys:
          letter_count_num[letter]+=1
      else:
          letter_count_num[letter]=1
  return letter_count_num
counts=letter_count('alphabetical')
word = counts
def print_histogram(x):
  from collections import Counter
  counts=Counter(word)
  for i in word:
      print(i,counts[i]*'\u2588')
print_histogram(counts)
