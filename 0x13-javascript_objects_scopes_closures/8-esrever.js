#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let i = 0;
  let j = list.length - 1;
  while (i < list.length) {
    newList[i] = list[j];
    i++;
    j--;
  }
  return newList;
};
