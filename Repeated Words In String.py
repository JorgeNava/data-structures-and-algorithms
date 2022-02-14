text = "Hola. hola hola Hola, hola. holu"
"""
  First approach 
  Time copmplexity of N - Linear
  Here we are using a hash map / dictionary
  to leveling complexity to N^2.
"""

def normalize(word):
  return word.lower().replace(".", "").replace(",", "").replace("!", "")

def countOfNormalizedWordsInText(text):
  words = {}
  for word in text.split(" "):
    word = normalize(word)
    if word in words: 
      words[word] += 1
    else:
      words[word] = 1
  return words
  
def countOfWordsInText(text):
  words = {}
  for word in text.split(" "):
    if "." in word:
      if "." in words: 
        words["."] += 1
      else:
        words["."] = 1
      word = word.replace(".", "")

    if "," in word:
      if "," in words: 
        words[","] += 1
      else:
        words[","] = 1
      word = word.replace(",", "")

    if word in words: 
      words[word] += 1
    else:
      words[word] = 1
  return words

print(countOfWordsInText(text))
print(countOfNormalizedWordsInText(text))