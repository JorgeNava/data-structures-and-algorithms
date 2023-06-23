function getCount(sampleArray, targetWord) {
  let count = 0;

  sampleArray.forEach(word => {
    if (
      targetWord === word ||
      targetWord === word.split("").reverse().join("")
    ) {
      count++;
    }
  });
  return count;
}

const SAMPLE_ARRAY = ['Jorge', 'Ana', 'egroJ', 'anA', 'Carlos'];
//const TARGET_WORD = 'Ana';
const TARGET_WORD = SAMPLE_ARRAY[0];
const RESULT = getCount(SAMPLE_ARRAY, TARGET_WORD);
console.log('[NAVA] RESULT:', RESULT);