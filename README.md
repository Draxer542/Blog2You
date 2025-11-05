# Blog2You

A modern, full-featured blog application built with Flask that allows users to read and comment on blog posts, with admin capabilities for content management.

## 📖 About

Blog2You is a blogging platform designed to create a vibrant community where ideas are shared, thoughts are exchanged, and voices are heard. The platform features a clean, responsive design and provides an interactive space for readers to engage with content through comments and discussions.

## ✨ Features

### User Features
- **User Registration & Authentication**: Secure user registration and login system with password hashing
- **Blog Post Viewing**: Browse all blog posts on the homepage
- **Individual Post Viewing**: Read full blog posts with rich text formatting
- **Comment System**: Authenticated users can leave comments on blog posts
  - Gravatar integration for user profile images
  - Rich text editor for comments
- **Contact Form**: Send messages to the blog administrator via email
- **About Page**: Learn more about the platform

### Admin Features
- **Create Posts**: Admin-only access to create new blog posts
- **Edit Posts**: Modify existing blog posts
- **Delete Posts**: Remove blog posts from the platform
- **Rich Text Editor**: CKEditor integration for creating and editing blog content

## 🛠️ Technology Stack

- **Backend Framework**: Flask 2.3.2
- **Database**: SQLAlchemy 2.0.25 (SQLite for development, PostgreSQL for production)
- **Authentication**: Flask-Login 0.6.3
- **Forms**: Flask-WTF 1.2.1, WTForms 3.0.1
- **Rich Text Editor**: Flask-CKEditor 0.5.1
- **User Avatars**: Flask-Gravatar 0.5.0
- **UI Framework**: Bootstrap 5 (via Bootstrap-Flask 2.3.3)
- **Email**: Python's smtplib
- **Password Security**: Werkzeug (PBKDF2 with SHA-256)
- **Production Server**: Gunicorn 22.0.0

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Gmail account (for contact form email functionality)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Blog2You
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   # On Windows
   python -m pip install -r requirements.txt

   # On macOS/Linux
   pip3 install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory (or set environment variables) with the following:
   ```env
   FLASK_SECRET_KEY=your-secret-key-here
   DB_URI_MAIN=sqlite:///posts.db
   EMAIL_KEY=your-email@gmail.com
   PASSWORD_KEY=your-app-password
   TO_EMAIL=recipient-email@gmail.com
   ```
   
   **Note**: 
   - `FLASK_SECRET_KEY`: Generate a secure random key for Flask sessions
   - `DB_URI_MAIN`: Database URI (SQLite for local development)
   - `EMAIL_KEY`: Your Gmail address
   - `PASSWORD_KEY`: Gmail App Password (not your regular password)
   - `TO_EMAIL`: Email address where contact form messages will be sent

5. **Initialize the database**
   
   The database will be automatically created when you run the application for the first time.

## 🎯 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:5001`

3. **Create an Admin Account**
   - Register a new user account (the first user with `id=1` will be the admin)
   - Admin users can create, edit, and delete blog posts

4. **Password Requirements**
   - Minimum 8 characters
   - At least one uppercase letter
   - At least one lowercase letter
   - At least one digit
   - At least one special character (@$!%*?&)

## 📁 Project Structure

```
Blog2You/
├── main.py                 # Main Flask application file
├── forms.py                # WTForms form definitions
├── requirements.txt        # Python dependencies
├── Procfile                # Heroku deployment configuration
├── instance/
│   └── posts.db           # SQLite database (created automatically)
├── templates/             # Jinja2 HTML templates
│   ├── header.html
│   ├── footer.html
│   ├── index.html         # Homepage with all posts
│   ├── post.html          # Individual post view
│   ├── make-post.html     # Create/Edit post form
│   ├── login.html
│   ├── register.html
│   ├── about.html
│   └── contact.html
└── static/                # Static files
    ├── css/
    │   └── styles.css     # Custom styles
    ├── js/
    │   └── scripts.js     # JavaScript functionality
    └── assets/
        ├── img/           # Background images
        └── favicon.ico
```

## 🔐 Database Models

### User Model
- `id`: Primary key
- `email`: Unique email address
- `password`: Hashed password
- `name`: User's name
- `posts`: Relationship to BlogPost
- `comments`: Relationship to Comment

### BlogPost Model
- `id`: Primary key
- `author_id`: Foreign key to User
- `title`: Post title (unique)
- `subtitle`: Post subtitle
- `date`: Publication date
- `body`: Post content (rich text)
- `img_url`: Header image URL
- `comments`: Relationship to Comment

### Comment Model
- `id`: Primary key
- `text`: Comment content
- `author_id`: Foreign key to User
- `post_id`: Foreign key to BlogPost

## 🌐 Routes

| Route | Method | Description | Access |
|-------|--------|-------------|--------|
| `/` | GET | Homepage with all posts | Public |
| `/register` | GET, POST | User registration | Public |
| `/login` | GET, POST | User login | Public |
| `/logout` | GET | User logout | Authenticated |
| `/post/<int:post_id>` | GET, POST | View individual post and add comments | Public/Authenticated |
| `/new-post` | GET, POST | Create new blog post | Admin only |
| `/edit-post/<int:post_id>` | GET, POST | Edit existing post | Admin only |
| `/delete/<int:post_id>` | GET | Delete a post | Admin only |
| `/about` | GET | About page | Public |
| `/contact` | GET, POST | Contact form | Public |

## 🚢 Deployment

The project includes a `Procfile` for Heroku deployment. To deploy:

1. **Prepare for Heroku**
   - Ensure all environment variables are set in Heroku config vars
   - Update `DB_URI_MAIN` to use PostgreSQL (Heroku Postgres)

2. **Deploy to Heroku**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

3. **Set environment variables on Heroku**
   ```bash
   heroku config:set FLASK_SECRET_KEY=your-secret-key
   heroku config:set DB_URI_MAIN=postgresql://...
   heroku config:set EMAIL_KEY=your-email@gmail.com
   heroku config:set PASSWORD_KEY=your-app-password
   heroku config:set TO_EMAIL=recipient-email@gmail.com
   ```

## 📝 Notes

- The admin user is identified by `id == 1` in the database
- Password hashing uses PBKDF2 with SHA-256 and salt length of 8
- The contact form uses Gmail's SMTP server
- CKEditor is configured for rich text editing in blog posts and comments
- Gravatar is used for user profile images in comments

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

**Note**: Remember to keep your environment variables secure and never commit them to version control. Use a `.env` file (which should be in `.gitignore`) or environment variables for sensitive information.

