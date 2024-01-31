from blog.models import PostComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ("full_name", "email", "website", "message")

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"]
        if len(full_name) < 3:
            raise forms.ValidationError("Full name must be at least 3 characters long.")
        return full_name

    def clean_email(self):
        email = self.cleaned_data["email"]
        from django.core.validators import EmailValidator

        email_validator = EmailValidator("Enter a valid email address.")
        email_validator(email)
        return email

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields["full_name"].widget.attrs["placeholder"] = "Full Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["website"].widget.attrs["placeholder"] = "Website"
        self.fields["message"].widget.attrs["placeholder"] = "Message"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
