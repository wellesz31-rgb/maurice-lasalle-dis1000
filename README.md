# Maurice LaSalle - DIS 1000 Teaching Assistant

A Streamlit web app that provides 24/7 teaching assistant support for DIS 1000 students at High Point University.

## Setup Instructions

### Step 1: Create a GitHub Repository

1. Go to https://github.com and sign in (or create a free account)
2. Click the "+" button in the top right and select "New repository"
3. Name it: `maurice-lasalle-dis1000`
4. Make it Public
5. Don't add README, .gitignore, or license (we'll upload files directly)
6. Click "Create repository"

### Step 2: Upload Files to GitHub

1. On your new repository page, click "uploading an existing file"
2. Upload these files:
   - `maurice_app.py` (the main app)
   - `requirements.txt` (Python dependencies)
   - `README.md` (this file - optional)

3. Create a folder called `knowledge_base`:
   - Click "Add file" → "Create new file"
   - Type `knowledge_base/placeholder.txt` in the filename field (this creates the folder)
   - Add any text in the file content
   - Commit the file

4. Upload all 7 knowledge base documents to the `knowledge_base` folder:
   - Navigate to the `knowledge_base` folder
   - Click "Add file" → "Upload files"
   - Upload:
     - 01_AI_Ideation_Philosophy_and_Coaching.md
     - 02_Google_Sites_Structure_and_Navigation.md
     - 03_Cakewalk_Basics_and_WAV_Export.md
     - 04_Audio_Embedding_to_Google_Sites.md
     - 05_Common_Problems_and_Solutions.md
     - 06_Teamwork_and_Field_Work.md
     - 07_Connection_to_Your_Major.md
   - Commit the files

### Step 3: Deploy to Streamlit Community Cloud

1. Go to https://share.streamlit.io
2. Sign in with your GitHub account
3. Click "New app"
4. Select:
   - Repository: `your-username/maurice-lasalle-dis1000`
   - Branch: `main`
   - Main file path: `maurice_app.py`
5. Click "Advanced settings"
6. Under "Secrets", add:
   ```
   ANTHROPIC_API_KEY = "your-api-key-here"
   ```
   (Replace with your actual Anthropic API key)
7. Click "Deploy!"

### Step 4: Get Your URL

After deployment (takes 2-3 minutes), you'll get a URL like:
`https://your-username-maurice-lasalle-dis1000.streamlit.app`

Share this URL with your students!

## Usage

Students can:
- Ask questions about Google Sites, Cakewalk, audio embedding, teamwork, and research
- Get step-by-step technical help
- Receive guidance on logistical questions

Maurice will redirect students to you (Mr. Turner) for:
- Creative/conceptual questions
- Grading questions
- Policy exceptions

## Updating the Knowledge Base

If you need to update the knowledge base documents:

1. Go to your GitHub repository
2. Navigate to the `knowledge_base` folder
3. Click on the file you want to edit
4. Click the pencil icon to edit
5. Make your changes
6. Commit the changes
7. Streamlit will automatically redeploy with the updates

## Troubleshooting

**Error: "API key not found"**
- Make sure you added your Anthropic API key in Streamlit secrets

**Error: "Knowledge base documents not found"**
- Verify all 7 markdown files are in the `knowledge_base` folder
- Check that filenames match exactly (including the numbers)

**App is slow or timing out**
- This is normal on the free Streamlit tier
- If it becomes a problem, consider upgrading to Streamlit Pro

## Cost

- Streamlit Community Cloud: Free
- Anthropic API usage: ~$0.01-0.03 per conversation
- Expected total cost for semester: $5-15

## Support

For questions about this setup, contact Mr. Turner at jturner@highpoint.edu
