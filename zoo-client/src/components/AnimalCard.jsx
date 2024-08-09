import React from 'react';

const AnimalCard = ({ animal }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow-lg">
      <h2 className="text-xl font-semibold">{animal.Animal_name}</h2>
      <p><strong>Species:</strong> {animal.Species_name}</p>
      <p><strong>Sex:</strong> {animal.Animal_sex}</p>
      <p><strong>Location:</strong> {animal.Current_animal_location}</p>
      <p><strong>Birthdate:</strong> {new Date(animal.Animal_birthdate).toLocaleDateString()}</p>
    </div>
  );
};

export default AnimalCard;