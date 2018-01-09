function abbrevName(name){
    var new1 = name.replace(/[a-z]/g, '');
    console.log(new1);
    return new1.replace(/ /g, '.')
}