function checkExam(array1, array2) {
    let score = 0;
    for (var i=0; i<array1.length; i++){
    if (array1[i]===array2[i]){score = score  +4 }
    if (array2[i] ===""){score = score + 0}
    if (array2[i]!==array1[i] && array2[i]!==""){score = score - 1 }
    if (score<0){score = 0}
    }
    return score;
   }