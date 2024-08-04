document.addEventListener('DOMContentLoaded', function() {
    const speciesInfoDiv = document.getElementById('species-info');
    const speciesForm = document.getElementById('species-form');

    function fetchSpeciesInfo() {
        fetch('http://127.0.0.1:8000/zoo_app/species_info')
            .then(response => response.json())
            .then(data => {
                speciesInfoDiv.innerHTML = '';
                data.forEach(species => {
                    const speciesDiv = document.createElement('div');
                    speciesDiv.classList.add('species');
                    speciesDiv.innerHTML = `
                        <p>Name: ${species.name}</p>
                        <p>Description: ${species.description}</p>
                        <button onclick="deleteSpecies('${species._id}')">Delete</button>
                    `;
                    speciesInfoDiv.appendChild(speciesDiv);
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    speciesForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(speciesForm);
        const data = {
            name: formData.get('name'),
            description: formData.get('description')
        };

        fetch('http://127.0.0.1:8000/zoo_app/species_info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            fetchSpeciesInfo();
            speciesForm.reset();
        })
        .catch(error => console.error('Error adding species:', error));
    });

    window.deleteSpecies = function(id) {
        fetch(`http://127.0.0.1:8000/zoo_app/species_info/${id}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            fetchSpeciesInfo();
        })
        .catch(error => console.error('Error deleting species:', error));
    }

    fetchSpeciesInfo();
});
