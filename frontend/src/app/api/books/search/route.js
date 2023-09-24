import { NextResponse } from "next/server";

async function fetchBooks() {
    const response = await fetch('http://localhost:8000/books', {
        "method": "GET",
        

        })
        
        const book = await response.json();
        return book;

}

export async function GET(request) {
    const books = await fetchBooks();
    const { searchParams } = new URL(request.url);
    const query = searchParams.get('query');

    const filteredBooks = books.results.filter((books) => {
        return books.title.toLowerCase().includes(query.toLowerCase()) || books.author.toLowerCase().includes(query.toLowerCase())
    })

    return NextResponse.json(filteredBooks);
}
