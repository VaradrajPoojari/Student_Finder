from sentence_transformers import SentenceTransformer
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain_pinecone import Pinecone
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

pinecone_api_key = os.getenv('PINECONE_API_KEY')

#Loading the data
data = pd.read_excel('./Data/university_data.xlsx', sheet_name='Professors')

# Load the pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')


# The name of the Pinecone index
index_name = "studentsdb" 

# Create SentenceTransformer-based embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# Create a Pinecone client using the existing index and SentenceTransformer embeddings
docsearch = Pinecone.from_existing_index(index_name, embeddings)


def get_similar_docs(query, k=3, score=False):
    """
    Args:
        query (str): The input query string for which similar documents are to be retrieved.
        k (int, optional): The number of similar documents to be returned. Defaults to 3.
        score (bool, optional): If True, returns similarity scores along with documents. Defaults to False.

    Returns:
        list or dict: A list of similar documents' IDs (and scores if score=True) based on the query.
    """
    if score:
        # Use Pinecone's similarity_search_with_score to get similar documents and their scores
        similar_docs = index.similarity_search_with_score(query, k=k)
    else:
        # Use Pinecone's MMR search to get similar documents without scores
        similar_docs = docsearch.max_marginal_relevance_search(query, k=k, fetch_k=10)

    return similar_docs

def get_research_interests(guid, df= data):
    """
    Args:
        guid (str): The input query string for which professor data is to be retrived.
        df (dataframe, optional): The professors dataframe

    Returns:
        string: A string for querying the pinecone vectorDB.
    """
    professor = df[df['Professor GUID'] == guid]
    if not professor.empty:
        research_interests = professor['Research Interests'].values[0]
        university_field = professor['University Field'].values[0]
        print(university_field)
        return f"research interests in {research_interests} and is from University Field of {university_field}"
    else:
        return "Professor GUID not found"


def final_function(text,k=3):
    """
    Args:
        query (str): The input query string for which similar documents are to be retrieved.
        k (int, optional): The number of similar documents to be returned. Defaults to 3.
        score (bool, optional): If True, returns similarity scores along with documents. Defaults to False.

    Returns:
        dict: A dict of similar student profiles
    """
    result = get_similar_docs(text,k)
    final_result = {}
    for doc in result:
        key = doc.metadata['source'].split('/')[-1].split('.')[0]
        value = doc.page_content
        final_result[key] = value

    return final_result

