# Simple multi step LLM call using langchain - LLM generate detailed report and given topic, then it send again to LLM to generate summary of that detailed report

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

os.environ['LANGSMITH_AGENT_ID'] = 'observability-2'

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

config={
    'tags': ['llm app', 'report summarization'],
    'metadata': {'model': 'chatgroq: openai/gpt-oss-120b'}
}

result = chain.invoke({'topic': 'Unemployment in India'}, config=config)

print(result)
