import { useEffect, useState } from 'react'
import {Button} from 'antd'

function Task() {
  const [tasks, setTask] = useState([])
  const [mavzu, setMavzu] = useState("")
  const [nomer, setNomer] = useState()
  const [sana, setSana] = useState()
  const [muddat, setMuddat] = useState()
  const [javobgar, setJavobga] = useState()
  const [topshiriq_turi, setTopshiriq_turi] = useState()
  const [topshiriq_kimdan, setTopshiriq_kimdan] = useState()
  const [status, setStatus] = useState()
  const [natijasi, setNatija] = useState()
  const [editTask, setEditTask] = useState("")
  



  const fetchTasks = async ()=>{
    try {
      const response = await fetch("http://127.0.0.1:8000/api/");
      const data = await response.json()
      
      setTask(data)
      
    }
    catch(err){
      console.log(err)
    }
  }

  useEffect(()=>{
    fetchTasks()
  },[])



  const addTask = async()=>{
   const taskData ={ 
    mavzu: mavzu,
    nomer: nomer,
    sana: sana,
    muddat: muddat,
    javobgar: javobgar,
    topshiriq_turi: topshiriq_turi,
    topshiriq_kimdan: topshiriq_kimdan,
    status: status,
    natijasi: natijasi
  };
  try {
    const response = await fetch("http://127.0.0.1:8000/api/",{
      method: "POST",
      headers: {
        "Content-Type":"application/json",
      },
      body: JSON.stringify(taskData)
      });
      const data = await response.json()
      setTask((prev)=>[...prev, data])

    }
    
  catch(err){
    console.log(err)
  } 
  }
  
  tasks.map((task)=>{
    console.log(task.nomer)
  })
  
  const deleteTask = async (id)=>{
    try {
        const response = await fetch(`http://127.0.0.1:8000/api/${id}`, {
          method: 'DELETE',
        });
        setTask((prev)=> prev.filter((tasks) => tasks.id !== id))
    } catch (err){
      console.log(err)
    }
  }


  return (
    <> 
    
    <h1>Hello world!!! I come back</h1>
    <div>
      <input type='text' placeholder='mavzu' onChange={(e)=>setMavzu(e.target.value)}/>
      <input type="text" placeholder='nomer' onChange={(e)=>setNomer(e.target.value)}/>
      <input type="date" placeholder='sana' onChange={(e)=>setSana(e.target.value)}/>
      <input type="date" placeholder='muddat' onChange={(e)=>setMuddat(e.target.value)}/>
      <input type="text" placeholder='javobgar'onChange={(e)=>setJavobga(e.target.value)}/>
      <input type="text" placeholder='topshiriq_turi'  onChange={(e)=>setTopshiriq_turi(e.target.value)}/>
      <input type="text" placeholder='topshiriq_kimdan' onChange={(e)=>setTopshiriq_kimdan(e.target.value)}/>
      <input type="text" placeholder='status' onChange={(e)=>setStatus(e.target.value)}/>
      <input type="text" placeholder='natijasi' onChange={(e)=>setNatija(e.target.value)}/>
      
      <button onClick={addTask}>Add task</button>
      
          
    </div>
      <h1>List Tasks</h1>
      <table>
            <th>ID</th>
            <th>Mavzu</th>
            <th>Nomer</th>
            <th>Sana</th>
            <th>Muddat</th>
            <th>Javobgar</th>
            <th>Topshiriq turi</th>
            <th>Topshriq kimdan</th>
            <th>Status</th>
            <th>Natijasi</th>
            <th>Edit</th>
            <th>Delete</th>      
      
      {tasks.map(e=>(

        
           <tr>
            <td>{e.id}</td>
            <td>{e.mavzu}</td>
            <td>{e.nomer}</td>
            <td>{e.sana}</td>
            <td>{e.muddat}</td>
            <td>{e.javobgar}</td>
            <td>{e.topshiriq_turi}</td>
            <td>{e.topshiriq_kimdan}</td>
            <td>{e.status}</td>
            <td>{e.natijasi}</td>
            <td><Button type='Danger'>Edit</Button></td> 
            <td><Button type='Ghost' color='red' onClick={()=>deleteTask(e.id)}>Delete</Button></td> 
            </tr>    
         
      ))}
         </table>
    </>
  )
}

export default Task
