
import json_manager
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='nombre de el usuario')
@click.option('--age', required=True, help='edad de el usuario')
@click.pass_context
def new(ctx, name, age):
    if not name or not age:
        ctx.fail('El nombre y edad son requeridos')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_user = {
            'id': new_id,
            'name': name,
            'age': age
        }
        data.append(new_user)
        json_manager.write_json(data)
        print(f"Usuario {name} {age} agregado satisfactoriamente con ID {new_id}")

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['age']}")

@cli.command()
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((u for u in data if u['id'] == id), None)
    if user is None:
        print(f"Usuario con ID {id} no encontrado")
    else:
        print(f"{user['id']} - {user['name']} - {user['age']}")


@cli.command()
@click.argument('id', type=int)
@click.option('--name', help='nuevo nombre de el usuario')
@click.option('--age', help='nueva edad de el usuario')
@click.pass_context
def update(ctx, id, name, age):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if name is not None:
                user['name'] = name
            if age is not None:
                user['age'] = age
            break
    json_manager.write_json(data)
    print(f"Usuario con ID {id} actualizado satisfactoriamente")


@cli.command()
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((u for u in data if u['id'] == id), None)
    if user is None:
        print(f"Usuario con ID {id} no encontrado")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"Usuario con ID {id} eliminado satisfactoriamente")

if __name__ == '__main__':
    cli()  

