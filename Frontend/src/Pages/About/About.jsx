import React from 'react'
import "./about.css"

const About = () => {
  return (
    <div className='about'>
        <section class="about-section">
            <h1>About Us</h1>
            <br />
            <h2>Protecting Students from Online Opportunity Scams</h2>
            <p>
            Every year, thousands of students lose money, time, and confidence due to
            fake internships, paid certifications, and scholarship frauds.
            Scammers exploit the dreams of freshers by offering:
            </p>
            <br />
            <ul>
                <li>Fake job offers</li>
                <li>“Guaranteed placement” courses</li>
                <li>Scholarship forms with registration fees</li>
                <li>Internship certificates in exchange for money</li>
            </ul>

        <div class="about-highlight">
            <p>
            <strong>Our platform was built with one goal:</strong><br />
            To help students verify opportunities before they fall into a trap.
            </p>
        </div>

        <h2>What Makes Our System Unique?</h2>

        <div class="features">
            <div class="feature-card">
            <h3>🎯 Student-Focused Detection</h3>
            <p>
                Designed specifically for internship, scholarship, and training scams.
            </p>
        </div>

        <div class="feature-card">
            <h3>🛡️ Cybersecurity-Based Analysis</h3>
            <p>
            Uses real scam indicators like domain trust, language patterns, and
            digital footprints.
            </p>
        </div>

        <div class="feature-card">
            <h3>⚡ Instant Results</h3>
            <p>
            No sign-up required. Just paste and analyze.
            </p>
        </div>

    <div class="feature-card">
      <h3>🌍 Social Impact Driven</h3>
      <p>
        We aim to reduce financial loss, mental stress, and career damage caused
        by fraud.
      </p>
    </div>
  </div>
    <br/>
  <h2>Our Vision</h2>
  <p>
    To create a safer digital ecosystem where every student can:
  </p>

  <ul className='thirsul'>
    <li>Apply without fear</li>
    <li>Trust verified opportunities</li>
    <li>Learn how to recognize online scams independently</li>
  </ul>

  <div class="user-types">
    <h2>Who Can Use It?</h2>
    <ul>
      <li>College students</li>
      <li>Fresh graduates</li>
      <li>Internship seekers</li>
      <li>Scholarship applicants</li>
      <li>Parents and educators</li>
    </ul>
  </div>
            </section>
    </div>
  )
}

export default About
