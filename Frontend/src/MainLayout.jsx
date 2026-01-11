import { Outlet } from 'react-router-dom'
import React from 'react'
import Navbar from "./Components/Navbar/Navbar"

const MainLayout = () => {
  return (
    <>
      <Navbar/>
      <main>
        <Outlet/>
      </main>
    </>
  )
}

export default MainLayout
