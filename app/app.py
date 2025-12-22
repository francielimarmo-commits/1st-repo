from flask import Flask

app = Flask(__name__, static_folder="static")

@app.get("/")
def home():
    return """
    <html>
      <head><title>1st-repo Docker Demo</title></head>
      <body style="font-family: Arial; padding: 24px;">
        <h1>🚀 Meu primeiro projeto com Docker</h1>
        <p>Se você está vendo isso, o site está rodando!</p>

        <img src="/static/pinguim.jpeg" alt="Pinguim" style="max-width: 320px;" />

        <p>Teste rápido: <a href="/health">/health</a></p>
      </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
