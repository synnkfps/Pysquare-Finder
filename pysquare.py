# Brute Force Accuracy
#     Lower Values = Less Squares to use as reference (better for lower values) (not totally recommended)
#     Higher Values = More Squares to use as reference (better for higher values) (more than 1000 can impact on speed)

bforce = 500

lastDebug = True

def square(n):
    found = False
    foundCallback = 0
    closestCallback = 0
    
    for i in range(1,n+1):
        if i ** 2 == n: 
            found = True
            return f'\nFound! {i}\n'
    else:
        if found == False:
            closestCallbackSquare = 0
            for i in range(1, n+1):
                callback = i ** 2
                if callback == callback:
                    if n - callback < 0:
                        pass
                    #     Here is where the bruteforce magic appears.
                    #     Example: If you put 200 in bforce, it will check square roots under 200 exact squares
                    #     For a total accuracy, you *can* put 2000 on bforce, but it's going to be slower
                    elif n - callback > 0 and n - callback < bforce:
                      
                        for k in range(1,callback+1):
                            if k ** 2 == callback:
                                foundCallback = k
                                closestCallback = foundCallback ** 2
                                
                        print(f'Closest Exact Square = {callback} = {foundCallback}     ({foundCallback} ^ 2 is {foundCallback**2})')

                        for j in range(1, closestCallback + 1):
                            if j ** 2 == closestCallback:
                                closestCallbackSquare = j

            else:
                if closestCallback == 0:
                    print('Wasn\'t possible to reference the closest square for this, try changing the brute-force amount to a higher value. (will take longer)')
                    square(n)
                else:
                    # (n + closestCallback) / (closestCallbackSquare * 2)
                    # ({n} + {closestCallback}) / ({closestCallbackSquare} * 2)
                    if lastDebug == True:
                      return f'Inperfect Square Mathematics Done!\nResult:\n({n} + {closestCallback}) / ({closestCallbackSquare} * 2)\n({n + closestCallback}) / ({closestCallbackSquare * 2})\n\nFOUND: {(n + closestCallback) / (closestCallbackSquare * 2)}  |   {(n + closestCallback) / (closestCallbackSquare * 2)}^2 is {((n + closestCallback) / (closestCallbackSquare * 2))**2}'
                    else:
                      return f'Q: Square of {n} (not exact):\nA: {(n + closestCallback) / (closestCallbackSquare * 2)}'

print(square(15))
# option = int(input('Which number you want to find the square?\n~> '))
# square(option)
