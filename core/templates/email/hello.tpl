{% extends "mail_templated/base.tpl" %}

{% block subject %}
Activation
{% endblock %}

{% block html %}
{{token}}
{% endblock %}