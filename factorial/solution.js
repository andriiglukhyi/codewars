function factorial(n){
    if (n>12 || n<0){
    throw "IllegalArgumentException";
    }
    if (n === 0) {return  1;  
    }else{
    let a =1;
    for (let i=1; i<=n; i++){
     a*=i;
    }
    return  a;
    }
  }