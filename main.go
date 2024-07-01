package main

import (
	"fmt"
	// "io"
	"net/http"
	"log"
)

func hello(w http.ResponseWriter, req *http.Request) {
	fmt.Fprintf(w, "hello\n")

}

func main() {
	http.HandleFunc("/hello", hello)
	log.Println("Server started on :8090")
	http.ListenAndServe(":8090", nil)
}
