package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"strings"
	"unicode/utf8"
)

func main() {
	var (
		countLines bool
		countWords bool
		countChars bool
	)

	flag.BoolVar(&countLines, "l", false, "Количество строк")
	flag.BoolVar(&countWords, "w", false, "Количество слов")
	flag.BoolVar(&countChars, "m", false, "Количество символов")
	flag.Parse() 

	if !countLines && !countWords && !countChars {
		countLines = true
		countWords = true
		countChars = true
	}

	fileName := flag.Arg(0)
	var file *os.File
	var err error

	if fileName == "" {
		file = os.Stdin
	} else {
		file, err = os.Open(fileName)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Ошибка при открытии файла: %v\n", err)
			os.Exit(1)
		}
		defer file.Close()
	}

	var lines, words, chars int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		lines++

		words += len(strings.Fields(line))

		chars += utf8.RuneCountInString(line) + 1 // +1 для символа конца строки
	}

	if err := scanner.Err(); err != nil {
		fmt.Fprintf(os.Stderr, "Ошибка при чтении файла: %v\n", err)
		os.Exit(1)
	}

	if countLines {
		fmt.Printf("Количество строк: %d\n", lines)
	}
	if countWords {
		fmt.Printf("Количество слов: %d\n", words)
	}
	if countChars {
		fmt.Printf("Количество символов: %d\n", chars)
	}

	if fileName != "" {
		fmt.Printf("Файл: %s\n", fileName)
	}
	fmt.Println()

}

