from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,EmailField,PasswordField,BooleanField
from wtforms.validators import DataRequired, URL,Email
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


#  Create a RegisterForm to register new users

class RegistrationForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()],render_kw={"class":"password-field","type": "password"})
    btn = BooleanField('Show Password',render_kw={"class":" show-hide-password" ,"value": "" ,"onclick":'togglePasswordVisibility()'})
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


#  Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    btn = BooleanField('Show Password',
                       render_kw={"class": " show-hide-password", "value": "", "onclick": 'togglePasswordVisibility()'})
    submit = SubmitField("Let Me In!")


#  Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment  = CKEditorField(label='Comment',validators=[DataRequired()])
    submit = SubmitField('Comment')

