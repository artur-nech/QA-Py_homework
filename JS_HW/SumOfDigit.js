/*Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
This is only applicable to the natural numbers.
 */
function digital_root(n) {
    var n;
    toString ( n );
    while (eval(n) >= 10) {
        console.log(n);
        (n = eval(n));
        console.log(n);
    }
    return n;
}
digital_root(16);