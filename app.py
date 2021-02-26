import uvicorn
import wikipedia as wiki
from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/raiseerror')
def raiseerror():
    raise EOFError

@app.get('/{query}')
def send_summary(query):
    summary = wiki.summary(query, sentences=3)
    return {'query': query, 'summary': summary}
