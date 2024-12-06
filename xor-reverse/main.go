package main

import (
	"fmt"
	"math/rand"
	"os"

	"github.com/Ingeniums/ingecode-e1-challenges/xor-reverse/generator"
	"github.com/Ingeniums/ingecode-e1-challenges/xor-reverse/structs"
)

const NUMLINES = 6000

func genData() {
    lines := [][]int{}
    result := 0
    for i := 0; i < NUMLINES; i++ {
        var t structs.Tree
        generator.GenTree(&t.Head, 4 + rand.Intn(4))
        results := []int{rand.Int()}
        generator.DFSXor(t.Head, &results)
        result += generator.CalcSum(t.Head)
        lines = append(lines, results)
    }
    generator.Output(lines)
    os.WriteFile("./medium - xor reverse.txt", []byte(fmt.Sprintf("%d", result)), 0644)
}

func main() {
    genData()
}
