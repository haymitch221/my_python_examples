def report(topic = "default"):
    # yield is like return, 
    # but the function becomes a generator, 
    # which means can use built in function 'next' to invoke until there is nothing to return
    yield "waiting " + topic
    yield "recieving " + topic
    for i in range(5): 
        print("info " + str(i))
        yield "see " + str(i)
    yield "done " + topic
    yield {
        'sss': 'this is a json'
    }

r = report()
print(r)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r)) # 没有了

