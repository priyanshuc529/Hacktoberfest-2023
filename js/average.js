function average(ar) {
    let sum = 0
    for (let index = 0; index < ar.length; index++) {
        sum +=ar[index]
    }
    return sum/ar.length
}

let ar = [1,2,3,4,5]
console.log(average(ar))