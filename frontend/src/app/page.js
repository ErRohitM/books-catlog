'use client'

import { useState, useEffect } from "react"
import Books from './components/Books'
import SearchBooks from './components/SearchBooks'
import { useRouter } from "next/router";

export default function Home() {
  const [books, setBooks] = useState([]);

    

  useEffect(() => {
    const getBooks = async () => {
      const response = await fetch('/api/books');
      const books = await response.json();
      setBooks(books.results);
    }
    
    getBooks();
  }, []);


  return (
   <div className="text-center">
      <h1 className="font-bold text-6xl mt-12">Books</h1>
      <SearchBooks getSearchResults={(results) => setBooks(results)} />
      <Books books={books} />
   </div>
  )
}