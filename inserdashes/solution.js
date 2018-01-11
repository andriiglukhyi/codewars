
function insertDash(num) {
    var a = num.toString().split('');
    var arr = [];
    for (var i = 0; i<a.length; ++i){
    if (a[i]===0){arr.push(a[i])}
    if (a[i] > 0 && a[i]%2 === a[i+1]%2 ){arr.push(a[i]+'-')}
    else {arr.push(a[i])}
    }
    
    return arr.toString().replace(/,/g , '');
    }
    