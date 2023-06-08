/* 
  # ExerciseImplement a `GET` endpoint `/dealer?cp=72550`
  ## Considerations- You will have the following function available 
  that doesn't require any coding on your end: - The function `getDealersFromDB` can receive as parameter an object defining 
  filters, for example it can take the following parameter: Typescript getDealersFromDB( { cp: '725'} )  - getDealersFromDB 
  response example: JSON { "data":[ { "dealerId": 1, "dealerName": "Autos Nuevos", "dealerBrand": "vw", "address": 
  { "street":"Calle 1", "cp": "72500", "state": "CDMX" } }, { "dealerId": 2, "dealerName": "Autos Semi Nuevos", "dealerBrand": 
  "vw", "address": { "street":"Calle 2", "cp": "72550", "state": "CDMX" } }, { "dealerId": 3, "dealerName": "Autos Semi Nuevos", 
  "dealerBrand": "vw", "address": { "street":"Calle 2", "cp": "72580", "state": "CDMX" } }, { "dealerId": 4, "dealerName": 
  "Autos Semi Nuevos", "dealerBrand": "vw", "address": { "street":"Calle 2", "cp": "72570", "state": "CDMX" } }, { "dealerId": 5, 
  "dealerName": "Autos Semi Nuevos", "dealerBrand": "vw", "address": { "street":"Calle 2", "cp": "72510", "state": "CDMX" } } ], 
  "nextToken":"12dadadopwqjepoqjeqwen" } 
  ### Constraints
  Your endpoint should return all dealers following these rules: 
    - If a dealer's `cp` matches in the first three digits (from left to right) it is considered a close dealer; 
    return at most 5 close dealers following these rules: 
      - Sort all `cp` ASC including the targeted `cp` from the original request, e.g. ["72500","72510","72550","72570","72580"]` 
      - If possible take the first immediate lower `cp` and move it to the answer. Taken the previous array this will be `"72510"` 
      - If possible take the first immediate greater `cp` and move it to the answer. Taken the previous array this will be `"72570"` 
      - Repeat lower-greater until no more `cp` or answer array length is equal to 5- 
  How would you unit test your code?
*/

interface Dealer {
  dealerId: number,
  dealerName: string,
  dealerBrand: string,
  address: {
    street: string,
    cp: string,
    state: string,
  }
};

interface SampleData {
  data: Dealer[],
  nextToken: string
};

interface Filter {
  cp: string;
};

const sampleData: SampleData = { "data":[ { "dealerId": 1, "dealerName": "Autos Nuevos", "dealerBrand": "vw", "address": 
{ "street":"Calle 1", "cp": "72500", "state": "CDMX" } }, { "dealerId": 2, "dealerName": "Autos Semi Nuevos", "dealerBrand": 
"vw", "address": { "street":"Calle 2", "cp": "72550", "state": "CDMX" } }, { "dealerId": 3, "dealerName": "Autos Semi Nuevos", 
"dealerBrand": "vw", "address": { "street":"Calle 2", "cp": "72580", "state": "CDMX" } }, { "dealerId": 4, "dealerName": 
"Autos Semi Nuevos", "dealerBrand": "vw", "address": { "street":"Calle 2", "cp": "72570", "state": "CDMX" } }, { "dealerId": 5, 
"dealerName": "Autos Semi Nuevos", "dealerBrand": "vw", "address": { "street":"Calle 2", "cp": "72510", "state": "CDMX" } } ], 
"nextToken":"12dadadopwqjepoqjeqwen" };

function getDealersFromDB(filters: Filter): Array<string> {
  const DEALERS: Array<Dealer> = sampleData?.data;
  const TARGET_CP: string = filters?.cp;
  const RETURN_VALUE: Array<string> = [];
  let IS_CLOSE_DEALER = false;

  const ALL_CPS = DEALERS.map((DEALER) => {
    return DEALER?.address?.cp;
  });
  const ORDERED_CPS = quickSort(ALL_CPS);
  const INDEX_OF_TARGET_CP = ORDERED_CPS.indexOf(TARGET_CP);

  if (INDEX_OF_TARGET_CP) {
    RETURN_VALUE.push(ORDERED_CPS[INDEX_OF_TARGET_CP]);
    for (let i = 1; i <= ORDERED_CPS.length; i++) {
      if (RETURN_VALUE.length < 5 && INDEX_OF_TARGET_CP - i >= 0) {
        const INMEDIATE_LOWER_CP = ORDERED_CPS[INDEX_OF_TARGET_CP - i];
        IS_CLOSE_DEALER = INMEDIATE_LOWER_CP.substring(0, 3) === TARGET_CP.substring(0, 3);
        if(IS_CLOSE_DEALER) RETURN_VALUE.push(INMEDIATE_LOWER_CP);
      }
      if (RETURN_VALUE.length < 5 && i + INDEX_OF_TARGET_CP <= ORDERED_CPS.length) {
        const INMEDIATE_HIGHER_CP = ORDERED_CPS[INDEX_OF_TARGET_CP + i];
        IS_CLOSE_DEALER = INMEDIATE_HIGHER_CP.substring(0, 3) === TARGET_CP.substring(0, 3);
        if(IS_CLOSE_DEALER) RETURN_VALUE.push(INMEDIATE_HIGHER_CP);
      }
    }
    return quickSort(RETURN_VALUE);
  } else {
    return [];
  }
}

function quickSort(array: Array<any>): Array<any>{
  if (array.length < 2) {
    return array;
  }
  const ARRAYS = divideArray(array);
  const LEFT_SIDE = ARRAYS[0];
  const PIVOT = ARRAYS[1];
  const RIGHT_SIDE = ARRAYS[2];
  return quickSort(LEFT_SIDE).concat(quickSort(PIVOT)).concat(quickSort(RIGHT_SIDE));
}

const divideArray = function (array: any): Array<any> {
  const PIVOT = array[0];
  const RIGHT_SIDE: Array<any> = [];
  const LEFT_SIDE: Array<any> = [];
  for (let i = 1; i < array.length; i++) {
    if (array[i] >= PIVOT) {
      RIGHT_SIDE.push(array[i]);
    } else {
      LEFT_SIDE.push(array[i]);
    }
  }
  return [LEFT_SIDE, [PIVOT], RIGHT_SIDE];
}

const SAMPLE_FILTER: Filter = { cp: '72550' };
const RESULT = getDealersFromDB(SAMPLE_FILTER);
console.log('[NAVA] RESULT:', RESULT);
