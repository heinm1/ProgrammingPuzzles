

function isPrime(n){
  if(n == 0 || n == 1 || n == 2 || n == 3) {
    return true;
  }
  if(n%2 == 0 || n < 0){
    return false;
  }

  for(var i = 3; i <= (n/3); ++i){
    if(n%i == 0){
      return false;
    }
  }
  return true;
}

function sequentialPrimes(a,b) {
  var n = 0;
  var isTrue = true;

  while(isTrue){
    var toTest = (n*n)+(a*n)+b;
    if(!isPrime(toTest)){
      isTrue = false;
    } else {
      n+=1;
    }
  }
  return n;
}

//console.log(sequentialPrimes(1,41));
//console.log(sequentialPrimes(-79,1601));



// n*n + a*n + b
//|a|<1000 and |b|≤1000 and 0≤n
var count = -1;
var best = -1;

for(var a = -999; a < 1000; ++a){
  for(var b = -1000; b <= 1000; ++b){
    var temp = sequentialPrimes(a,b);
    if(temp > count){
      count = temp;
      best = a*b;
    }
  }
}

console.log(best + ": " + count);
