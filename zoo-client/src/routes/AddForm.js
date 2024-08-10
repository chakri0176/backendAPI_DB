import React, { useState } from 'react';
import axios from 'axios';

const AddAnimal = () => {
    const [formData, setFormData] = useState({
        Animal_name: '',
        Animal_birthdate: '',
        Animal_sex: '',
        Current_animal_location: '',
        Species_name: '',
        Enclosure_info: {
            Animal_capacity: '',
            Current_population: '',
            Enclosure_condition: '',
            Enclosure_location: '',
            Enclosure_name: ''
        },
        Species_info: {
            Food_type: '',
            Species_image_url: '',
            Species_lifespan: '',
            Species_type: ''
        },
        Feeding_records: [
            {
                Feeding_action_type: '',
                Food_time: '',
                Food_type: '',
                Food_weight: '',
            }
        ],
        Health_records: [
            {
                Health_check_date: '',
                Health_notes: '',
                Health_status: '',
            }
        ]
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleNestedChange = (e, nested) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [nested]: {
                ...prevState[nested],
                [name]: value
            }
        }));
    };

    const handleArrayChange = (e, index, arrayName) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [arrayName]: prevState[arrayName].map((item, i) =>
                i === index ? { ...item, [name]: value } : item
            )
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
        try {
            const response = await axios.post(BACKEND_URL + '/animals/add_animal', formData);
            console.log(response.data);
            alert('Animal added successfully!');
        } catch (error) {
            console.error('Error adding animal:', error);
            alert('Error adding animal. Please try again.');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="max-w-lg mx-auto mt-10 p-6 bg-white rounded shadow-md">
            <h2 className="text-2xl font-bold mb-6">Add New Animal</h2>

            <div className="mb-4">
                <label className="block mb-2">Animal Name:</label>
                <input
                    type="text"
                    name="Animal_name"
                    value={formData.Animal_name}
                    onChange={handleChange}
                    className="w-full p-2 border rounded"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block mb-2">Birthdate:</label>
                <input
                    type="datetime-local"
                    name="Animal_birthdate"
                    value={formData.Animal_birthdate}
                    onChange={handleChange}
                    className="w-full p-2 border rounded"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block mb-2">Sex:</label>
                <select
                    name="Animal_sex"
                    value={formData.Animal_sex}
                    onChange={handleChange}
                    className="w-full p-2 border rounded"
                    required
                >
                    <option value="">Select Sex</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                </select>
            </div>

            <div className="mb-4">
                <label className="block mb-2">Current Location:</label>
                <input
                    type="text"
                    name="Current_animal_location"
                    value={formData.Current_animal_location}
                    onChange={handleChange}
                    className="w-full p-2 border rounded"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block mb-2">Species Name:</label>
                <input
                    type="text"
                    name="Species_name"
                    value={formData.Species_name}
                    onChange={handleChange}
                    className="w-full p-2 border rounded"
                    required
                />
            </div>

            <h3 className="text-xl font-semibold mt-6 mb-4">Enclosure Information</h3>
            {Object.keys(formData.Enclosure_info).map(key => (
                <div key={key} className="mb-4">
                    <label className="block mb-2">{key.replace(/_/g, ' ')}:</label>
                    <input
                        type="text"
                        name={key}
                        value={formData.Enclosure_info[key]}
                        onChange={(e) => handleNestedChange(e, 'Enclosure_info')}
                        className="w-full p-2 border rounded"
                        required
                    />
                </div>
            ))}

            <h3 className="text-xl font-semibold mt-6 mb-4">Species Information</h3>
            {Object.keys(formData.Species_info).map(key => (
                <div key={key} className="mb-4">
                    <label className="block mb-2">{key.replace(/_/g, ' ')}:</label>
                    <input
                        type="text"
                        name={key}
                        value={formData.Species_info[key]}
                        onChange={(e) => handleNestedChange(e, 'Species_info')}
                        className="w-full p-2 border rounded"
                        required
                    />
                </div>
            ))}

            <h3 className="text-xl font-semibold mt-6 mb-4">Feeding Record</h3>
            {formData.Feeding_records.map((record, index) => (
                <div key={index} className="mb-4 p-4 border rounded">
                    {Object.keys(record).map(key => (
                        <div key={key} className="mb-4">
                            <label className="block mb-2">{key.replace(/_/g, ' ')}:</label>
                            <input
                                type={key.includes('time') ? 'datetime-local' : 'text'}
                                name={key}
                                value={record[key]}
                                onChange={(e) => handleArrayChange(e, index, 'Feeding_records')}
                                className="w-full p-2 border rounded"
                                required
                            />
                        </div>
                    ))}
                </div>
            ))}

            <h3 className="text-xl font-semibold mt-6 mb-4">Health Record</h3>
            {formData.Health_records.map((record, index) => (
                <div key={index} className="mb-4 p-4 border rounded">
                    {Object.keys(record).map(key => (
                        <div key={key} className="mb-4">
                            <label className="block mb-2">{key.replace(/_/g, ' ')}:</label>
                            <input
                                type={key.includes('date') ? 'datetime-local' : 'text'}
                                name={key}
                                value={record[key]}
                                onChange={(e) => handleArrayChange(e, index, 'Health_records')}
                                className="w-full p-2 border rounded"
                                required
                            />
                        </div>
                    ))}
                </div>
            ))}

            <button type="submit" className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600">
                Add Animal
            </button>
        </form>
    );
};

export default AddAnimal;