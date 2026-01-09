import React from 'react'
import "./search.css"
import { useState } from "react";

const Search = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    if (!text.trim()) {
      setError("Please enter something");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const res = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text })
      });

      const data = await res.json();
      setResult(data); 
    } catch (err) {
      setError("Server error. Try again later.");
    }

    setLoading(false);
  };


  return (
    <div className='search'>

      <div className='search-bar'>

        <p className='pone'>Paste your Text or URL here</p>
        
        <form className='form' action="">
          <input className='input' type="text" placeholder='paste your text or url here' value={text} onChange={(e)=>setText(e.target.value)}/>
          
          <button onClick={handleSearch} className='buttonone' type='submit'>Submit</button>
        
        </form>
      </div>

      <br />
      
      {error && <p className='error-text' >{error}</p>}
      
      {result && (
        <div className='result-card'>
          <h3>Result</h3>

          <p><b>Risk Score:</b> {result.risk_score}</p>
          <p><b>Risk Level:</b> {result.risk_level}</p>
          <p><b>Explanation:</b> {result.explanation}</p>

          <h4>Signals Detected</h4>
          <ul>
            {result.signals_detected.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          <h4>Advice</h4>
          <ul>
            {result.advice.map((a, i) => (
              <li key={i}>{a}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  )
}

export default Search
