import sys

sys.setrecursionlimit(10**9)



def main():

    memo = {}

    primes = [3,5,7,11,13,17]

    initial = [[1,2,3,4,5,6,7,8,9]]

    possible_moves = [(0,1),(1,2),(3,4),(4,5),(6,7),(7,8),(0,3),(3,6),(1,4),(4,7),(2,5),(5,8)]

    key = str(initial[0])

    memo[key] = 0

    while(True):

        curr = initial.pop(0)

        ini_key = str(curr)

        ini = list(curr) 

        for i,j in possible_moves:

            if curr[i] + curr[j] in primes:

                curr[i],curr[j] = curr[j],curr[i]

                key = str(curr)

                if key not in memo:

                    initial.append(curr)

                if key in memo:

                    memo[key] = min(memo[key],memo[ini_key] + 1)

                else:

                    memo[key] = memo[ini_key] + 1

                curr = list(ini)

                

        if len(initial) == 0:

            break





    #print(memo)

    T = int(input())

    for _ in range(T):

        grid = []

        blank = input()

        for i in range(3):

            a,b,c = (map(int,input().split()))

            grid.append(a)

            grid.append(b)

            grid.append(c)

            

        gridkey = str(grid)

        if gridkey not in memo:

            print("-1")

        else:

            print(memo[gridkey])







if __name__ == '__main__':

    main()

