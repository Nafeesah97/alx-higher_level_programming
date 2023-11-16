#!/usr/bin/node
exports.logMe = function (item) {
    let i = 0;

    function print () {
        console.log(i + ':' + item);
        i++;
    }
    return print;
}