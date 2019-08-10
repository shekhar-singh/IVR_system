from django import template
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
	css = css.split(";")
	return field.as_widget(attrs={"class": css[0], "placeholder": css[1]})

@register.filter(name='addplaceholder')
def addplaceholder(field, placeholder):
	return field.as_widget(attrs={"placeholder": placeholder})