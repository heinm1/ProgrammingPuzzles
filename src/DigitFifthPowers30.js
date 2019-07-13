
//identify the sum of all the numbers that can be made by the sum of there digits to the power 5

//===========================
//10000000 was a guess as an upper bound
//much room for refinment


var count = 0;
var sum = 0;

for(var i = 2; i <= 10000000; ++i){
  var temp = i+"";
  var temp2 = 0;
  for(var x = 0; x < temp.length; ++x){
    temp2 += Math.pow(temp[x],5)
  }
  if(temp2 == i){
    count += 1;
    sum += i;
  }
}

console.log(count);
console.log(sum);
