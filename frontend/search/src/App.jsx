import React from 'react'
import { Routes,Route } from 'react-router-dom'
import Search from './Pages/Search/Search'
import Home from './Pages/Home/Home'
import Result from "./Pages/Result/Result"
import MainLayout from './MainLayout'

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home/>}/>
      
      <Route element={<MainLayout/>}>
        <Route path='/search' element={<Search/>}/>
        <Route path='/Result' element={<Result/>}/>
      </Route>
    </Routes>
  )

}
export default App
