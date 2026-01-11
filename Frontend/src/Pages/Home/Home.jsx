import React from 'react'
import "./home.css"
import img1 from "../../assets/img1.jpeg"
import img2 from "../../assets/img2.jpeg"
import img3 from "../../assets/img3.jpeg"
import { useNavigate } from 'react-router-dom'


const Home = () => {
  const navigate = useNavigate();
  const handleSignIn=()=>{
    navigate("/search")
  }

  return (
    <div className='home'>

        <div className='block' id="top">
          <h1>AI powered scam detection for students</h1>
          <img className='img1' src={img1} alt="" />
        </div>
      <hr />
        <div  id="paraone">
          <h2>What We do ?</h2>
          <div  className="inone">
            <img className='block' src={img2} alt="" />
            <p className='block'>Fake internships are everywhere.We help you spot 
              them before they trap you.</p>
          </div>
        </div>
        <div  id='paratwo'>
          <p className='block'>Students are constantly targeted with fake 
            internship offers on whatsApp and email-promising 
            high pay,certificates,or "guarenteed placements" 
            in exchange for money.Interguard analyzes these 
            messages and tells you how risky they really are.</p>
            <img className='block' src={img3} alt="" />
        </div>


        <div className='block' id="buttom">
            <h2 id='heading'>Get Started</h2>
            <div id="btn">

                <button onClick={handleSignIn} className='buttonone'>Signup</button>
                <button onClick={handleSignIn} className='buttonone'>Guest</button>
            
            </div>
        </div>

    </div>
  )
}

export default Home
