import Image from "next/image";
import Link from "next/link";
import { useRouter } from "next/router";





export default function Books({books}) {

  return (
    <>
    
     <ul className="grid grid-cols-2 mx-auto max-w-[1000px] gap-7 ">
         {books.map(book => (
                <div key={book.slug}
                className="flex flex-col border-2  border-black">
                    
                    <Link href={"/"+ book.slug}>
                      <h1 className="py-2 text-xl">{book.title}</h1>
                        </Link>
                        <Image 
                        src={book.book_imageURL || ""}
                        alt="avatar"
                        height={52}
                        width={52}
                        className="p-10py-2 height={52}
                        width={52}"
                        />  
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
