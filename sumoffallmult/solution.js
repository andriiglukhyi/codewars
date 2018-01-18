function findSum(n) {
    let a = []
    for (var i=0; i<=n; i++ ){
    if (i%3===0 || i%5===0){
    a.push(i);
    }
      
    }
    return a.reduce((a,b)=>  a+b);
    }