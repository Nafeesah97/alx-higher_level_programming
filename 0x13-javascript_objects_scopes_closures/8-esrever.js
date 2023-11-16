#!/usr/bin/node
exports.esrever = function (list) {
    let new_list = [];
    let i = 0;
    let j = list.length - 1
    while (i < list.length) {
        new_list[i] = list[j];
        i++;
        j--;
    }
    return new_list;
}