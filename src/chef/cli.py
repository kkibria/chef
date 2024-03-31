import argparse
from pathlib import Path
from warnings import warn

from . import get_template_path, set_warnigs_hook
from .hook import MyGen


def build(params, path, force, **kwargs):
    dst = Path(path)
    if not force:
        if dst.exists():
            warn(f'"{path}" already exists, use --force, exiting!')
            return
    g = MyGen(get_template_path())
    g.update_params(params)
    g.exclude_add('__pycache__'.split())
    g.run(dst)

def main():
    params = {"app": __name__.split(".")[0]}

    parser = argparse.ArgumentParser(
        prog=params["app"],
        description='Builds a project builder',
        epilog=f'python -m {params["app"]}')

    parser.add_argument('path')
    parser.add_argument('-f', '--force', default=False,
                    action='store_true')
    
    args = parser.parse_args()
    params = params | vars(args)

    set_warnigs_hook()
    try:
        build(params, **params)
    except Exception as e:
        print(f'{e.__class__.__name__}:', *e.args)
        return 1

    print(f'"{args.path}" has been created. Run "poetry install" from')
    print(f'inside "{args.path}" to get all the dependencies installed.')
    
    return 0