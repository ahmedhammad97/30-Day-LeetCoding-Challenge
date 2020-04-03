/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let previousNums = new Set();
    let currNum = n;

    while(!previousNums.has(currNum)) {
        previousNums.add(currNum);

        let digits = `${currNum}`.split('');
        let sumOfSquares = digits.reduce((sum, curr) => {
            return +(sum + curr**2)
        }, 0);

        currNum = sumOfSquares;

        if (sumOfSquares === 1) return true;
    }

    return false;
};


/*
    As we know from the `Halting Problem`, there is no way to detect an infinite 
    loop without trying, so we must wait until either:
        a) The program terminates, as the number is `Happy`.
        b) The number which is to be checked, did appear before,
        which means, the program is stuck in a loop.

    The beauty of JavaScript being `loosely typed`, allows it to coerce the number to
    a string and split it to digits in a single line, and some idiots still hate JS!
*/