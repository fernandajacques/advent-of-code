import fs from 'fs/promises';

const text = await fs.readFile('day02data.txt', { encoding: 'utf8' });
const data = text.split("\r\n")

const rockScore = 1; //rock
const paperScore = 2; //paper
const scissorsScore = 3; //scissors
const drawScore = 3;
const victoryScore = 6;

function scorePerRound(str) {
    let opponentChoice = str[0];
    let playerChoice = str[2];
    let score = 0;

    if(opponentChoice == 'A') {
        if (playerChoice == 'X') {
            score = scissorsScore;
        } else if (playerChoice == 'Y') {
            //draw
            score = rockScore + drawScore;
        } else {
            score = paperScore + victoryScore;
        }

    } else if (opponentChoice == 'B') {
        if (playerChoice == 'X') {
            score = rockScore;
        } else if (playerChoice == 'Y') {
            //draw
            score = paperScore + drawScore;
        } else {
            score = scissorsScore + victoryScore;
        }

    } else {
        if (playerChoice == 'X') {
            score = paperScore;
        } else if (playerChoice == 'Y') {
            //draw
            score = scissorsScore + drawScore;
        } else {
            score = rockScore + victoryScore;
        }
    }
    return score
}

const totalScore = data.reduce((acc, round) => acc + scorePerRound(round), 0);
console.log(totalScore);

// console.log(scorePerRound('A X'))
// console.log(scorePerRound('A Y'))
// console.log(scorePerRound('A Z'))
// console.log(scorePerRound('B X'))
// console.log(scorePerRound('B Y'))
// console.log(scorePerRound('B Z'))
// console.log(scorePerRound('C X'))
// console.log(scorePerRound('C Y'))
// console.log(scorePerRound('C Z'))
