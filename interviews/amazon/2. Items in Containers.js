/* 
2. Items in Containers (example question)

Amazon would like to know how much inventory exists in their closed inventory compartments. Given a string s consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments within the substring between the two indices, inclusive.

An item is represented as an asterisk ("*" = ascii decimal 42)
A compartment is represented as a pair of pipes that may or may not have items between them ("|" = ascii decimal 124).
Example

s = "|**|*|*"
startIndices = [1, 1]
endIndices = [5, 6]

The string has a total of 2 closed compartments, one with 2 items and one with 1 item. For the first pair of indices, (1, 5), the substring is |**|*. There are 2 items in a compartment. For the second pair of indices, (1, 6), the substring is |**|*| and there are 2 + 1 = 3 items in compartments. Both of the answers are returned in an array, [2, 3].

Function Description
Complete the numberOffItems function in the editor below. The function must return an integer array that contains the results for each of the startIndices[i] and endIndices[i] pairs.

numberOffItems has three parameters:

s: A string to evaluate
startIndices: An integer array, the starting indices.
endIndices: An integer array, the ending indices.
Constraints

1 ≤ m, n ≤ 10^5
1 ≤ startIndices[i] ≤ endIndices[i] ≤ n
Each character of s is either "*" or "|"
*/

// FIRST APPROACH (HAS COMPLEXITY TIME ISSUES)
function numberOfItems(s, startIndices, endIndices) {
  const rslt = [];
  for(let i = 0; i < startIndices.length; i++){
      const start = startIndices[i] - 1;        
      const end = endIndices[i] - 1;        
      let open = false;
      let close = false;
      let items = 0;
      let possibleItems = 0;
      
      for(let j = start; j <= end; j++){
          const actChar = s[j];
          if(actChar === '|') {
              if(!open){
                  open = true;
              } else if(open){
                  items += possibleItems;
                  possibleItems = 0;
              }
          }
          if(actChar === '*' && open){
              possibleItems += 1;
          }
      }
      rslt.push(items);
  } 
  return rslt;
}

// IMPROVED APPROACH
function preprocess(s) {
  let itemCount = 0;
  let cumulativeItems = new Array(s.length).fill(0);
  let lastOpenCompartment = new Array(s.length).fill(-1);
  let nextCloseCompartment = new Array(s.length).fill(s.length);

  let lastPipePosition = -1;

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '|') {
      lastPipePosition = i;
      cumulativeItems[i] = itemCount;
    } else if (s[i] === '*') {
      itemCount++;
    }
    cumulativeItems[i] = itemCount;
    lastOpenCompartment[i] = lastPipePosition;
  }

  lastPipePosition = s.length;
  for (let i = s.length - 1; i >= 0; i--) {
    if (s[i] === '|') {
      lastPipePosition = i;
    }
    nextCloseCompartment[i] = lastPipePosition;
  }

  return { cumulativeItems, lastOpenCompartment, nextCloseCompartment };
}

function numberOfItems(s, startIndices, endIndices, cumulativeItems, lastOpenCompartment, nextCloseCompartment) {
  let results = [];

  for (let i = 0; i < startIndices.length; i++) {
    let start = startIndices[i] - 1;
    let end = endIndices[i] - 1;

    let actualStart = nextCloseCompartment[start];
    let actualEnd = lastOpenCompartment[end];

    if (actualStart < actualEnd && actualStart < s.length && actualEnd >= 0) {
      let count = cumulativeItems[actualEnd] - cumulativeItems[actualStart];
      results.push(count);
    } else {
      results.push(0);
    }
  }

  return results;
}

const s = '|**|*|*';
const startIndices = [1, 1];
const endIndices = [5, 6];

const { cumulativeItems, lastOpenCompartment, nextCloseCompartment } = preprocess(s);

const results = numberOfItems(s, startIndices, endIndices, cumulativeItems, lastOpenCompartment, nextCloseCompartment);
console.log(results); // Output should be [2, 3]
