from flask import Flask, render_template, request, redirect, url_for


tasks = [
    {
        "name":"do the dishes",
        "description":"none indeed",
        "id":1
    }
]


app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', tasks=tasks)

next_task_id = len(tasks) + 1  # Simple way to generate a new ID

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        form = request.form
        task_name = form.get('name')
        task_description = form.get('description')

        if not task_description:
            task_description = 'None indeed'

        global next_task_id
        tasks.append({
            "name": task_name,
            "description": task_description,
            "id": next_task_id  # Use the generated ID
        })
        next_task_id += 1
        return redirect(url_for('index'))
    

@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')



@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id: int):
    task_to_edit = next((task for task in tasks if task['id'] == id), None)
    if task_to_edit is None:
        return "Task not found", 404

    if request.method == 'POST':
        form = request.form
        task_to_edit['name'] = form.get('name')
        task_to_edit['description'] = form.get('description')
        return redirect(url_for('index'))

    return render_template('edit.html', task=task_to_edit)
        
@app.route('/delete/<int:id>', methods=['GET'])
def delete(id: int):
    for task in tasks:
        if task.get('id') == id:
            tasks.pop(tasks.index(task))
            return redirect(url_for('index'))
app.run()