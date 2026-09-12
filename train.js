// TASK F:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi.
// Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

function findDoublers(b) {
  for (let i = 0; b.length > i; i++) {
    for (let c = 1 + i; b.length > c; c++) {
      if (b[i] === b[c]) {
        return true;
      }
    }
  }
  return false;
}

console.log(findDoublers("hello")); //true
console.log(findDoublers("mashaqqat")); // true
console.log(findDoublers("Ron")); // false

// MITASK-E:

// Shunday function tuzing, u bitta string argumentni qabul
// qilib osha stringni teskari qilib return qilsin.
//  MASALAN: getReverse("hello") return qilsin "olleh"

// function mit(word) {
//   return word.split("").reverse().join("");
// }
// console.log(mit("python"));
