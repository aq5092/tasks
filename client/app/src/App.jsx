import { useState } from 'react'
import './App.css'
import Task from './components/Tasks'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <Task/>   
    </>
  )
}

export default App
