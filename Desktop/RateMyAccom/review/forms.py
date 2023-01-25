from django import forms
class PostSearchForm(forms.Form):
    q = forms.CharField()
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['q'].label = 'Search For'
        self.fields['q'].widget.attrs.update(
            {'class': 'w-full text-black rounded-md border border-gray-300 bg-white py-2 pl-3 pr-12 shadow-sm focus:border-indigo-500 focus:outline-none focus:ring-1 focus:ring-indigo-500 sm:text-sm'})
        self.fields['q'].widget.attrs.update(
            {'data-toggle': 'dropdown','placeholder':'Start typing your univeristy ...'})
