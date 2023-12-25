from django.test import TestCase

# Create your tests here. HTML-форма в файле layout.html в папке "templates" внутри приложения:

<form method="post" action="{% url 'feedback' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Отправить отзыв</button>
</form>


'''Здесь form.as_p автоматически отображает поля формы в виде абзацев.'''