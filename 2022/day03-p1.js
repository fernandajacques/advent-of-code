import fs from 'fs/promises';

const text = await fs.readFile('day03data.txt', { encoding: 'utf8' });
const data = text.split("\r\n")

const priorities = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

function getWrongItem(str) {

    let itemPerCompart = (str.length)/2;
    const firstCompart = str.substring(0,itemPerCompart)
    const secondCompart = str.substring(itemPerCompart)

    let wrongItem = Array.from(firstCompart).reduce((acc, value) => {
        if (secondCompart.includes(value)) {
            acc = value
        };
        return acc;
    }, "");

    return wrongItem
}

const wrongItems = [];
data.forEach(inputStr => {
    wrongItems.push(getWrongItem(inputStr))
});

let prioritySum = wrongItems.reduce((acc, val) => {
    return acc + (priorities.indexOf(val) + 1);
}, 0);


console.log(prioritySum)

