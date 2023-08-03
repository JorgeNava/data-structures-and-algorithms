def countPalyndromes(sampleArray):
    COUNT = {}
    """ 
        var re = /[\W_]/g; // or var re = /[^A-Za-z0-9]/g;
        const CLEAN_WORD = word.toLowerCase().replace(re, '');
    """
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