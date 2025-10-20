import { useState, type ChangeEvent } from "react";
import ChatBubble from "./components/ChatBubble";
import axios from "axios";
import { Database, Ellipsis, FileText, Github, Linkedin, Send } from "lucide-react";
import { startupMessage } from "./components/message";

export interface Message {
  time: string;
  message: string;
  role: string;
}


function App() {

  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState<string>("");
  const [isLoading, setisLoading] = useState<boolean>(false);

  const apiUrl = import.meta.env.VITE_API_URL || "http://localhost:8000";

  const handleSubmit = async () => {
    try {

      setisLoading(true);
      if (!input.trim()) return;
      const userMessage = { "time": "12PM", "message": input, "role": "user" }
      setMessages(prev => [...prev, userMessage]);
      setInput("");

      const response = await axios.post(`${apiUrl}/query`, userMessage);
      console.log(response.data);
      setMessages(prev => [...prev, response.data]);



    } catch (error) {
      console.log(error);

    }
    finally {
      setisLoading(false);
    }
  }

  const handleInput = (e: ChangeEvent<HTMLInputElement>) => {
    setInput(e.target.value);
  }

  return (
    <>
      <div className="min-h-screen flex flex-col">
        <nav className="bg-primary p-2 text-white flex justify-between  ">

          <div className="font-bold flex gap-2 text-white"> <Database /> DB QUERY  </div>
        </nav>

        <div className="flex-col flex-grow  mx-auto  m-3 bg-primary mb-10" >

          <div className="min-w-md md:min-w-6xl container h-[83vh] bg-base-300 overflow-y-auto p-4 ">


            <div className="chat chat-start">
              <div className="chat-header">
                Query Agent
                <time className="text-xs opacity-50">12:45</time>
              </div>
              <div className="chat-bubble chat-bubble-secondary text-secondary-content">
                <p> {startupMessage} </p>
              </div>
            </div>




            {messages.map((msg) => <ChatBubble message={msg} key={msg.message} />)}

            {isLoading && <div className="chat chat-start p-4 text-secondary-content font-semibold "> Thinking  <Ellipsis className=" text-black h-8 w-8 animate-pulse " /> </div>}


          </div>
          <div className="flex justify-center items-center m-2 ">

            <input type="text" value={input} onChange={handleInput} placeholder="Type here" className="input w-full " />
            <button className="btn btn-soft" onClick={handleSubmit}> <Send /> </button>

          </div>
        </div>

        <footer className="bg-secondary p-3 flex justify-center items-center ">

          <div className="flex gap-3">
            <a href="https://github.com/agaazaslam/db-query" target="_blank" rel="noopener noreferrer" >
              <button className="btn btn-circle "> <Github /> </button>
            </a>

            <a href="https://www.linkedin.com/in/agaaz-aslam-00b960198/" target="_blank" rel="noopener noreferrer" >
              <button className="btn btn-circle "> <Linkedin /> </button>
            </a>



            <a href="https://drive.google.com/drive/folders/17Fi__Vn3uejZXN9C8_GX3zUaXXnEOAhv?usp=sharing" target="_blank" rel="noopener noreferrer" >
              <button className="btn btn-circle "> <FileText /> </button>
            </a>
          </div>

        </footer >
      </div >
    </>
  )
}

export default App
