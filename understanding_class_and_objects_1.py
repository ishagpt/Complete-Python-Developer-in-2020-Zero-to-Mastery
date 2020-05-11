class BigObject:  # class

    """
    let's think about the efficiency here. You see the blueprint itself - the class is going to be stored in memory.
    So, python interpreter is going to say hey, the BigObject is going to be the blueprint for this. So, I' am going to
    store all that memory, but every time I create an object, I don't have to repeat the code or do anything like that.
    I can simply say go in memory where BigObject is and just run that code . In this way, we have one place that allow
    us to instantiate our code into objects.
    """
    # code
    pass


# we have 3 different objects which are using the BigObject class as Blueprint.
Obj1 = BigObject()  # instantiating the object
Obj2 = BigObject()
Obj3 = BigObject()

