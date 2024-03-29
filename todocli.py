import typer
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()

@app.command(short_help='add an item')
def add(task: str, category: str):
    typer.echo(f'adding {task}, in category: {category}')
    show()
    
@app.command(short_help='delete an item')
def delete(position: int):
    typer.echo(f'deleting {position}')
    show()
    
@app.command(short_help='update an item')
def update(position: int, task: str = None, category: str = None):
    typer.echo(f'updating {position}')
    show()
    
@app.command(short_help='mark the task as completed')
def complete(position: int):
    typer.echo(f'complete {position}')
    show()

@app.command(short_help='show todo\'s')
def show():
    tasks = [('Todo1', 'Study'), 
             ('Todo2', 'Sports')]
    console.print('[bold magenta]Todos[/bold magenta]', '💻')
    
    table = Table(show_header=True, header_style='bold blue')
    table.add_column('#', style='dim', width=6)
    table.add_column('Todo', min_width=20)
    table.add_column('Category', min_width=12, justify='right')
    table.add_column('Done', min_width=12, justify='right')

    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'Youtube': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'
    
    for index, task in enumerate(tasks, start=1):
        c = get_category_color(task[1])
        is_done_str = '✅' if True == 2 else '❌'
        table.add_row(str(index), task[0], f'[{c}]{task[1]}[/{c}]', is_done_str)
    console.print(table)

if __name__ == '__main__':
    app()