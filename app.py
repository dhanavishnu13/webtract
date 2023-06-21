import gradio as gr
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter

def scrap(urls):
  loaders = UnstructuredURLLoader(urls=[urls])
  data = loaders.load()

  # Text Splitter
  text_splitter = CharacterTextSplitter(separator='\n', 
                                        chunk_size=1000, 
                                        chunk_overlap=200)


  docs = text_splitter.split_documents(data)
  return docs

iface = gr.Interface(fn = scrap, 
                     inputs = "text", 
                     outputs = ['text'],
                     title = 'WebScrap', 
                     description="Get content of the website from given website URL")
                     
iface.launch(inline = False)