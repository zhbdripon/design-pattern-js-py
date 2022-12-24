const Printer = (()=> {
    let instance;

    const createInstance = () => {
        return {
            get: (prop) => {
                if (instance[prop]) {
                    return instance[prop];
                }
            },
            set: (prop, value) => {
                if (instance) {
                    instance[prop] = value;
                }
            }
        }
    }
    console.log(this)

    return {
        getInstance: () => {
            if (!instance) {
                instance = createInstance();
            }

            return instance
        }
    }
})()

function run() {
    printer1 = Printer.getInstance()
    printer2 = Printer.getInstance()
    console.log(printer1 === printer2)

    printer1.set('print', (text) => {
        console.log(`printing ${text}`)
    })

    printer2.print("Hello World")

}