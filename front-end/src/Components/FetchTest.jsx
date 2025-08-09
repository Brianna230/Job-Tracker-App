import React,{useState,useEffect} from "react";

function FetchJobs(){
const[jobs, setJobs] = useState([])
    useEffect(()=>{
        const fetchData = async ()=>{
            const response = await fetch('http://127.0.0.1:5000/api/jobs')
            const jsonData = await response.json();
            setJobs(jsonData)
        };
        fetchData();
    }, []);

   

    return(
        <div>
            <h1>Job List</h1>
            <ul>
                {jobs.map((job,index)=>(
                    <li key={index}>{job.title}<br></br>{job.apply_link}<br></br>{job.company}<br></br>{job.location}</li>
                ))}
            </ul>
        </div>
    )

}

export default FetchJobs;