- The idea is to first get the values of the tree:
    1. start from the end xor(last element, before last element)
    2. go through the array from last to first xor(i, i - 1)
- From the obtained array, reconstruct the tree:
    1. the first element is the root of the tree
    2. the second is its right node
    3. the third is the right node of the right node of the root
    .
    .
    .
    You must also pay attention to the depth of the tree.
What is left is to is to calculate the sum by simply summing the leftmost nodes `ls`, and the rightmost
nodes `rs`, and the head `h`: ls + rs + h
