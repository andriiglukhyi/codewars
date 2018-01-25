function high(x){
    var alf1 = "abcdefghijklmnopqrstuvwxyz".split('');
   var arr = x.split(' ').filter(c => c.length>2).reduce(function(a,b){
            var x = a.split('').reduce(function(a,b) {return alf1.indexOf(a) + alf1.indexOf(b)});
            var y = b.split('').reduce(function(a,b) {return alf1.indexOf(a) + alf1.indexOf(b)});

            if  (x>y){
                return a;
            } else { 
                return b;
            }
        });

        return arr;
    }