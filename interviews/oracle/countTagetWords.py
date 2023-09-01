def countTargetWord(words, targetWord):
  count = 0

  for word in words:
    if word == targetWord or targetWord == word[::-1]:
      count += 1
  return count

words = ['Jorge', 'Ana', 'egroJ', 'anA', 'Carlos', 'anA']
targetWord = 'Ana'
print(countTargetWord(words, targetWord))
