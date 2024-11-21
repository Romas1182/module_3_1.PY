calls = 0
def count_calls():
    global calls
    calls +=1
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [string.lower() for string in list_to_search]

print(string_info('stROchECHka'))
print(string_info('tExT'))
print(is_contains('URban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('human', ['humAN', 'name']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)