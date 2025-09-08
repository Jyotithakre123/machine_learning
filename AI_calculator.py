import streamlit as st
from langchain_google_genai import ChatGoogleGenerative
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import wikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.callbacks import StdOutCallbackHandler

st.set_page_config(page_title="Text to Math Problem Solver")
st.title("Text to Math problem Solver using Gemini")

#Gemini ApI Key
gemini_api_key= st.sidebar.text_input(Label="AIzaSyDAO5wyDE2BOcGRrNdBdI3bYHMPI8tm5jo")
if  not gemini_api_key:
    st.info("Please add your gemini API Key to Continue")
    st.stop()
llm = ChatGoogleGenerative(model = 'gemini-2.5-flash',
                           google_api_key = gemini_api_key)
wikipedia_wrapper = wikipediaAPIWrapper
wikipedia_tool = Tool(
    name = 'Wikipedia',
    func = wikipedia_wrapper,
    description = 'A tool for searching the internet to find information on various object'
)

# Math tool

math_chain = LLMMathChain.from_llm(llm = llm)
calculator = Tool(
    name = 'Calculator',
    func = math_chain.run,
    description = 'A tool for answering math related questions'
)

prompt = """
            you are my personal agent task with
            solving users' mathematical questionss
Questions = st.text_input({questions})
Answer: 
"""

question = st.text_input("Enter your problem here")
prompt_template = PromptTemplate(input_variables=
['questions'],template=prompt)
chain = LLMChain(llm = llm, prompt = prompt_template)

reasoning_tool = Tool(
    name = "Reasoning Tool",
    func = chain.run,
    description = "A tool for answering logic-based and reasoning questions."

)