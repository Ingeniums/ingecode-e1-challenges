package generator

import (
	"fmt"
	"math/rand"
	"os"
	"strings"

	"github.com/Ingeniums/ingecode-e1-challenges/xor-reverse/structs"
)

func strArray(arr []int) []string {
    result := []string{}
    for _, i := range arr {
        result = append(result, fmt.Sprintf("%d", i))
    }
    return result
}

func Output(lines [][]int) {
    out := []string{fmt.Sprintf("%d", len(lines))}
    for _, arr := range lines {
        out = append(out, fmt.Sprintf("%d", len(arr)))
        out = append(out, strings.Join(strArray(arr), " "))
    }
    os.WriteFile(os.Args[1], []byte(strings.Join(out, "\n")), 0644)
}

func GenTree(root **structs.Node, depth int) {
    if depth <= 0 {
        root = nil
        return
    }

    value := rand.Int() % 100000000000000
    *root = &structs.Node{
        Value: value,
    }
    GenTree(&(*root).Left, depth - 1)
    GenTree(&(*root).Right, depth - 1)
}

func DFSXor(head *structs.Node, results *[]int) {
    if head == nil {
        return
    }
    DFSXor(head.Left, results)
    DFSXor(head.Right, results)
    result := (*results)[len(*results) - 1] ^ head.Value
    *results = append(*results, result)
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

func CalcSum(head *structs.Node) int {
    if head == nil {
        return 0
    }
    return calcSumLeft(head) + calcSumRight(head) - head.Value
}
