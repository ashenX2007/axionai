# AXION AI

Railway-ready Flask AI chat app.

## Repository structure
- `app.py` - Flask application entrypoint
- `requirements.txt` - Python dependencies
- `Procfile` - Railway / Heroku startup command
- `runtime.txt` - Python runtime version for deployment
- `templates/index.html` - app HTML template
- `static/logo.png` - app logo asset

## Local setup
1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run locally:
   ```bash
   python app.py
   ```

## Deploy on Railway
1. Create a GitHub repository and push this project.
2. Connect Railway to the GitHub repository.
3. Set environment variables in Railway:
   - `AXION_API_KEY`
   - optionally `GOOGLE_API_KEY`
4. Railway will detect `Procfile` and `requirements.txt` and deploy the app.

## GitHub
1. Initialize the repo:
   ```bash
   git init
   git add .
   git commit -m "Initial Railway-ready Flask app"
   ```
2. Create a GitHub repository and add the remote:
   ```bash
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git branch -M main
   git push -u origin main
   ```

## Notes
- The app uses static assets from `static/` and a template from `templates/`.
- Keep credentials out of source control. Use Railway environment variables instead of hardcoding API keys.
