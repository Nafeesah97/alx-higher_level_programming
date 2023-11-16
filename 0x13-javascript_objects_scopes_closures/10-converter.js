#!/usr/bin/node
exports.converter = function (base) {
    function converter(num) {
        num.toString(base);
    }
    converter();
}