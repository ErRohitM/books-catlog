
import React from "react"
import { useState } from "react"

export default function DetailedBook([slug]) {
    const [[slug], setBooks] = useState('')
 
    useEffect(() => {
        const getBooks = async () => {
          const response = await fetch('/api/books');
          const books = await response.json();
          setBooks(books.results);
        }
        
        getBooks();
        
      }, []);

    return(
        <>
    
        <ul className="grid grid-cols-2 mx-auto max-w-[1000px] gap-7 ">
            {books.map(book => (
                    <div key={book.slug}
                    className="flex flex-col rounded-full border-2  border-black">
                        
                        <Link href={"/"+ book.slug}>
                        <h1 className="py-2 text-xl">{book.title}</h1>
                            </Link>
                        <p className="py-2">Type - {book.slug}</p>
                        <p className="py-2">Type - {book.genere}</p>
                        <p className="py-2">Published On - {book.publication_date}</p>
                        <p className="py-2">By - {book.author}</p>
                        <Link href={"/"+ "details/" + book.slug}>
                        <p className="py-2 bg-black text-white rounded-full">Read more</p>
                        </Link>
                    </div>
                ))}
        </ul>
    </>
    )
       
    }
