import React from 'react'
import "./howitworks.css"

const Howitworks = () => {
  return (
    <div className='howitworks'>
      <section class="how-it-works">
            <h2>How It Works</h2>
            <br />
            <p class="subtitle">
             Verify internships, jobs, and scholarships in just a few steps.
            </p>

            <div class="steps-container">

                <div class="step-card">
                    <span class="step-number">1</span>
                    <h3>Paste the Content</h3>
                    <ul>
                        <li>A website link</li>
                        <li>An email message</li>
                        <li>A WhatsApp or Telegram message</li>
                        <li>Any text offering internships, jobs, or scholarships</li>
                    </ul>
                </div>

                <div class="step-card">
                    <span class="step-number">2</span>
                    <h3>Smart Scam Analysis</h3>
                    <ul>
                        <li><strong>Email Domain Check</strong> -Detects free or suspicious domains</li>
                        <li><strong>Urgency Language</strong> -Finds pressure words like “limited slots”</li>
                        <li><strong>Payment Requests</strong> -Flags fees & deposits</li>
                        <li><strong>Company Verification</strong> -Checks fake or missing company data</li>
                        <li><strong>Pattern Matching</strong> -Compares with known scam cases</li>
                    </ul>
                </div>

                <div class="step-card">
                    <span class="step-number">3</span>
                    <h3>Risk Score & Result</h3>
                    <ul>
                        <li>Scam Risk Score (0-100%)</li>
                        <li>Status: <strong>Safe / Suspicious / High Risk</strong></li>
                        <li>Detected red flags explanation</li>
                        <li>Actionable safety tips</li>
                    </ul>
                </div>

                <div class="step-card">
                    <span class="step-number">4</span>
                    <h3>Student Safety Guidance</h3>
                    <ul>
                        <li>What actions to avoid</li>
                        <li>How to verify real companies</li>
                        <li>Where and how to report scams</li>
                    </ul>
                </div>

            </div>
        </section>
    </div>
  )
}

export default Howitworks
