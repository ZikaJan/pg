
#   def my_range():
#        seznam = (list(range(1, 10, 2)))
#        index = 0
#        while index < len(seznam):
#            print(seznam[index])
#            index += 1
#        return seznam

# def my_range(start, stop, step=1):
#    result = []
#    hodnota = start
#    while hodnota < stop:
#        result.append(hodnota)
#        hodnota += step
#    return result

#def for_enumerate():
#    seznam = ["Alice", "Bob", "Eva"]
#    for index, hodnota in enumerate(seznam):
#        index+=1
#       print(f"{index}: {hodnota}")
#    return seznam

def for_enumerate(iterable, start=0):
    result = []

    #index = start
    for prvek in iterable:
        result.append( (start, prvek) )
        start +=1
    return result

def while_enumerate(iterable, start=0):
    result = []
    index = 0
    while index < len(iterable):
        result.append( (index + start, iterable[index] ))
        index +=1
        #start +=1
    return result

if __name__ == "__main__":
    #my_range()

    #print(list(enumerate(['Alice', 'Bob', 'Eva'], 1)))
    #print(for_enumerate(['Alice', 'Bob', 'Eva'], 1))
    print(while_enumerate(['Alice', 'Bob', 'Eva'], 1))