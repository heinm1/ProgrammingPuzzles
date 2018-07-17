

function solution1(w){
  var l = [];
  var res = [];
  var count = 0;

  for(var a = 2; a <= w; ++a){
    for(var b = 2; b <= w; ++b){
      l.push(Math.pow(a,b));
    }
  }

  for(var i = 0; i < l.length; ++i){
    res[l[i]] = l[i];
  }

  for(var x = 0; x < res.length; ++x){
    if(res[x] != undefined){
      count += 1;
    }
  }

  console.log(count);
}
/*
for(var a = 2; a <= 32; ++a){
  var t = "";
  for(var b = 2; b <= 32; ++b){
    t += ""+Math.pow(a,b)+",";
  }
  console.log(t);
  console.log("");
}
*/


 solution1(10);

 //solution by hand; dont know how to program solution
