package structs

import "fmt"

type Node struct {
    Value int
    Left *Node
    Right *Node
}

type Tree struct {
    Head *Node
}

func (t Tree) Left() *Node {
    return t.Head.Left
}

func (t Tree) Right() *Node {
    return t.Head.Right
}

func (n Node) AssignLeft(l *Node) Node {
    n.Left = l
    return n
}

func (n Node) AssignRight(r *Node) Node {
    n.Right = r
    return n
}

func (n *Node) Print() {
    if n == nil {
        return
    }
    n.Left.Print()
    fmt.Printf("%d ", n.Value)
    n.Right.Print()
}

func (n *Node) DFSPrint() {
    if n == nil {
        return
    }
    n.Left.DFSPrint()
    n.Right.DFSPrint()
    fmt.Printf("%d ", n.Value)
}
