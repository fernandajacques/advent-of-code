import fs from 'fs/promises';

const text = await fs.readFile('day01-part01data.txt', { encoding: 'utf8' });
const data = text.split("\r\n\r\n")
// console.log(data)

function totalPerElf(elfArray) {
    let calorieCount = 0;
    elfArray.forEach((item) => {
        calorieCount += Number(item)
    })
    return calorieCount
}

const calorieSums = data.map((str) => {
    const perElf = str.split("\r\n")
    return totalPerElf(perElf)
});

calorieSums.sort((a, b) => b - a)
let topThree = calorieSums.slice(0,3);
console.log(topThree.reduce((acc, val) => acc + val, 0));

// console.log(calorieSums);

