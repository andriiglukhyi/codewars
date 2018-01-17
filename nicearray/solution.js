function isNice(arr){
    let a;
    let counter = 0;
      for (var i=0; i<arr.length; i++){
        if(arr.includes(arr[i]+1) || arr.includes(arr[i]-1)){counter++}
        }
      if ( counter === arr.length && counter !==0){a = true}
      else{a = false}
    return a;
  }