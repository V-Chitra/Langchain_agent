PROJECT_ID = "chitra-agent-project"  # @param {type:"string"}
LOCATION = "us-central1"  # @param {type:"string"}
STAGING_BUCKET = "gs://grcv-bucket"  # @param {type:"string"}

import vertexai
vertexai.init(project=PROJECT_ID, location=LOCATION, staging_bucket=STAGING_BUCKET)

import getpass
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyAXBWXWBr1qIaYyeQ85qFNahrvLJ1QCKnk"

from langchain_google_vertexai import ChatVertexAI

model = ChatVertexAI(model="gemini-pro")

from typing import List

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
#from flask import Flask, request

# 1. Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
ChatVertexAI(model="gemini-pro")

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

add_routes(
    app,
    chain,
    path="/chain",
)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
#app = Flask(__name__)

#if __name__ == "__main__":
#    app.run(port=8080, host='0.0.0.0', debug=True)
