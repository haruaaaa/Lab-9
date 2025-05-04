function addRecord() {
    const date = document.getElementById('date').value;
    const steps = document.getElementById('steps').value;

    if (!date || !steps) {
        alert('Please fill all fields');
        return;
    }

    fetch('/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            date: date,
            steps: parseInt(steps)
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            
            const newItem = document.createElement('li');
            newItem.innerHTML = `<div>${date} - ${steps} steps</div>`;
            document.getElementById('recordsList').prepend(newItem);
            
            
            document.getElementById('recordForm').reset();
        }
    })
    .catch(error => console.error('Error:', error));
}

function clearAll() {
    if (confirm('Are you sure you want to delete all records?')) {
        fetch('/clear', {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                document.getElementById('recordsList').innerHTML = '';
            }
        })
        .catch(error => console.error('Error:', error));
    }
}