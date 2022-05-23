function deafGrandma() {
  //Call helper function
  handleNextQuestion();
}

let bye = false;
let outputMessage = "SPEAK UP, KID!";

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

function handleNextQuestion() {
  readline.question('HEY KID! ', input => {
    if (input === "") {
      outputMessage = "WHAT?!";
    } else if (input.match(/^[GOODBYE]/)) {
      if (bye) { return "LATER, SKATER!"; close();}
      outputMessage = "LEAVING SO SOON?";
      bye = true;
    } else if (input.match(/^[AZ]/)) {
      outputMessage = "NO, NOT SINCE 1946!";
    }
    console.log(outputMessage);
    handleNextQuestion();
  })
}

deafGrandma();