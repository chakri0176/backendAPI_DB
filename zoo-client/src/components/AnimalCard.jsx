// src/components/AnimalCard.js
import React from "react";

const AnimalCard = ({ animal }) => {
  return (
    <div className="bg-white rounded-lg shadow-lg overflow-hidden transition-transform duration-300 hover:scale-105">
      <div className="bg-gray-200 h-48 flex items-center justify-center">
        <span className="text-6xl">{getAnimalEmoji(animal.Species_name)}</span>
      </div>
      <div className="p-6">
        <h2 className="text-xl font-semibold mb-2">{animal.Animal_name}</h2>
        <p className="text-gray-600">
          <strong>Species:</strong> {animal.Species_name}
        </p>
        <p className="text-gray-600">
          <strong>Sex:</strong> {animal.Animal_sex}
        </p>
        <p className="text-gray-600">
          <strong>Location:</strong> {animal.Current_animal_location}
        </p>
        <p className="text-gray-600">
          <strong>Birthdate:</strong>{" "}
          {new Date(animal.Animal_birthdate).toLocaleDateString()}
        </p>
      </div>
    </div>
  );
};

function getAnimalEmoji(species) {
  const emojiMap = {
    Lion: "🦁",
    Elephant: "🐘",
    Giraffe: "🦒",
    Penguin: "🐧",
    Monkey: "🐒",
    // Add more species and emojis as needed
  };
  return emojiMap[species] || "🐾";
}

export default AnimalCard;
