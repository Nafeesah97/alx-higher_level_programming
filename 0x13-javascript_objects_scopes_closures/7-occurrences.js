#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let j = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      j++;
    }
    i++;
  }
  return j;
};
