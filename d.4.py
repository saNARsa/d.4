data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]
p = 0
def g (*args):
    print(args)
    global p
    for i in args:
        if type(i) == str:
            p += len(i)
        elif type(i) == int:
            p += i
        else:
            for j in i:
                if type(i) == dict:
                    p += i[j]
                    p += len(j)
                elif type(j) == str:
                    p += len(j)
                elif type(j) == int:
                    p += j
                else:
                    g(j)
g(data_structure)
print(p)