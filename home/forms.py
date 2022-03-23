from .models import Agent
from django.forms import ModelForm

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'provider', 'email_address', 'phone_number']

    # function for validation
    def clean(self):
 
        super(AgentForm, self).clean()
         
        phone = self.cleaned_data.get('phone_number')
 
        # email validation provided by 'EmailField' in Agent model
        if len(phone) < 9:
            self._errors['phone_number'] = self.error_class([
                'Please enter a valid phone number'])
 
        return self.cleaned_data