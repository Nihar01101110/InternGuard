import React, { useState } from 'react'
import "./signup.css"

const Signup = () => {
    const[islogin,setIslogin]=useState(true);

  return (
    <div className='signup'>
        <div className='form-container'>
            <div className='form-toggle'>
                <button className={islogin ? 'active':""} onClick={()=>setIslogin(true)}>Login</button>
                <button className={!islogin ? 'active':""} onClick={()=>setIslogin(false)}>Signup</button>
            </div>
            {islogin?<>
                <div className='form'>
                    <h2>Login Form</h2>
                        <input type="email" placeholder='email'/>
                        <input type="password" placeholder='password'/>
                        <a href='#'>Forgot Password</a>
                        <button>Login</button>
                        <br />
                        <p>Not a member ? <a href='#' onClick={()=>setIslogin(false)}> Signup now</a></p>
                </div>
            </> : <>
                <div className='form'>
                    <h2>Signup Form</h2>
                        <input type="email" placeholder='email'/>
                        <input type="password" placeholder='password'/>
                        <input type="password" placeholder='confirm password'/>
                        <button>signup</button>
                </div>
            </>}
        </div>
    </div>
  )
}

export default Signup
