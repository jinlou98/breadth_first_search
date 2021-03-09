import sys

############################

# DO NOT CHANGE THIS PART!!

############################

def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [line.split(',') for line in f.read().splitlines()]

    N = int(raw[0][0])
    sin = raw[1]
    s = []
    for st in sin:
        s.append(int(st))
    adj_list = []
    for line in raw[2:]:
        if line == ['-']:
            adj_list.append([])
        else:
            adj_list.append([int(index) for index in line])
    return N, s, adj_list

def writeOutput(output_file, level):
    with open(output_file, 'w') as f:
        for i in level:
            f.write(str(i) + '\n')

 

def Run(input_file, output_file):
    N, s, adj_list = readGraph(input_file)
    level =   BFS(N, s, adj_list)
    writeOutput(output_file, level)


############################

# READ THIS:

############################

def  BFS(N, s, adj_list):
    # We give you three variables:
    # N = the number of vertices in the graphfile
    # s = the start node
    # adj_list = a list of lists:
    # The 0th item is a list of the vertices adjecent to vertex 0.
    # The 1st item is a list of the vertices adjecent to vertex 1.
    # The 2nd item is a list of the vertices adjecent to vertex 2.
    # And so forth.

    # We also give you a variable called level, 
    # which is a list containing N x's as placeholders:
    level = ['x']*N
    # You will write the BFS level of each node here.
    # The 0th item will be the level of vertex 0 in your BFS tree.
    # The 1st item will be the level of vertex 1.
    # Et cetera.

    # PLEASE DO NOT SUBMIT CODE WITH PRINT STATEMENTS.
    # IT WILL MESS UP THE AUTOGRADER.

    ############################

    # WRITE YOUR CODE HERE!!

    ############################
    disc = [False] * N
    queue = []

    for i in s:
        queue.append(i)
        level[i] = 0

    while len(queue) != 0:
        node = queue.pop(0)
        
        for n in adj_list[node]:
            if disc[n] == False:
                queue.append(n)
                if n in s:
                    level[n] = 0
                else:
                    level[n] = str(int(level[node]) + 1)
                disc[n] = True

    return level

############################

# DO NOT CHANGE THIS PART!!

############################



def main(args=[]):
    Run('input', 'output')


if __name__ == "__main__":
    main(sys.argv[1:])    