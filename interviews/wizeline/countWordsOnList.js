function countWords(sampleArray) {
  const COUNT = {};

  sampleArray.forEach(word => {
    const REVERSED_WORD = word.split("").reverse().join("");
    if (COUNT[REVERSED_WORD] !== undefined) {
      COUNT[REVERSED_WORD] += 1;
      if (COUNT[word] === undefined) {
        COUNT[word] = COUNT[REVERSED_WORD];
      }
    }

    if(COUNT[word] === undefined) COUNT[word] = 1;
  });
  return COUNT;
}

const SAMPLE_ARRAY = ['Jorge', 'Ana', 'egroJ', 'anA', 'Carlos'];
const RESULT = countWords(SAMPLE_ARRAY);
console.log('[NAVA] RESULT:', RESULT);