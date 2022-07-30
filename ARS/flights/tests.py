from django.test import TestCase

# Create your tests here.
<h3>
      {% for  flight in flights  %}

      <li><a href="{%  url 'flight' flight.id %}">
          {{ flight.id }} {{ flight.origin }} to  {{ flight.destination }}
          </a>
      </li>
      {% endfor %}
  </h3>
{% for  flight in results  %}
{ % endfor %}

li><a href="{%  url 'flight' air.id %}">
          {{ air.id }} {{ flight.origin }} to  {{ flight.destination }}
          </a>
      </li>

< h1 > Search
Results < / h1 >
< h3 >
{ %
for flight in flights %}

< li > < a
href = "{%  url 'flight' flight.id %}" >
{{flight.id}}
{{flight.origin}}
to
{{flight.destination}}
< / a >
< / li >
{ % endfor %}
< / h3 >

< h1 > Available
flights < / h1 >