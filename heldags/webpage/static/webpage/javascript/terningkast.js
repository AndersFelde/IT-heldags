function throwDice() {
    amountBar = document.getElementById("amount")
    sumBar = document.getElementById("sum")
    throwP = document.getElementById("throw")

    min = Math.ceil(1)
    max = Math.floor(6)
    dice = Math.floor(Math.random() * (max - min + 1) + min)

    increaseWidth(amountBar, 1)
    increaseWidth(sumBar, 0.5 * dice)
    throwP.innerHTML = "Du kastet " + dice

    if (getWidth(sumBar) >= 100 || getWidth(amountBar) >= 100) {
        document.getElementById("throwDice").classList.add("disabled")
        alert("Du får ikke kaste mer :/")
    }
}

function increaseWidth(el, size) {
    width = getWidth(el)
    width += size
    console.log(el.id)
    console.log(width.toString())
    el.style.width = width.toString() + "%"
    console.log(el.style.width)
}

function getWidth(el) {
    console.log(el.style.width)
    return parseInt(el.style.width.slice(0, -1))
    // kutter av % og gjør om til int
}
