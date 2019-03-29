import sys
import phelp
import parray

"""
Expects a list of arguments, without appropraite identifying metadata
Metadata includes:
name: always present, the name of the argument
flag: How it is identified, should only be present for - arguments (-p, -x, --long)
optional: whether the flag is optional (only for flags)
has_value: Whether the flag has a following value (i.e. -p <p name>)
  These can't be chained (like -pvg for -p -v and -g)
type: Optional, The constructor for the type of the object (i.e. int)
  It should be able to parse a string, i'm not responsible for what happens
  if it can't. It defaults to a string

Returns a dictionary mapping names to the values (true for non-valued Named)
"""

def print_help ( desc, arglist, exit_code=1 ):
    clargs = []
    for arg in arglist:
        name = arg.get('flag',arg.get('name',''))
        _desc = arg.get('description','')
        clargs.append((name,_desc))
    phelp.phelp ( desc, clargs )
    sys.exit(exit_code)

def parse_args ( desc, arglist ):
    flags=[]
    single_flags={"h": {"ishelp": True}}
    long_flags={"--help": {"ishelp": True}}
    necessaries=[]
    for arg in arglist:
        if arg.get('flag',"").startswith('-'):
            flags.append(arg)
        else:
            necessaries.append(arg)
        if arg.get("flag","").startswith("-"):
             if arg.get("flag","").startswith("--"):
                 long_flags[arg["flag"]] = arg
             else:
                 single_flags[arg["flag"][1:]] = arg
    ret = {}
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith('-'):
            cs = []
            if ( arg.startswith('--') ):
                cs.append(long_flags.get(arg))
            else:
                for l in arg[1:]:
                    cs.append(single_flags.get(l,{'flag': l}))
            for c in cs:
                if c.get('ishelp'):
                    print_help(desc, arglist,0)
                elif 'name' not in c:
                    print "Unrecognized argument '{}'".format(c['flag'])
                    print_help(desc, arglist)
                else:
                    if c.get('has'):
                        print "Already received argument '{}'".format(c['flag'])
                        print_help(desc, arglist)
                    val = True
                    if c.get('has_value'):
                        if ( len ( sys.argv ) < i+2 ):
                            print "'{}' Should be followed by an argument".format(c['flag'])
                            print_help(desc, arglist)
                        val = sys.argv[i+1]
                        if 'type' in c:
                            try:
                                val = c['type'](val)
                            except:
                                print "'{}' is not of correct type".format(val)
                                print_help(desc, arglist)
                        i += 1
                    ret[c['name']] = val
                    c['has'] = True
        else:
            if ( len ( necessaries ) > 0 ):
                c = necessaries.pop(0)
                val = arg
                if 'type' in c:
                    try:
                        val = c['type'](val)
                    except:
                        print "'{}' is not of correct type".format(val)
                        print_help(desc, arglist)
                ret[c['name']] = val
            else:
                print "Extra argument '{}'".format(arg)
                print_help(desc, arglist)
        i += 1
    names=[]
    for n in necessaries:
        names.append(n['name'])
    for n in flags:
        if not n.get('optional',False) and not 'has' in n:
            names.append("{} ({})".format(n['flag'],n['name']))
    if len ( names ) > 0:
        print "Missing arguments: {}".format(parray.parray(names))
        print_help(desc, arglist)
    return ret

"""
print parse_args ( "I am a test description", [ { 'name': 'present', 'flag': '-p', 'optional': True, 'has_value': True, 'type': int, 'description': 'This specifies to make the file present' },
                     { 'name': 'cool', 'flag': '-x', 'description': 'Determined whether it is cool' },
                     { 'name': 'filename', 'description': 'The file name to use bro' },
                     { 'name': 'use_long', 'flag': '--long', 'optional': True, 'description': 'use long ints' },
                     { 'name': 'doggo', 'description': 'Whether or not doggo' }] )
"""
