def vAlg(prob, absorbing, f, error, cost = [], discount = 1):
    """
    Calculates the vector v for optimal stopping when an sup-norm error
    of error is reached.

    To specify no cost but a discount, pass in [] for cost.
    """
    maxf = max(f)
    # Set cost to be all 0's if cost not passed to function
    if not cost:
        cost = [0] * len(f)

    # Holds the current iteration of u_n
    current = []
    for x in range(len(f)):
        if absorbing[x]:
            current.append(f[x])
        else:
            current.append(maxf)

    # Loop until desired error achieved
    totalError = 1
    while totalError > error:
        iterError = 0
        prev = current.copy()

        for x in range(len(current)):
            if not absorbing[x]:
                # Calculate Pv(x)
                total = 0
                for z in range(len(current)):
                    total += prob[x][z] * prev[z]

                # The actual algorithm
                current[x] = max(discount * total - cost[x], f[x])

                # Compute sup-norm error
                xError = abs(current[x] - prev[x])
                if iterError < xError:
                    iterError = xError

        totalError = iterError

    return current

############################# Tests Below #############################
def diceTest():
    # Dice test
    prob = [[1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0/6, 1.0 / 6],
            [1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0/6, 1.0 / 6],
            [1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0/6, 1.0 / 6],
            [1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0/6, 1.0 / 6],
            [1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0 / 6, 1.0/6, 1.0 / 6],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]

    f = [1, 2, 3, 4, 5, 0]
    absorbing = [False, False, False, False, False, True]
    print(vAlg(prob, absorbing, f, 1e-6))

def srwTest():
    prob = [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [1.0 / 2, 0.0, 1.0 / 2, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0 / 2, 0.0, 1.0 / 2, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0 / 2, 0.0, 1.0 / 2, 0.0, 0.0],
            [0.0, 0.0, 0.0, 1.0 / 2, 0.0, 1.0 / 2, 0.0],
            [0.0, 0.0, 0.0, 0.0, 1.0 / 2, 0.0, 1.0 / 2],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]
    f = [0, 2, 4, 5, 9, 3, 0]
    absorbing = [True, False, False, False, False, False, True]
    cost = [0.5, 0.5, 0.5, 1, 1, 1, 1]
    discount = 0.9
    print(vAlg(prob, absorbing, f, 1e-6, cost, discount))

def problem4_1():
    prob = [[0.0] * 11 for i in range(11)]
    prob[0][0] = 1.0
    prob[10][10] = 1.0
    absorbing = [True]
        
    for i in range(1, 10):
        prob[i][i - 1] = 1.0 / 2
        prob[i][i + 1] = 1.0 / 2
        absorbing.append(False)

    absorbing.append(True)

    f = [0, 2, 4, 3, 10, 0, 6, 4, 3, 3, 0]
    print(vAlg(prob, absorbing, f, 1e-6))

def problem4_3a():
    prob = [[0.0] * 11 for i in range(11)]
    prob[0][0] = 1.0
    prob[10][10] = 1.0
    absorbing = [True]
    g = [0.75]
        
    for i in range(1, 10):
        prob[i][i - 1] = 1.0 / 2
        prob[i][i + 1] = 1.0 / 2
        absorbing.append(False)
        g.append(0.75)

    absorbing.append(True)
    g.append(0.75)

    f = [0, 2, 4, 3, 10, 0, 6, 4, 3, 3, 0]
    
    print(vAlg(prob, absorbing, f, 1e-6, g))

def problem4_3b():
    prob = [[0.0] * 11 for i in range(11)]
    prob[0][0] = 1.0
    prob[10][10] = 1.0
    absorbing = [True]
        
    for i in range(1, 10):
        prob[i][i - 1] = 1.0 / 2
        prob[i][i + 1] = 1.0 / 2
        absorbing.append(False)

    absorbing.append(True)

    f = [0, 2, 4, 3, 10, 0, 6, 4, 3, 3, 0]
    print(vAlg(prob, absorbing, f, 1e-6, [], 0.8))

def problem4_3c():
    prob = [[0.0] * 11 for i in range(11)]
    prob[0][0] = 1.0
    prob[10][10] = 1.0
    absorbing = [True]
    g = [0.75]
        
    for i in range(1, 10):
        prob[i][i - 1] = 1.0 / 2
        prob[i][i + 1] = 1.0 / 2
        absorbing.append(False)
        g.append(0.75)

    absorbing.append(True)
    g.append(0.75)

    f = [0, 2, 4, 3, 10, 0, 6, 4, 3, 3, 0]
    
    print(vAlg(prob, absorbing, f, 1e-6, g, 0.8))

def problem4_2():
    # Warning everything is zero indexed
    prob = [[0.0] * 11 for i in range(11)]
    for i in range(11):
        for j in range(6):
            prob[i][j] = (j + 1.0) / 36

        for j in range(5):
            prob[i][6 + j] = (5.0 - j) / 36

    absorbing = [False] * 11
    absorbing[5] = True
    f = [2, 3, 4, 5, 6, 0, 8, 9, 10, 11, 12]
    print(vAlg(prob, absorbing, f, 1e-6))
        

