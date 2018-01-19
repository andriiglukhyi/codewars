function formatWords(words){
    if (!words) return "";
    return words.filter(function(a) { return a !== ''}).join(', ').replace(/(, )+(\S+)$/, ' and $2');