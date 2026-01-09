import React from 'react'
import "./navbar.css"
import { Link,NavLink } from 'react-router-dom'

const Navbar = () => {
  return (
    <div className='navbar'>

      <div className='right'>

            <ul>
                <li><button className='buttontwo'><NavLink to="/" style={({isActive})=>({
                  color:isActive?"black":"",
                  color:isActive?"white":"",
                  textDecoration:"none",
                
                })}>Home</NavLink></button></li>
                <li><button className='buttontwo'><NavLink to="/Result" style={({isActive})=>({
                  color:isActive?"black":"",
                  color:isActive?"white":"",
                  textDecoration:"none",
                 })}> How it works</NavLink> </button></li>

                <li><button className='buttontwo'><NavLink to="/Result" style={({isActive})=>({
                  color:isActive?"black":"",
                  textDecoration:"none",
                  color:isActive?"white":"",
                 })}>About</NavLink></button></li>

            </ul>

            <div className="nav-right">
                <button className='buttonone'><NavLink to="/" style={({isActive})=>({
                  textDecoration:"none",
                })}>Sign up</NavLink></button>
            </div>

        </div>
    </div>
  )
}

export default Navbar
