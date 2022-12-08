import fs from 'fs/promises';

const text = await fs.readFile('day01-part01data.txt', { encoding: 'utf8' });
const data = text.split("\r\n\r\n")

let highestCal = 0;

function totalPerElf(elfArray) {
    let calorieCount = 0;
    elfArray.forEach((item) => {
        calorieCount += Number(item)
    })
    return calorieCount
}

data.forEach((str) => {
    const perElf = str.split("\r\n")
    let sumPerElf = totalPerElf(perElf)

    if (sumPerElf > highestCal) {
        highestCal = sumPerElf
    }
});

console.log(highestCal);

