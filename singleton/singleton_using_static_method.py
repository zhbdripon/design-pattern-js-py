
class Singleton:
 
    __shared_obj__ = 'Hi'
 
    @staticmethod
    def getInstance():
        if Singleton.__shared_obj__ == 'Hi':
            Singleton()
        return Singleton.__shared_obj__
 
    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_obj__ != 'Hi':
            raise Exception("This is a singleton class and cannot instantiate more than once")
        else:
            Singleton.__shared_obj__ = self
 
 
# main method
if __name__ == "__main__":
 
    obj_0 = Singleton()
    obj_1 = Singleton.getInstance()
    obj_2 = Singleton.getInstance()

    assert(obj_0 == obj_1 and obj_1 == obj_2)
    print(obj_0, obj_1, obj_2) # should print the same reference

    # will throw an error here
    # obj_3 = Singleton() 