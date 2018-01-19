function formatWords(words){
    let a;
    var arr = [];
    if (words){  
    for (var i=0; i<words.length; i++){
        if (words[i].length>0){
            arr.push(words[i]);
        }
    }
    }
    
    if (arr[0].length === 1){a = arr[0]}
    if (arr.length === 2){a = arr[0]+ ' and ' + arr[1]}
    else { a = arr.join().replace(/,([^,]*)$/, ' and $1').replace(/,/g, ', ')}
    return a
    }