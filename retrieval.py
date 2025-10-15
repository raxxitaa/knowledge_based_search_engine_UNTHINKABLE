from langchain.chains import RetrievalQA
from langchain_openai import OpenAI

def query_documents(vectorstore, query):
    llm = OpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever())
    result = qa_chain.run(query)
    return result
