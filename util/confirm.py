"""
    Confirmación si el usuario desea realizar acción
"""

def confirm(msg):
    confirm = (input(msg)).lower()
    if confirm == 'si':
        return True
    elif confirm == 'no':
        return False
    else:
        print(f"\nOpción inválida")
        return False