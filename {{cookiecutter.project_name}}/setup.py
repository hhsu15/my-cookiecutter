from setuptools import setup

VERSION_TEMPLATE = (
    '"""Version of {{ cookiecutter.project_name }}."""\n\n__version__ = "{version}"\n'
)

setup(
    use_scm_version={
        "write_to": "src/{{ cookiecutter.namespace }}/{{ cookiecutter.package_name }}/version.py",
        "write_to_template": VERSION_TEMPLATE,
    }
)