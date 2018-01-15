function defineSuit(card) {
    let b = card.split('').reverse();
    
    if (b[0]==='♣') { b = 'clubs'}
    if (b[0]==='♦') {b ='diamonds'}
    if (b[0]==='♥') {b =  'hearts'}
    if (b[0]==='♠') {b = 'spades'}
    return b;
    }