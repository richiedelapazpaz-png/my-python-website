from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Richie | Lead Generation Specialist</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #0f172a, #1e293b, #111827);
            color: white;
        }

        .container {
            max-width: 1000px;
            margin: auto;
            padding: 40px;
        }

        .hero {
            text-align: center;
            padding: 60px 20px;
        }

        .hero h1 {
            font-size: 40px;
        }

        .highlight {
            color: #f97316;
            font-weight: bold;
        }

        .card {
            background: rgba(255,255,255,0.05);
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 15px;
        }

        .badge {
            display: inline-block;
            background: #f97316;
            padding: 5px 10px;
            border-radius: 20px;
            margin: 5px;
            font-size: 12px;
        }

        .footer {
            text-align: center;
            margin-top: 40px;
            opacity: 0.8;
        }
    </style>
</head>

<body>

<div class="container">

    <div class="hero">
        <h1>Richie</h1>
        <p class="highlight">Lead Generation Specialist | B2B & B2C (2+ Years Experience)</p>
        <p>I help businesses generate high-quality leads and verified contacts.</p>
    </div>

    <div class="card">
        <h2>About Me</h2>
        <p>
            Lead Generation Specialist focused on B2B and B2C outreach, email campaigns,
            LinkedIn prospecting, and data-driven lead research.
        </p>
    </div>

    <div class="card">
        <h2>Tools I Use</h2>
        <div>
            <span class="badge">Sales Navigator</span>
            <span class="badge">Apollo</span>
            <span class="badge">Python</span>
            <span class="badge">Google Maps</span>
            <span class="badge">LinkedIn Research</span>
            <span class="badge">Email Extractor 7</span>
            <span class="badge">Let’s Extract Email Studio</span>
        </div>
    </div>

    <div class="card">
        <h2>Services</h2>
        <div class="grid">
            <div>
                <h3>B2B Leads</h3>
                <p>Decision makers & companies</p>
            </div>
            <div>
                <h3>B2C Leads</h3>
                <p>Targeted consumer outreach</p>
            </div>
            <div>
                <h3>Email Outreach</h3>
                <p>Cold email campaigns</p>
            </div>
            <div>
                <h3>LinkedIn Outreach</h3>
                <p>Direct prospect messaging</p>
            </div>
        </div>
    </div>

    <div class="card">
        <h2>Contact</h2>
        <p>Email: richiedelapazpaz@gmail.com</p>
        <p>Phone: +63 995 127 9375</p>
    </div>

</div>

<div class="footer">
    © 2026 Richie | Lead Generation Specialist
</div>

</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
