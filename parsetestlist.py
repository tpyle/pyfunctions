import re

# takes in a test list to parse it

def parsetestlist(tests):
    _tests = [[] for j in range(256)]
    for test in tests:
        # Compile Regex
        cre = re.compile(test['test'])
        ntest = dict()
        ntest['test'] = cre.match
        ntest['function'] = test['function']
        ntest['let'] = test['let']
        _tests[ord(test['let'])].append ( ntest )
    return _tests
