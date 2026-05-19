from pathlib import Path
import yaml
import os

def load_yaml_data(file:str)->dict:
    """Loads seed data from a YAML file in the management seeds directory."""
    main_directory='apps/projects/management/seeds/data'
    full_path=os.path.join(main_directory,file)

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Seed file not found at: {full_path}")
    
    with open(full_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data or {}

def load_yaml_directory(directory:str) -> list[dict]:
    """Discovers, loads, and collects all project YAML files from the projects sub-directory."""
    main_directory = Path('apps/projects/management/seeds/data')
    directory_path = main_directory / directory

    if not directory_path.is_dir():
        print(f"Error: Projects directory not found at {directory_path}")
        return []
    
    all_files = []

    for file_path in directory_path.glob("*.y*ml"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                project_data = yaml.safe_load(f)

                if project_data:
                    all_files.append(project_data)

        except yaml.YAMLError as exc:
            print(f"YAML Syntax Error in file {file_path.name}: {exc}")
        except Exception as exc:
            print(f"Failed to read file {file_path.name}: {exc}")

    print(f"Total entries prepared for database ingestion: {len(all_files)}")
    return all_files

