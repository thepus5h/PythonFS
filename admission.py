maths=int(input('enter your maths mark: '))
physics=int(input('enter your phy mark: '))
chemistry=int(input('enter your chem mark: '))
print('maths=',maths)
print('physics=',physics)
print('chemistry=',chemistry)
total=maths+physics+chemistry
print('the total= ',total)
mathnphy=maths+physics
print('the maths and physics total= ',mathnphy)
if(maths>=65)and(physics>= 55)and(chemistry>=50):
    if(total>=190)and(mathnphy>=140):
        print('eligible')
else:print('not eligible')        
    