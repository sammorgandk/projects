const getUserChoice = userInput => {
 userInput = userInput.toLowerCase();
  if(userInput==='rock'|| userInput==='paper'||userInput==='scissors'|| userInput==='bomb'){
    return userInput
  }
  else{
    console.log('Error. Choose betweeen rock, paper, or scissors')
  }
};

const getComputerChoice = () => {
  let randomNumber=Math.floor(Math.random() * 3)
   switch (randomNumber){
    case 0:
      return 'rock';
    case 1:
      return 'paper'
    case 2:
      return 'scissors'
  }
};
//console.log(getComputerChoice())

function determineWinner(userChoice,computerChoice){
  if (userChoice === computerChoice){
    return ('The game is tied. Try again.')
  }
  if (userChoice === 'bomb'){
    return ('You are the winner!')
  }
  if (userChoice==='paper') {
    if (computerChoice==='scissors') {
      return 'The computer is the winner!';
    } else {
      return 'You are the winner!'
    }
  }
  if (userChoice==='rock') {
    if (computerChoice==='paper') {
       return 'The computer is the winner!'
    } else {
      return 'You are the winner!'
    }
  }
  if(userChoice==='scissors') {
    if (computerChoice==='rock') {
      return 'The computer is the winner!'
    } else {
      return 'You are the winner!'
    }
  }
}

const playGame = () => {
  const userChoice = getUserChoice('paper') //input your choice here;
  const computerChoice = getComputerChoice();
  console.log('You chose: ' + userChoice);
  console.log('The computer chose: ' + computerChoice);
  console.log(determineWinner(userChoice,computerChoice)) 
};

playGame()