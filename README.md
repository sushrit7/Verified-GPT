# Verified GPT  

**Verified GPT** is a collaborative Q&A platform designed to ensure the accuracy and reliability of AI-generated answers. It integrates human expertise and community feedback to refine AI responses and improve large language models (LLMs) over time.  

## Features  
- **AI-Generated Answers**: Users post questions, and the system generates an AI-based answer.  
- **Expert Verification**: Experts and the public can upvote, downvote, and leave comments on AI-generated answers.  
- **Answer Refinement**: AI answers are updated if they receive significant downvotes or after 12 hours, considering all feedback and votes.  
- **Q&A Archive**: Users can explore past questions, answers, and verified comments to gain insights into various edge cases.  
- **LLM Training Data**: The feedback system serves as a data source for refining and training LLMs.  

## Tech Stack  
- **Backend**: Django framework using the MVT (Model-View-Template) architecture.  
- **Frontend**: Integrated with Django templates for seamless user interaction.  
- **API**: Powered by the Gemini API for AI response generation.  
- **Database**: SQLite/PostgreSQL for storing questions, answers, comments, and votes.  

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/verified-gpt.git  
   cd verified-gpt  
    ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/macOS
   env\Scripts\activate     # For Windows
    ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
```
4. Set up the database:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Run the development server:
```bash
python manage.py runserver
```
## Usage  
1. Open the application in your browser at `http://127.0.0.1:8000/`.  
2. Post a question to generate an AI answer.  
3. Review answers, upvote/downvote, and add comments.  
4. Watch answers refine as feedback is considered.  
