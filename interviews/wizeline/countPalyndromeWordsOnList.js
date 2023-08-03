function countPalyndromes(sampleArray) {
  const COUNT = {};

  sampleArray.forEach(word => {
    /* 
        var re = /[\W_]/g; // or var re = /[^A-Za-z0-9]/g;
        const CLEAN_WORD = word.toLowerCase().replace(re, '');
    */
    const REVERSED_WORD = word.split("").reverse().join("");

    if (word.toLowerCase() === REVERSED_WORD.toLowerCase()) {
      COUNT[word] = COUNT[word] === undefined ? 1 : COUNT[word]++; 
    }
  });
  return COUNT;
};

const SAMPLE_ARRAY = ['Jorge', 'Ana', 'Peace', 'Ono'];
const RESULT = countPalyndromes(SAMPLE_ARRAY);
console.log('[NAVA] RESULT:', RESULT);