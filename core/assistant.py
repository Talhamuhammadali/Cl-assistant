
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import CommaSeparatedListOutputParser
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate


load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')
model = "llama-3.1-70b-versatile"
llm = ChatGroq(model=model,
    api_key=GROQ_API_KEY,
    temperature=0.5
)

def get_command_suggestions(partial_command):
    template="""
You are an AI assistant helping with linux, DevOps and other essential commands for developers. The user has entered the following partial command:

{command}

Please suggest possible completions or variations of this command. Provide up to 5 suggestions. Do not hallucinate. Return the suggestions as a comma-separated list.
    """
    prompt = PromptTemplate.from_template(template)
    
    chain = prompt | llm | CommaSeparatedListOutputParser()
    
    response = chain.invoke(
        {
            "command": partial_command
        }
    )
    return response

if __name__ == "__main__":
    import sys
    partial_command = " ".join(sys.argv[1:])
    suggestions = get_command_suggestions(partial_command)
    print("\n".join(suggestions))