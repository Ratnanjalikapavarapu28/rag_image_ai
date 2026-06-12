# 🎨 RAG Image AI

An AI-powered Image Generation application that combines Retrieval-Augmented Generation (RAG) with style retrieval to create high-quality images from user prompts.

## 🚀 Features

* Generate images from text prompts
* Retrieval-Augmented Generation (RAG) pipeline
* Style-based image generation
* ChromaDB vector database integration
* Modular Python code structure
* Easy to extend and customize

## 🛠️ Tech Stack

* Python
* ChromaDB
* Generative AI Models
* RAG (Retrieval-Augmented Generation)

## 📂 Project Structure

rag_image_ai/
│
├── app.py
├── requirements.txt
├── image_generation/
├── rag/
├── data/
├── chroma_db/
└── .gitignore

## ⚙️ Installation

### 1. Clone the Repository

git clone https://github.com/Ratnanjalikapavarapu28/rag_image_ai.git

### 2. Navigate to the Project Folder

cd rag_image_ai

### 3. Install Dependencies

pip install -r requirements.txt

## ▶️ Run the Application

python app.py

## 📖 How It Works

1. User enters a text prompt.
2. Relevant style information is retrieved using the RAG pipeline.
3. ChromaDB provides contextual retrieval.
4. The image generation module creates images based on the prompt and retrieved context.
5. Generated images are displayed to the user.

## 🎯 Future Enhancements

* Support for multiple image styles
* Advanced prompt engineering
* Improved retrieval accuracy
* Web deployment
* User authentication