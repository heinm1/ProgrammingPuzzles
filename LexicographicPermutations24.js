//What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

//Two options:-
//    Brute fource - calculate all
//    Calculate - use maths aka if starting with 0 there are 9 digits left thus 9! permustations
//                this equates to 362880, thus the millionth permutation cant start with 0.
//                It must start with 2 as if it starts woth 1 it can ony represent 9!*2 permutations < million
//                this idea is repeated

//3,628,800 permutations
var list = [0,1,2,3,4,5,6,7,8,9];
var ccc = [];


function perRec(l,per) {
  if(l.length == 0){
    ccc.push(per);
  } else {
    for(var i = 0; i<l.length; ++i){
      var c = l.slice();
      c.splice(i,1);
      var p = per.slice();
      p += l[i]
      perRec(c,p);
    }
  }
}

perRec(list,"");
//ccc.sort();
console.log(ccc[999999]);
