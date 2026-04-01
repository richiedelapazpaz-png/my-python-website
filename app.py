from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Richie | Lead Generation Specialist</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: #f5f5f5;
            }
            .container {
                max-width: 900px;
                margin: auto;
                padding: 20px;
                background: white;
            }
            h1 {
                color: #333;
            }
            .section {
                margin-top: 30px;
            }
            .highlight {
                color: #ff6600;
                font-weight: bold;
            }
            .btn {
                display: inline-block;
                padding: 10px 15px;
                background: #ff6600;
                color: white;
                text-decoration: none;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Richie</h1>
            <p class="highlight">Lead Generation Specialist (2+ Years Experience)</p>

            <div class="section">
                <h2>About Me</h2>
                <p>
                I am a Lead Generation Specialist with over 2 years of experience
                focusing on B2B lead generation. I help businesses find targeted
                prospects, decision-makers, and verified contact data to support
                their sales growth.
                </p>
            </div>

            <div class="section">
                <h2>What I Do</h2>
                <ul>
                    <li>B2B Lead Generation</li>
                    <li>Email & Contact Research</li>
                    <li>LinkedIn & Google Prospecting</li>
                    <li>Data Scraping & Web Research</li>
                    <li>CRM & Database Building</li>
                </ul>
            </div>

            <div class="section">
                <h2>Tools I Use</h2>
                <ul>
                    <li>Apollo</li>
                    <li>LinkedIn</li>
                    <li>Google Maps</li>
                    <li>Hunter.io</li>
                    <li>Python (Web Scraping)</li>
                </ul>
            </div>

            <div class="section">
                <h2>Contact Me</h2>
                <p>Email: sales2@ohoryelectric.com</p>
                <p>Phone: +63 962 860 7876</p>
            </div>

            <div class="section">
                <h2>Let’s Work Together</h2>
                <p>I help businesses find high-quality leads that convert into real clients.</p>
                <a class="btn" href="mailto:sales2@ohoryelectric.com">Contact Me</a>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)