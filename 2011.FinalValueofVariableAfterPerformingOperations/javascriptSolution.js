/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function (operations) {
  let x = 0;

  operations.forEach((op) => {
    if (op.includes("+")) x++;
    else x--;
  });

  return x;
};
