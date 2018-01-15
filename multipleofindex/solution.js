function multipleOfIndex(array) {
    var a = [];
    for (var i = 0; i<array.length; i++){
    if (array[i]%i===0) {a.push(array[i])}
    }
  return a;
  }