from django import forms

from .models import product 

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ('title','Description','Price')


    # def clean_title(self,*args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     # if "CFE" in title:
    #     #     return title
        
    #     # else: 
    #     #     raise forms.ValidationError("This is not a valid title ")
        
    #     if not "CFE" in title:
    #         raise forms.ValidationError("This is not a valid title")

    #     if not "news" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title

    # def clean_email(self,*args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("this is not a valid email")

    #     return email



class RawProductForm(forms.Form):
    title = forms.CharField()
    Description = forms.CharField(widget = forms.Textarea(
                                attrs = {
                                    "placeholser":"your description",
                                    "class":"new-class-name two",
                                    "id": "my-id-for-textarea",
                                    "row":10,
                                    "cols":30,

                                }

                        )

                        )
    Price = forms.DecimalField(initial= 199.99,widget=forms.Textarea(attrs={"placeholder": "your price"}))

      