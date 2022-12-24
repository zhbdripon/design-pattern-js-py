class Dev {
    constructor(){
        this.title = "Software Engineer"
        this.responsibility = "developing features and fix bugs"
    }
}

class QA {
    constructor(){
        this.title = "QA Engineer"
        this.responsibility = "test new features, bug report and regression test"
    }
}

class DevLead {
    constructor(){
        this.title = "Software Dev Lead"
        this.responsibility = "managing dev team"
    }
}

class QALead {
    constructor(){
        this.title = "Software QA Lead"
        this.responsibility = "managing QA team"
    }
}

const Factory = function () {
    this.createEmployee = function (type) {
        let employee;

        switch(type){
            case "dev":
                employee = new Dev();
                break
            case "qa":
                employee = new QA();
                break
            case "dev_lead":
                employee = new DevLead();
                break
            case "qa_lead":
                employee = new QALead();
                break
        }

        employee.greet = function () {
            console.log(`Hi, I am a ${employee.title} and my responsibility is ${employee.responsibility}\n`);
        }

        return employee;
    }
}


function run() {

    let employees = [];
    let factory = new Factory();

    employees.push(factory.createEmployee("qa"));
    employees.push(factory.createEmployee("dev"));
    employees.push(factory.createEmployee("dev_lead"));
    employees.push(factory.createEmployee("qa_lead"));


    for (let employee of employees) {
        employee.greet();
    }
}