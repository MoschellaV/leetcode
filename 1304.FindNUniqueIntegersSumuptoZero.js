/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function (n) {
    var solution = [];

    // create an array of a number and the same number but negative
    // this way they cancel out and sum to 0
    for (var i = 1; i <= Math.floor(n / 2); i++) {
        solution.push(i, -i);
    }

    // in case the number is odd we need to add one more number
    // so add 0 b/c it wont change anything
    if (n % 2 !== 0) {
        solution.push(0);
    }

    return solution;
};
