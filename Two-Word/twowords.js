'use strict';

function nbYear(p0, percent, aug, p) {
  var counter = 0;
  while (p0 < p) {
    p0 += p0 * percent + aug;
    counter ++;
  }
  return counter;
} var a = (1500, 5, 100, 5000);
nbYear(a);


function lil (){
  console.log('hello');
}
lil();