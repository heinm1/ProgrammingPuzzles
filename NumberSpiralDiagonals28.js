//
//  7 8 9
//  6 1 2
//  5 4 3
//
//What is the sum of the numbers on the diagonals in a
//1001 by 1001 spiral formed in the same way?

// ====================================================

// 1-3  = 2
// 1-5  = 4
// 1-7  = 6
// 1-9  = 8
// 3-13 = 10
// 5-17 = 12
// ...

// solution is this sequence
var start = 1;

//corner values at each stage
var n1 = 1;
var n2 = 1;
var n3 = 1;
var n4 = 1;

var count = 0;

function solution(){

  for(var i = 0; i < 500; ++i){
    count += 2;
    n1 += count;
    start += n1;

    count += 2;
    n2 += count;
    start += n2;

    count += 2;
    n3 += count;
    start += n3;

    count += 2;
    n4 += count;
    start += n4;
  }

}

solution();
console.log(start);
