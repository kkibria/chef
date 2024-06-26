# Chef

`chef` builds a project builder.

It is a python CLI tool that does the followings,
- Creates a poetry project.
- Runs git init.
- Creates a license file.

This tool uses [`prj-gen`](https://github.com/kkibria/prj-gen) library.

## Install
`chef` requires `poetry` and `git` installed in your system and added to
`path` already. Recommended way is to install `chef` globally and you will
have to install in administrative mode.

### Using poetry
```
poetry add git+https://github.com/kkibria/chef.git
```

### Using pip
```
pip install chef@git+https://github.com/kkibria/chef.git
```

Without the administrative privilege, you can install it in a virtual
environment as well.

## Running
It can be executed directly from command line,
```
chef <path>
```

You can also run this as a python module,
```
python -m chef <path>
```