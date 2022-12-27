class Burger{
    constructor() {
        this.cost = () => {
            return 200;
        }
    }
}

// decorator 1
class DoublePatty {
    constructor(burger){
        let initialCost = burger.cost()
        burger.cost = () => {
            return initialCost + 100;
        }
    }
}

// decorator 2
class ExtraCheese {
    constructor(burger){
        let initialCost = burger.cost()
        burger.cost = () => {
            return initialCost + 20;
        }
    }
}


const run = () => {
    burger = new Burger();
    console.log(burger.cost())

    new DoublePatty(burger)
    console.log(burger.cost())

    new ExtraCheese(burger)
    console.log(burger.cost())
}