// MITASK-E:

// Shunday function tuzing, u bitta string argumentni qabul
// qilib osha stringni teskari qilib return qilsin.
//  MASALAN: getReverse("hello") return qilsin "olleh"

function mit(word) {
  return word.split("").reverse().join("");
}
console.log(mit("python"));
