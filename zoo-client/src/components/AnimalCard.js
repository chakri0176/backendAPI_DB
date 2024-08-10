// src/components/AnimalCard.js
import React, { useState } from "react";

const AnimalCard = ({ animal }) => {
  const [expanded, setExpanded] = useState(false);

  const toggleExpand = () => setExpanded(!expanded);

  return (
    <div className="bg-yellow-50 rounded-3xl shadow-lg overflow-hidden transition-all duration-300 hover:shadow-xl hover:scale-105">
      <div className="bg-green-400 p-4 flex items-center justify-between">
        <h2 className="text-3xl font-bold text-white">{animal.Animal_name}</h2>
        <span className="text-5xl">{getAnimalEmoji(animal.Species_name)}</span>
      </div>
      <div className="p-4">
        {/* Display animal image */}
        <div className="mb-4">
          <img
            src={animal.Species_info.Species_image_url}
            alt={`${animal.Species_name}`}
            className="w-full h-auto object-cover rounded-lg"
          />
        </div>
        <p className="text-gray-800">
          <strong>Species:</strong> {animal.Species_name}
        </p>
        <p className="text-gray-800">
          <strong>Sex:</strong> {animal.Animal_sex}
        </p>
        <p className="text-gray-800">
          <strong>Location:</strong> {animal.Current_animal_location}
        </p>
        <p className="text-gray-800">
          <strong>Birthdate:</strong>{" "}
          {new Date(animal.Animal_birthdate).toLocaleDateString()}
        </p>

        <button
          onClick={toggleExpand}
          className="mt-4 bg-blue-400 text-white px-6 py-2 rounded-full hover:bg-blue-500 transition-transform duration-300 hover:scale-105"
        >
          {expanded ? "Show Less" : "Show More"}
        </button>

        {expanded && (
          <div className="mt-4">
            <h3 className="text-xl font-semibold mb-2 text-green-500">
              Enclosure Info
            </h3>
            <p className="text-gray-800">
              <strong>Name:</strong> {animal.Enclosure_info.Enclosure_name}
            </p>
            <p className="text-gray-800">
              <strong>Type:</strong> {animal.Enclosure_info.Enclosure_type}
            </p>
            <p className="text-gray-800">
              <strong>Capacity:</strong>{" "}
              {animal.Enclosure_info.Enclosure_capacity}
            </p>

            <h3 className="text-xl font-semibold mt-4 mb-2 text-green-500">
              Species Info
            </h3>
            <p className="text-gray-800">
              <strong>Food Type:</strong> {animal.Species_info.Food_type}
            </p>
            <p className="text-gray-800">
              <strong>Lifespan:</strong> {animal.Species_info.Species_lifespan}{" "}
              years
            </p>
            <p className="text-gray-800">
              <strong>Type:</strong> {animal.Species_info.Species_type}
            </p>

            <h3 className="text-xl font-semibold mt-4 mb-2 text-green-500">
              Recent Feeding
            </h3>
            {animal.Feeding_records.length > 0 && (
              <p className="text-gray-800">
                <strong>
                  {new Date(
                    animal.Feeding_records[0].Food_time
                  ).toLocaleDateString()}
                  :
                </strong>{" "}
                {animal.Feeding_records[0].Food_type} (
                {animal.Feeding_records[0].Food_weight} kg)
              </p>
            )}

            <h3 className="text-xl font-semibold mt-4 mb-2 text-green-500">
              Recent Health Check
            </h3>
            {animal.Health_records.length > 0 && (
              <p className="text-gray-800">
                <strong>
                  {new Date(
                    animal.Health_records[0].Health_event_time
                  ).toLocaleDateString()}
                  :
                </strong>{" "}
                {animal.Health_records[0].Health_event_type} -{" "}
                {animal.Health_records[0].Health_event_comments}
              </p>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

function getAnimalEmoji(species) {
  const emojiMap = {
    Tiger: "🐯",
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
