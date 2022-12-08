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
            score = rockScore + drawScore;
        } else if (playerChoice == 'Y') {
            score = paperScore + victoryScore;
        } else {
            score = scissorsScore;
        }

    } else if (opponentChoice == 'B') {
        if (playerChoice == 'X') {
            score = rockScore;
        } else if (playerChoice == 'Y') {
            score = paperScore + drawScore;
        } else {
            score = scissorsScore + victoryScore;
        }

    } else {
        if (playerChoice == 'X') {
            score = rockScore + victoryScore;
        } else if (playerChoice == 'Y') {
            score = paperScore;
        } else {
            score = scissorsScore + drawScore;
        }
    }
    return score
}

const totalScore = data.reduce((acc, round) => acc + scorePerRound(round), 0);
console.log(totalScore);


