function isPrime(n) {
    if(n==1) return undefined
    for (let index = 2; index < n; index++) {
        if(n%index==0) return false
    }
    return true
}

console.log(isPrime(5))