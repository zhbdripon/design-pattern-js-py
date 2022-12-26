
// old interface 
class SlackMessage {
    constructor(public_key) {
        this.key = public_key
        this.send_message = message => {
            console.log("message_sent")
        }
    }
}

// new interface
class SlackSecureMessage {
    constructor() {
        this.request_otp = () => {
            console.log("OTP requested")
        }

        this.verify_otp = code => {
            console.log('verifying otp')
            return { session: "session_data"}
        }

        this.verify_session = (public_key) => {
            console.log("verifying session")
            return true;
        }

        this.send_message = (message, session) => {
            if (this.verify_session(session)) {
                console.log("message_sent")
            }
        }
    }
}

class SlackMessageAdapter {

    constructor(slack_message) {
        this.slack_secure_message = new SlackSecureMessage()
        this.slack_message = slack_message

        this.get_session_using_public_key = public_key => {
            console.log('getting session using public key...')

            return { session: "session_data"}
        }

        this.send_message = message => {
            const session = this.get_session_using_public_key(this.slack_message.key)
            this.slack_secure_message.send_message(message, session)
        }
    }


}

const run = () => {

    // using the new interface
    slack_secure_message = new SlackSecureMessage()
    slack_secure_message.request_otp()
    session = slack_secure_message.verify_otp("123456")
    slack_secure_message.send_message("Hi", session)

    // using the old interface
    slack_message = new SlackMessage("public_key")
    slack_message.send_message("Hi")

    // using the old interface with adapter
    slack_message_adapter = new SlackMessageAdapter(slack_message)
    slack_message_adapter.send_message("Hi")


}