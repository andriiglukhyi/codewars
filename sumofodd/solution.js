function cubeOdd(arr) {
    if (arr.find((x)=> typeof(x) === "string")){ return undefined}
    else { return arr.filter((x)=> x%2===1 || x%2=== -1).map(x=>x*x*x).reduce( (a,x)=>a + x);}
    
    return 0;
    }