
var val = 0;
var m1 = 1;
var m2 = 1;
var index = 3;

while ((val+"").length < 1000) {
  val = m1 + m2;
  m1 = m2;
  m2 = val;
  index += 1;
  console.log(val);
}

console.log(index);
