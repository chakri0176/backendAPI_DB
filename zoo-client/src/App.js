// src/App.js
import React, { useState } from 'react';
import AnimalCard from './components/AnimalCard';
import SearchBar from './components/SearchBar';
import useFetchAnimals from './hooks/useFetchAnimals';
import './App.css';

function App() {
  const { animals, loading, error } = useFetchAnimals();
  const [searchTerm, setSearchTerm] = useState('');

  if (loading) {
    return <div className="flex justify-center items-center h-screen text-xl font-semibold">Loading...</div>;
  }

  if (error) {
    return <div className="flex justify-center items-center h-screen text-xl text-red-500">Error: {error}</div>;
  }

  const filteredAnimals = animals.filter(animal =>
    animal.Animal_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    animal.Species_name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="bg-gradient-to-r from-blue-100 to-green-100 min-h-screen">
      <header className="bg-white shadow-md py-4">
        <div className="container mx-auto px-4">
          <h1 className="text-3xl font-bold text-gray-800">Zoo Keeper</h1>
        </div>
      </header>
      <main className="container mx-auto px-4 py-8">
        <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
          {filteredAnimals.map(animal => (
            <AnimalCard key={animal._id} animal={animal} />
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;