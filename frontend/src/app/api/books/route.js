import { NextResponse } from "next/server";

async function fetchBooks() {
    const response = await fetch('http://localhost:8000/books', {
        "method": "GET",
        
        })
        
        const books = await response.json();
        return books;

}

export async function GET(request) {
    const books = await fetchBooks();
    return NextResponse.json(books);
}