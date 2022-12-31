function Subscriber(username){
    this.username = username

    this.setNotification = (notification) => {
        console.log(`${username} got notified about: ${notification}`)
    }

}

function Publisher(){
    this.subscribers = []

    this.publish = notification => {
        for(subscriber of this.subscribers){
            subscriber.setNotification(notification)
        }
    }

    this.addSubscriber = newSubscriber => {
        this.subscribers.push(newSubscriber)
    }

    this.removeSubscriber = subscriber => {
        this.subscribers = this.subscribers.filter(item => item!=subscriber)
    }
}

function Netflix() {

    this.publisher = new Publisher()
    this.series = []

    this.addSeries = newSeries => {        
        this.series.push(newSeries)
        this.publisher.publish(newSeries)
    }
}

const run = () => {

    const netflix = new Netflix()
    const subscriber_1 = new Subscriber("redoan")
    const subscriber_2 = new Subscriber("ziaul")
    const subscriber_3 = new Subscriber("monjurul")
    const subscriber_4 = new Subscriber("yakin")
    
    netflix.publisher.addSubscriber(subscriber_1)
    netflix.publisher.addSubscriber(subscriber_3)
    netflix.publisher.addSubscriber(subscriber_4)
    
    netflix.addSeries("Stranger things")
}

    
/*
output:
redoan got notified about: Stranger things
monjurul got notified about: Stranger things
yakin got notified about: Stranger things
*/




