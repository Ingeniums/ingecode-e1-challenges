package main

import (
	"fmt"
	"math/rand"
	"os"
	"strings"

	"github.com/Ingeniums/ingecode-e1-challenges/xor-reverse/generator"
	"github.com/Ingeniums/ingecode-e1-challenges/xor-reverse/structs"
)

const NUMLINES = 6000

func strArray(arr []int) []string {
    result := []string{}
    for _, i := range arr {
        result = append(result, fmt.Sprintf("%d", i))
    }
    return result
}

func genData() {
    lines := []string{}
    result := 0
    for i := 0; i < NUMLINES; i++ {
        var t structs.Tree
        generator.GenTree(&t.Head, 4 + rand.Intn(4))
        results := []int{rand.Int()}
        generator.DFSXor(t.Head, &results)
        result += generator.CalcSum(t.Head)
        lines = append(lines, strings.Join(strArray(results), ","))
    }
    os.WriteFile("./generator/data/data.txt", []byte(strings.Join(lines, "\n")), 0644)
    os.WriteFile("./medium - xor reverse.txt", []byte(fmt.Sprintf("%d", result)), 0644)
}

func main() {
    genData()
}
