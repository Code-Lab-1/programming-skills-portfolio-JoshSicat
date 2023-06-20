glossary = {
    'string': 'A series of characters.',
    'comment' : 'a note in a program that the python interperter ignores.',
    'list' : 'a collection of item in  a particular order.',
    'loop' : 'work through a collection of time, one at a time.',
    'dictionary' : 'A collection of key-value of pairs.',
    'key' : 'the first item in key-value pair in dictionary.',
    'value' : 'an item associated with a key in a dictionary.',
    'conditional test' : 'a comparison between two value.',
    'float' : 'a numerical calue with a decimal component.',
    'boolean' : 'an experssion that ecaluates  to true or false.',
}


for word, definition in glossary.items() :
    print(f"\n{word.title()}: {definition}") 