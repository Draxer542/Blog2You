from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField
import re
from wtforms.validators import ValidationError

def validate_password(form, field):
    password = field.data
    regex = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    if not re.match(regex, password):
        raise ValidationError(
            "Password must be at least 8 characters long, include an uppercase letter, "
            "a lowercase letter, a digit, and a special character."
        )

# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create a form to register new users
class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField("Password", validators=[DataRequired(), validate_password])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


# Create a form to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")


# Create a form to add comments
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
