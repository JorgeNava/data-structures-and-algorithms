def countPalyndromes(sampleArray):
    COUNT = {}
    
    for word in sampleArray:
        REVERSED_WORD = word[::-1]
        if word.lower() == REVERSED_WORD.lower():
            if word not in COUNT:
                COUNT[word] = 1
            else:
                COUNT[word] += 1
    return COUNT
SAMPLE_ARRAY = ['Jorge', 'Ana', 'Ono', 'PPP', 'ASDASD', 'Jorge', 'Ana', 'Ono', 'PPP', 'ASDASD']
RESULT = countPalyndromes(SAMPLE_ARRAY)
print(RESULT)