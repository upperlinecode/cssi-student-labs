function checkNumEven(number){
  if(number%2=0){
    return true;
  }
  else{
    return false;
  }
}

function checkStringEqualNum(numberString, numberInt){
  if(numberString === numberInt){
    return true;
  }
  return false;
}

function getFirstElement(array){
  return array(1);
}

//Test Functions

//Expected output: true
console.log(checkStringEqualNum("10",10));

//Expected output: false
console.log(checkNumEven(3));

arr = ["first", "not first"];
//Expected output first
console.log(getFirstElement(arr));
