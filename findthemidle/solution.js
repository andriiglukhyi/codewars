var gimme = function (ar) {
    var a = Math.min(ar[0], ar[1], ar[2]);
    var b = Math.max(ar[0], ar[1], ar[2]);
    return ar.indexOf(ar.find((c)=> c !==a && c !== b));
    };
    