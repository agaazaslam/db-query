import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import  create_agent 
from pymongo import MongoClient
from dotenv import load_dotenv
import json
load_dotenv()


ENV = os.getenv("ENVIRONMENT",'development') 

if ENV == "production":
    MONGO_URI= os.getenv("PROD_MONGO_URI")
else:
    MONGO_URI = os.getenv("DEV_MONGO_URI")


client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["credit-users"]

def query_db(query):
    """Query The DataBase by putting in the mongodb aggregration within"""
    result = collection.aggregate([query])
    return result 



system_prompt = """ 
You are an expert MongoDB engineer.

Your task: convert the user's natural-language question into a **valid MongoDB aggregation pipeline** that can be directly used with PyMongo's collection.aggregate().

Rules:
- Output ONLY a valid JSON array of pipeline stages. 
- Do NOT include backticks, code blocks, explanations, or extra text.
- Field names and string values must use double quotes (") to be valid JSON.
- Always wrap the entire pipeline in [ ].
- Use proper MongoDB operators ($match, $group, $project, $count, $sort, $limit).
- If the query asks for a count, average, or sum, include appropriate stages like $group or $count.
- Ensure the output is valid JSON so that it can be passed directly to:
      pipeline = json.loads(llm_output)
      query_result = list(collection.aggregate(pipeline))

Sample data:
{
    "client_num": 719455083,
    "attrition_flag": "Existing Customer",
    "customer_age": 48,
    "gender": "F",
    "dependent_count": 3,
    "education_level": "Uneducated",
    "marital_status": "Single",
    "income_category": "Less than $40K",
    "card_category": "Blue",
    "months_on_book": 39,
    "total_relationship_count": 4,
    "credit_limit": 2991.0,
    "total_revolving_bal": 1508
}

Examples:

User: "find all customers who are Female"
Output:
[
  { "$match": { "gender": "F" } }
]

User: "group customers by income_category and count them"
Output:
[
  { "$group": { "_id": "$income_category", "count": { "$sum": 1 } } },
  { "$sort": { "count": -1 } }
]

Now, generate the MongoDB aggregation pipeline for:
User: {query}

Output ONLY the JSON array of the pipeline, with proper formatting, ready to use in Python's json.loads().
"""


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
agent = create_agent(model=model, system_prompt=system_prompt)





def llm_use(query):
    try:
        result = agent.invoke({"messages": [{"role": "user", "content": query}]})
        llm_output = result["messages"][-1].content

        print(llm_output)
        print("Processing in db ")
        pipeline = json.loads(llm_output)
        query_result = list(collection.aggregate(pipeline))
        print(query_result)
        final_prompt = f"""
You are given the result of a MongoDB query.
The actual query result is:
{query_result}
the user query was {query}
Write a single, clear, and factual sentence summarizing the result — 
as if reporting directly to a non-technical audience. 
Do not mention queries, databases, or technical terms. 
Relate it with the user input query and write a output giving relevant info as if you are bussiness assistant
Simply state the information naturally, for example:
A total of 28 people have names starting with A.
Keep the tone formal and concise.
"""
        final_result = model.invoke(final_prompt)
        return final_result.content

    except Exception as e:
        print(f"had an error {e}")

    finally:
        print("exiting code execution")

