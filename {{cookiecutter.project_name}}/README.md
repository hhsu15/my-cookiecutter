# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Project Documentation

{% set to_do_text = 'Documentation or link to documentation here' -%}

{% for i in to_do_text %}={% endfor %}

{{ to_do_text }}

{% for i in to_do_text %} = {% endfor %}

## Developer

- [{{ cookiecutter.author_github_username }}] (https://github.com/{{ cookiecutter.author_github_username }})
