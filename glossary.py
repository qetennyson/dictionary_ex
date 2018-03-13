
programming_terms = {
    'variable': "a variable is a value that can change, depending on conditions or on information passed "
                "to the program",
    'data type': "a classification of data which tells the compiler or interpreter "
                 "how you intend to use the data, examples include: boolean, int, and String",
    'string': "a sequence of characters, not to be confused with a primitive data "
              "type like an int.  They are immutable!",
    'mutability': "an object is mutable if it can be changed, and immutable if it cannot be.  For example: a list is "
                  "mutable, but a String is not.",
    'list': "a list of data of any kind, sometimes called an array in other languages.",
    'conditional': "a fundamental method of checking a condition, and changing the behavior of a program accordingly "
                   "the most common example is an if/else statement"
}

for key, value in programming_terms.items():
    print("\nKey: " + key.title())
    print("Value: " + value)

print "\n"

# boss-mode version

for k, v in programming_terms.items():
    print '\n{}: {}'.format(k.title(), v)
