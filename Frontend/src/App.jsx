import React from 'react'
import { Routes,Route } from 'react-router-dom'
import Search from './Pages/Search/Search'
import Home from './Pages/Home/Home'
import MainLayout from './MainLayout'
import Signup from './Pages/Signup/Signup'
import Howitworks from './Pages/Howitworks/Howitworks'
import About from './Pages/About/About'

const App = () => {
  return (
    <>
    <Routes>
      <Route path="/" element={<Home/>}/>
      
      <Route element={<MainLayout/>}>
        <Route path='/search' element={<Search/>}/>
        <Route path='/Howitworks' element={<Howitworks/>}/>
        <Route path='/Signup' element={<Signup/>}/>
        <Route path='/About' element={<About/>}/>
      </Route>
    </Routes>
    </>
  )
}
export default App
