
# DB-Query : MongoDB Query Summarizer with Gemini AI

A full-stack application that allows users to query a MongoDB database using **natural language** and receive **concise, human-readable summaries** of the results. The app leverages **FastAPI** for the backend, **React** for the frontend, and **Google Gemini API via LangChain** for natural language processing and query generation.

---

## Features

- Accepts **natural language queries** from the user.  
- Converts user queries into **MongoDB aggregation pipelines** dynamically using Gemini AI.  
- Executes the aggregation on the MongoDB database.  
- Summarizes the query results into **friendly text** using Gemini.  
- Supports filtering, grouping, counting, and more.  
- Full-stack implementation: **React frontend** + **FastAPI backend**.  

---

## Tech Stack

- **Backend:** FastAPI (Python)  
- **Frontend:** React (JavaScript/TypeScript)  
- **Database:** MongoDB  
- **AI/LLM:** Google Gemini API (via LangChain)  

## Info about the Dataset Used 
---

### 🗂️ MongoDB Credit Churn Dataset — Field Reference

| Field | Example Value | Description |
|--------|----------------|-------------|
| **client_num** | `778247358` | Unique customer ID |
| **attrition_flag** | `"Existing Customer"` / `"Attrited Customer"` | Customer status |
| **customer_age** | `65` | Age of the customer |
| **gender** | `"M"` / `"F"` | Gender |
| **dependent_count** | `1` | Number of dependents |
| **education_level** | `"Graduate"` / `"High School"` / `"Doctorate"` | Education qualification |
| **marital_status** | `"Single"` / `"Married"` / `"Divorced"` | Marital status |
| **income_category** | `"Less than $40K"` / `"$40K–$60K"` / `"$80K–$120K"` / `"$120K+"` | Annual income range |
| **card_category** | `"Blue"` / `"Gold"` / `"Platinum"` / `"Silver"` | Type of credit card |
| **months_on_book** | `56` | Months since account opened |
| **total_relationship_count** | `5` | Number of products/accounts with the bank |
| **credit_limit** | `7636` | Credit card limit |
| **total_revo_**


### 🧾 Sample Document

```json
{
  "client_num": 778247358,
  "attrition_flag": "Existing Customer",
  "customer_age": 65,
  "gender": "M",
  "dependent_count": 1,
  "education_level": "Graduate",
  "marital_status": "Single",
  "income_category": "Less than $40K",
  "card_category": "Blue",
  "months_on_book": 56,
  "total_relationship_count": 5,
  "credit_limit": 7636,
  "total_revolving_bal": 0
}
