class ArabicLocalizer:
 
    def __init__(self):
 
        self.translations = {
            "car": "car in ar",
            "bike": "bike in ar",
            "cycle":"cycle in ar"
        }
 
    def localize(self, msg):
        return self.translations.get(msg, msg)
 
class BanglaLocalizer:
 
    def __init__(self):
        self.translations = {
            "car": "car in bn",
            "bike": "bake in bn",
            "cycle":"cycle in bn"
        }
 
    def localize(self, msg):
        return self.translations.get(msg, msg)
 
 
def Factory(language):
    localizers = {
        "Arabic": ArabicLocalizer,
        "Bangla": BanglaLocalizer,
    }
 
    return localizers[language]()
 
if __name__ == "__main__":
 
    arabic = Factory("Arabic")
    bangla = Factory("Bangla")
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(bangla.localize(msg))
        print(arabic.localize(msg))