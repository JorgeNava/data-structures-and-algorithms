/*
Design a program that could accept words and determine if the
current word is a permutation of a previously submitted word.

A permutation is any arrangement of the same letters in a different
order.

E.g.
User: GOD
Response: GOD: No permutations found
User: DOG
Response: DOG: GOD
User: HELP
Response: HELP: No permutations found
User: PHEL
Response: PHEL: HELP
User: GOO
Response: GOO: No permutations found
User: GDO
Response: GDO: GOD, DOG
*/

function permutations(input) {
  const SORTED_INPUT = input.sort();

  if(permutatedInputs.hasProperty(SORTED_INPUT)){
    permutatedInputs.SORTED_INPUT.push(input);
    return permutatedInputs.SORTED_INPUT;
  } else {
    permutatedInputs[SORTED_INPUT] = [input];
    return "No permutations found";
  }  
}

permutations('GOD');
permutations('DOG');
permutations('HELP');
permutations('PHEL');
permutations('GOO');
permutations('GDO');