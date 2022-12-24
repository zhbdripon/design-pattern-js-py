class Singleton():
    __shared_obj__ = dict()

    def __init__(self) -> None:
        
        self.__dict__ = self.__shared_obj__
        self.state = "Hello"
        
    def __str__(self) -> str:
        return self.state

if __name__ == "__main__":
    instance1 = Singleton()
    instance2 = Singleton()
    instance3 = Singleton()
 
    print(instance1, instance2, instance3)  # output -> Hello Hello Hello

    instance1.state = "Hi"

    print(instance1, instance2, instance3)  # output -> Hi Hi Hi
    