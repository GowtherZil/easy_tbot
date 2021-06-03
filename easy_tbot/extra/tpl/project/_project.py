from pathlib import Path

BASE_PATH= Path(__file__).parent

TEMPLATES = [
    BASE_PATH/'botmanager.py.tpl',
    BASE_PATH/'settings.py.tpl'
    ]


def create_project(name, token):
    target_path = Path(f'./{name}')
    
    if target_path.exists():
        raise FileExistsError('A directory with this name already exist in this location')
    
    target_path.mkdir()

    for tlp in TEMPLATES:
        current_path = target_path/tlp.stem
        with open(tlp) as source:
            with open(current_path, 'w') as to:
                raw_data = source.read()
                with_context_data = raw_data.format_map({
                    'name':name,
                    'token':token
                })
                to.write(with_context_data)


