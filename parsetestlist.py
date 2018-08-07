import re

# takes in a test list to parse it

def parsetestlist(tests):
    _tests = [[] for j in range(256)]
    for test in tests:
        # Compile Regex
        if not test.get('compiled',False):
            cre = re.compile(test['test'])
            test['test'] = cre.match
            _tests[ord(test['let'])].append ( test )
    return _tests
