
# Attempt at task 1 #2 . Decided to use python :(
# this is the node class, nodel is the left child, noder is 
#     is the right child. 
class Node:
    def __init__(self, value, nodel, noder):
        self.value = value # the value - either an operator or a number
        self.nodel = nodel
        self.noder = noder

# lets make the tree. first, we will tokenize the string
# before doing that, this also gets rid of all extra 
#   white space. 
def make_tree(eqn):
    eqn = eqn[1:] #removes = sign
    clean_eqn = eqn.replace(" ", "")    # remove whitespace
    arr = []
    word = ""
    # this just separates it into an array of numbers and operators, and brackets 
    for i in range(0,len(clean_eqn)):
      
        if (clean_eqn[i].isdigit() or clean_eqn[i].isalpha()) :
            word+=clean_eqn[i]
        else:
          if(len(word) != 0):
            arr.append(word)
            word = ""
          arr.append(clean_eqn[i])
    arr.append(clean_eqn[len(clean_eqn)-1])      
      
    return make_node(arr)
   

#  lets make the node (the hard part), recursively make the
#     the right subtree and the left subtree. 
def make_node(arr):
    # base case - just the number when one thing left 
    if len(arr) == 1:
        return Node(arr[0], None, None)
    elif (arr[0] == "(" or arr[0] == ")"): #this isn't working :(
       nodel = make_node(arr[1:2]) #skips the bracket, 
       noder = make_node (arr[3:]) # rest of expression
       return Node(arr[2],nodel,noder)
    else:
        nodel = make_node(arr[0:1]) # take the first
        noder = make_node(arr[2:])  # recurse the rest
        return Node(arr[1], nodel, noder)

eqn = "=1+2"
eqn2 = "=A1*A2/2-3"
eqn3 = "=1 + 2/ (1+2)"
# printing the tree with the pretty print format that is asked for
# just adds indentation where necessary recursively
def print_tree(node, indent=1):
    print(node.value)
    if(node.nodel):
        for i in range(indent):
            print(" ", end="")
        print_tree(node.nodel)
    if(node.noder):
        for i in range(indent):
            print(" ", end="")
        print_tree(node.noder, indent=indent+1)


print_tree(make_tree(eqn))
print("----------")
print_tree(make_tree(eqn2))
print("----------")
print_tree(make_tree(eqn3))
