// countPalyndromeWordsOnList

function countPalyndromes(words) {
  words.forEach(word => {
    var re = /[\W_]/g; // or var re = /[^A-Za-z0-9]/g;
    const CLEAN_WORD = word.toLowerCase().replace(re, '');
    const REVERSED_WORD = CLEAN_WORD.split('').reverse().join('');
    console.log('[NAVA] CLEAN_WORD:', CLEAN_WORD);
    console.log('[NAVA] REVERSED_WORD:', REVERSED_WORD);
    console.log('[NAVA] CLEAN_WORD == REVERSED_WORD:', CLEAN_WORD === REVERSED_WORD);
  });
}

const SAMPLE_ARRAY = ['race car', 'not  a palidrome', 'A man, a plan, a canal. Panama', 'My age is 0, 0 si ega ym.', 'rac ecar',  'never odd or even', 'neve ro ddo reven'];
const RESULT = countPalyndromes(SAMPLE_ARRAY);
console.log('[NAVA] RESULT:', RESULT);