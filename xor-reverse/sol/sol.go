package main

import (
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"

	"github.com/Ingeniums/ingecode-e1-challenges/xor-reverse/structs"
)

func intArray(arr []string) []int {
    result := []int{}
    for _, value := range arr {
        intVal, err := strconv.Atoi(value)
        if err != nil {
            panic(err)
        }
        result = append(result, intVal)
    }
    return result
}

func getTreeValues(values []int) []int {
    nodes := []int{}
    for i := len(values) - 1; i > 0; i-- {
        nodes = append(nodes, values[i] ^ values[i - 1])
    }
    _ = sort.Reverse(sort.IntSlice(nodes))
    return nodes
}

func calculateDepth(numNodes int, currentLevel int) int {
    if numNodes == 0 {
        return 0
    }
    if numNodes == 1 {
        return 1
    }
    return calculateDepth(numNodes - int(math.Pow(2, float64(currentLevel))), currentLevel + 1) + 1
}

var index int = 0
func constructTree(nodes []int, head **structs.Node, depth int) {
    if depth <= 0 {
        *head = nil
        return
    }
    *head = &structs.Node{
        Value: nodes[index],
    }
    index++
    constructTree(nodes, &(*head).Right, depth - 1)
    constructTree(nodes, &(*head).Left, depth -1)
}

func toTree(nodes []int) *structs.Tree {
    t := &structs.Tree{}
    constructTree(nodes, &(*t).Head, calculateDepth(len(nodes), 0))
    return t
}

func calcSumLeft(head *structs.Node) int {
    if head == nil {
        return 0
    }
    return head.Value + calcSumLeft(head.Left)
}

func calcSumRight(head *structs.Node) int {
    if head == nil {
        return 0
    }
    return head.Value + calcSumRight(head.Right)
}

func calcSum(head structs.Tree) int {
    if head.Head == nil {
        return 0
    }
    return calcSumLeft(head.Head) + calcSumRight(head.Head) - head.Head.Value
}

func parse(line string) []int {
    values := strings.Split(line, ",")
    return intArray(values)
}

func flag() int {
    contents, err := os.ReadFile(os.Args[1])
    if err != nil {
        panic(err)
    }
    s := 0
    for _, line := range strings.Split(string(contents), "\n") {
        if line == "" {
            continue
        }
        index = 0
        s += calcSum(*toTree(getTreeValues(parse(line))))
    }
    return s
}

func main() {
    fmt.Println(flag())
}
