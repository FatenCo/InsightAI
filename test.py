import subprocess

# Chemin du fichier à analyser
file_path = 'D:/BDBI/stage/projet/tao/tao/toolkit/tao/eval.py'

# Obtenir la liste des commits modifiant ce fichier
log_command = f'git log --pretty=format:"%H" --follow -- {file_path}'
commits = subprocess.check_output(log_command, shell=True).decode().split('\n')

# Compter les commits qui modifient les fonctions ou le code source
modification_count = 0

for commit in commits:
    # Obtenir les modifications de ce commit
    show_command = f'git show {commit} -- {file_path}'
    diff = subprocess.check_output(show_command, shell=True).decode()
    
    # Vérifier si le diff contient des modifications de code
    if 'def ' in diff or any(keyword in diff for keyword in ['+', '-']):
        modification_count += 1

print(f'Nombre de tickets ayant modifié une fonction ou le code source : {modification_count}')
