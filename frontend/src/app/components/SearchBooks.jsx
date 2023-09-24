'use client'

import Link from "next/link"
import { useState } from "react"

export default function SearchBooks({ getSearchResults }) {
   const [query, setQuery] = useState('')

   const handleSubmit = async (e) => {
    e.preventDefault()

    const response = await fetch(`/api/books/search?query=${query}`)

    const book = await response.json(query);

    getSearchResults(book)

   }

  return (
    <div className="text-center my-10 px-2">
        <form onSubmit={handleSubmit}>
            <input className="text-black border-2 border-black rounded-full px-12 py-2 " type="text" placeholder="Search by author/book name" value={query} onChange={(e) => setQuery(e.target.value)} />
            <button className="bg-black text-white rounded-full px-3 py-2 hover:bg-black/60" type="submit">Search</button>
        </form>
    </div>
  )
}
