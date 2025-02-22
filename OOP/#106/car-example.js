class Car{
    constructor(name , color , model , price) {
        this.name = name
        this.color = color
        this.model = model
        this.price = price
    }
    startEngin() {
        return `${this.name} is start the Engine`
    }
    
    stopEngin() {
        return `${this.name} is stop the Engine`
    }
}

let carOne = new Car("BMW" , "Red" , "M5" , 500000)
let carTwo = new Car("Toyota" , "Red" , "Sonera" , 250000)

console.log(carOne.startEngin())
console.log(carTwo.stopEngin())