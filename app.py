from flask import Flask

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
            margin-bottom: 10px;
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
            box-shadow: 0 0 10px rgba(0,0,0,0.3);
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
            padding: 20px;
            opacity: 0.8;
        }

        a {
            color: #f97316;
            text-decoration: none;
        }
    </style>
</head>

<body>

<div class="container">

    <div class="hero">
        <h1>Richie</h1>
        <p class="highlight">Lead Generation Specialist | B2B & B2C Expert (2+ Years Experience)</p>
        <p>I help businesses find high-quality leads, decision-makers, and verified contacts to grow sales.</p>
    </div>

    <div class="card">
        <h2>About Me</h2>
        <p>
            Experienced Lead Generation Specialist focused on B2B and B2C outreach.
            Skilled in building targeted prospect lists, email campaigns, LinkedIn outreach,
            and data-driven lead research.
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
                <h3>B2B Lead Generation</h3>
                <p>Targeted business leads and decision-makers.</p>
            </div>
            <div>
                <h3>B2C Lead Generation</h3>
                <p>Consumer targeting and outreach campaigns.</p>
            </div>
            <div>
                <h3>Email Outreach</h3>
                <p>Cold email campaigns and response tracking.</p>
            </div>
            <div>
                <h3>LinkedIn Outreach</h3>
                <p>Direct messaging and connection campaigns.</p>
            </div>
        </div>
    </div>

    <div class="card">
        <h2>Contact</h2>
        <p>Email: <b>richiedelapazpaz@gmail.com</b></p>
        <p>Phone: <b>+63 995 127 9375</b></p>
        <p>Open for freelance & commission-based projects.</p>
    </div>

</div>

<div class="footer">
    © 2026 Richie | Lead Generation Specialist
</div>

</body>
</html>
"""

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)