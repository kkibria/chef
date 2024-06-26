# {{__target__|title}}

`{{__target__}}` {{description|lower}}.

It is a python CLI tool that does the followings,
- Creates a poetry project.
- Runs git init.
- Creates a license file.

This tool is built with [`chef`](https://github.com/kkibria/chef) which uses
[`prj-gen`](https://github.com/kkibria/prj-gen) library to perform generation.

## Install
`{{__target__}}` requires `poetry` and `git` installed in your system and added to
`path` already. Recommended way is to install `{{__target__}}` globally and you will
have to install in administrative mode.

### Using poetry
```
poetry add git+https://github.com/{{github_user}}/{{__target__}}.git
```

### Using pip
```
pip install {{__target__}}@git+https://github.com/{{github_user}}/{{__target__}}.git
```

Without the administrative privilege, you can install it in a virtual
environment as well.

## Running
It can be executed directly from command line,
```
{{__target__}} <path>
```

You can also run this as a python module,
```
python -m {{__target__}} <path>
```
