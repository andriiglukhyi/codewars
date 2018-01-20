function minMax(arr){

    return [arr.reduce((a,b)=>Math.min(a,b)),arr.reduce((a,b)=>Math.max(a,b))]; // fix me!
  }