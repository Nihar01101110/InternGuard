import "./search.css"
import React,{ useState } from "react";

const Search = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const handleSearch = async (e) => {
    e.preventDefault();

    if (!text.trim()) {
      setError("Please enter something");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await fetch("https://internguard.onrender.com/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text:text }),
      });

      if(!res.ok){
        throw new Error(`HTTP error! status: ${res.status}`)
      }

      const data = await res.json();

      if(!data || Object.keys(data).length===0){
        throw new Error("API returned empty response");
      }

      setResult(data); 
    } catch (err) {
      setError("Server error. Try again later.");
    }finally{
    setLoading(false);
    }

  };


  return (
    <div className='search'>
      <div className='search-bar'>
        <p className='pone'>Paste your Text or URL here</p>
        
        <form id='form' onSubmit={handleSearch}>
          <textarea 
              className='input'  
              placeholder='paste your text or url here' 
              value={text} 
              onChange={(e)=>setText(e.target.value)}
          />
          <button onClick={handleSearch} className='buttonone' type='submit'>Submit</button>
        </form>
      </div>

      <br />
      
      {error && <p className='error-text' >{error}</p>}

      {loading && <p className='analyze-text'>Analyzing...</p>}
      
      {result && (
        <div className='result-card'>
          <div className='result-top'><h2>Analysis Result</h2></div>
          <p><b>Risk Score: </b> {result.final_risk_score }</p>
          <br />
          <p><b>Risk Level: </b><span className={`risk-level risk-${result.final_risk_level.toLowerCase()}`}> {result.final_risk_level}</span></p>
          <br />
          <p><b>Text Risk Score: </b>{result.text_risk_score}</p>
          <br />
          <p><b>URL Risk Score: </b>{result.url_risk_score}</p>
          <p>{result.explanation}</p>
          <br />

          <div className='result-top'>
          <h4>Signals Detected</h4>
          </div>
          <ul>
            {result.signals_detected && result.signals_detected.length>0 ? ( result.signals_detected.map((s, i) => (
              <li key={i}>{s}</li>  )
              )):(<li>No Specific signals detected</li>)
            }
          </ul>

          <br />
          <h4>Analysis</h4>
          <div className="analysis">
              {result.final_risk_level === "High" ? 
                  "⚠️ High risk detected. This content shows significant red flags." :
              result.final_risk_level === "Medium" ?     
                  "⚠️ Medium risk detected. Exercise caution with this content." :
              result.final_risk_level === "Low" ? 
                  "✅ Low risk detected. This content appears relatively safe." :
                  "Analysis complete."}
          </div>
          <br />

          {/* <h4>Advice</h4>
          <ul>
            {result.advice  &&  result.advice.map((a, i) => (
              <li key={i}>{a}</li>  )
              )
            }
          </ul> */}

           <h4>Recommendations</h4>
                  <div className="recommendations">
                     <ul>
                            {(result.final_risk_level === "High" || result.final_risk_level === "high") && (
                                <>
                                    <li className='risk-highone'>Avoid sharing personal information</li>
                                    <li className='risk-highone'>Do not click on suspicious links</li>
                                    <li className='risk-highone'>Verify the source independently</li>
                                </>
                            )}
                            {(result.final_risk_level === "Medium" || result.final_risk_level === "medium") && (
                                <>
                                    <li className='risk-mediumone'>Be cautious with personal details</li>
                                    <li className='risk-mediumone'>Verify the sender/website</li>
                                    <li className='risk-mediumone'>Look for official contact information</li>
                                </>
                            )}
                            {(result.final_risk_level === "Low" || result.final_risk_level === "low") && (
                                <>
                                    <li className='risk-lowone'>Continue to practice general online safety</li>
                                    <li className='risk-lowone'>Keep software updated</li>
                                    <li className='risk-lowone'>Use strong, unique passwords</li>
                                </>
                            )}
                        {!result.final_risk_level && (
                            <li>Practice general online safety measures</li>
                        )}
                    </ul>
                  </div>
        </div>
      )}

    </div>
  )
}

export default Search