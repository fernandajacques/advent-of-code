import fs from 'fs/promises';

const text = await fs.readFile('day03data.txt', { encoding: 'utf8' });
const data = text.split("\r\n")

const priorities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

const groupsOfElves = [];

while (data.length > 0) {
    const eachGroup = data.splice(0, 3);
    groupsOfElves.push(eachGroup);
}

function getElfGroup(arr) {

    let repeatedItems = Array.from(arr[0]).reduce((acc, value) => {
        if (arr[1].includes(value) && arr[2].includes(value)) {
            acc.add(value) 
        };
        return acc;
    }, new Set());

    let result = Array.from(repeatedItems)
    return result[0]
}

const elvesBadges = [];
groupsOfElves.forEach(inputArr => {
    elvesBadges.push(getElfGroup(inputArr))
});

let prioritySum = elvesBadges.reduce((acc, val) => {
    return acc + (priorities.indexOf(val) + 1);
}, 0);

console.log(prioritySum)