// ============== TASK G: ===============

// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.

function maxIndex(arr) {
  let index = 0;
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > arr[index]) {
      index = i;
    }
  }

  return index;
}

console.log(maxIndex([4, 5, 29, 58, 11]));

// TASK F:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi.
// Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

// function findDoublers(b) {
//   for (let i = 0; b.length > i; i++) {
//     for (let c = 1 + i; b.length > c; c++) {
//       if (b[i] === b[c]) {
//         return true;
//       }
//     }
//   }
//   return false;
// }

// console.log(findDoublers("hello")); //true
// console.log(findDoublers("mashaqqat")); // true
// console.log(findDoublers("Ron")); // false

// MITASK-E:

// Shunday function tuzing, u bitta string argumentni qabul
// qilib osha stringni teskari qilib return qilsin.
//  MASALAN: getReverse("hello") return qilsin "olleh"

// function mit(word) {
//   return word.split("").reverse().join("");
// }
// console.log(mit("python"));
