def countPalyndromeWords(words):
  palyndromes = {}

  for word in words:
    if word in palyndromes:
      palyndromes[word] += 1
    elif word[::-1] in palyndromes:
      palyndromes[word[::-1]] += 1
    else:
      palyndromes[word] = 1
  return palyndromes

words = ['Jorge', 'Ana', 'egroJ', 'anA', 'Carlos', 'anA']
print(countPalyndromeWords(words))
