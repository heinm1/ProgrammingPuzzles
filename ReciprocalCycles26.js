//A unit fraction contains 1 in the numerator
//
// e.g. 1/2   1/3    1/4
//
//Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.



// numurator dosent matter - repeated number detemined by divisor
//


/*
for(var i = 1; i < 1000; ++i){
  console.log( (1/i).toFixed(60) );
}
*/

//console.log((1/71).toFixed(60));

//long division generator
var a = 1;
var b = 7;
var digits = 8;
for (var i = 0; i < digits; i++) {
  var n = a / b | 0;
  console.log(a + " / "+ b + " = "+ n);
  a = a % b * 10;
}
