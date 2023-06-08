function quickSort(array) {
  if (array.length < 2) {
    return array;
  }
  const sortedArrays = divideArray(array);
  const leftSide = sortedArrays?.left;
  const pivot = sortedArrays?.pivot;
  const rightSide = sortedArrays?.right;

  return quickSort(leftSide).concat(quickSort(pivot)).concat(quickSort(rightSide));
};

function divideArray(array) {
  const pivot = array[0];
  const leftSide = [];
  const rightSide = [];

  for (let i = 1; i < array.length; i++) {
    if (array[i] >= pivot) {
      rightSide.push(array[i]);
    } else {
      leftSide.push(array[i]);
    }
  }
  return {
    left: leftSide,
    pivot: [pivot],
    right: rightSide
  };
};

const SAMPLE_ARRAY = [8, 12, 3, 11, 5, 9, 10, 4, 15, 7];
const CORRECT_RESULT = [3, 4, 5, 7, 8, 9, 10, 11, 12, 15];
const RESULT = quickSort(SAMPLE_ARRAY);
console.log('[NAVA] CORRECT_RESULT === RESULT:', JSON.stringify(CORRECT_RESULT) === JSON.stringify(RESULT));
