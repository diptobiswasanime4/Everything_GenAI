import {useEffect} from 'react'
import Quill from "quill"
import "quill/dist/quill.snow.css"

function TextEditor() {
    useEffect(() => {
        new Quill("#container", {theme: "snow"})
    }, [])
  return (
    <div id='container'>TextEditor</div>
  )
}

export default TextEditor