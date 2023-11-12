from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError, NumberRange
from market.models import User

class RegistrationForm(FlaskForm):
    username = StringField(label="User Name:", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email Address:", validators=[Email(), DataRequired()])
    mobile = StringField(label="Mobile Number:", validators=[DataRequired()])
    password1 = PasswordField(label="Password:", validators=[DataRequired()])
    password2 = PasswordField(label="Confirm Password:", validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label="Register")

    def validate_username(self, username_check):
        user = User.query.filter_by(username=username_check.data).first()
        if user:
            raise ValidationError("Username already exists. Please try a different username")

    def validate_email(self, email_check):
        email = User.query.filter_by(email_address=email_check.data).first()
        if email:
            raise ValidationError("Email already exists. Please try a different email")

    def validate_mobile(self, mobile_check):
        mobile = User.query.filter_by(mobile=mobile_check.data).first()
        if mobile:
            raise ValidationError("Mobile number already exists. Please try a different mobile")

class LoginForm(FlaskForm):
    username = StringField(label="User Name:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Login")

class SearchForm(FlaskForm):
    searched = StringField(label="Search here")
    submit = SubmitField(label='Submit')


