const sampleArrayOfObjects = [
  {
    name: "Jorge",
    age: 23
  },
  {
    name: "Rodrigo",
    age: 24
  },
  {
    name: "Brissa",
    age: 19
  },
  {
    name: "Jp",
    age: 22
  },
  {
    name: "Maia",
    age: 1.5
  },
];

let retVal = sampleArrayOfObjects.sort((a, b) => {
  return a.age - b.age;
})
console.log('By age', retVal);

retVal = sampleArrayOfObjects.sort((a, b) => {
  if (a.name > b.name) {
    return 1;
  } else if (a.name == b.name) {
    return 0;
  } else {
    return -1
  }
})
console.log('By name', retVal);
