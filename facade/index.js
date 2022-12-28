function FileService() {

    this.getFile = () => {
        console.log("Getting file from disk")
    }
}

function Decoder() {

    this.decode_music_data_to_analogue_signal = () => {
        console.log("Decoding encoded music data to analog data")
    }
}

function AudioDriver() {

    this.play_sound = () => {
        console.log("Playing sound from give analogue data")
    }
}

// Facade class
function MusicPlayer() {

    this.fileService = new FileService()
    this.decoder = new Decoder()
    this.audioDriver = new AudioDriver

    this.play_music = () => {
        this.fileService.getFile()
        this.decoder.decode_music_data_to_analogue_signal()
        this.audioDriver.play_sound()
    }
}

const run = () => {
    musicPlayer = new MusicPlayer()
    musicPlayer.play_music()
}

/*
Getting file from disk
index.js:11 Decoding encoded music data to analog data
index.js:18 Playing sound from give analogue data
*/