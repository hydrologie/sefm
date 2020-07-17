{%- extends 'full.tpl' -%}

{% block output_group %}
<div class="output_hidden">
{{ super() }}
</div>
{% endblock output_group %}

{%- block header -%}
{{ super() }}

<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>

<style type="text/css">
div.output_wrapper {
  margin-top: 0px;
}
.output_hidden {
  overflow-y: scroll;
    max-height: 1000px;
}
</style>

<script>

</script>
{%- endblock header -%}
