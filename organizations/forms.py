"""Classes for forms related to organizations."""

from django.forms import ModelForm

from organizations.models import Organization


class PopeOrganizationForm(ModelForm):
    class Meta:
        """Meta default."""
        model = Organization
        fields = ['org_name', 'cnpj', 'social_reason', 'email', 'telephone']
