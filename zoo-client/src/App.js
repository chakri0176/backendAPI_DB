// src/App.js
import React from 'react';
import AnimalCard from './components/AnimalCard';
import useFetchAnimals from './hooks/useFetchAnimals';
import './App.css';

function App() {
  const { animals, loading, error } = useFetchAnimals();

  if (loading) {
    return <div className="text-center text-xl font-semibold">Loading...</div>;
  }

  if (error) {
    return <div className="text-center text-xl text-red-500">Error: {error}</div>;
  }

  return (
    <div className="bg-red-200 min-h-screen p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">Zoo Animals</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {animals.map(animal => (
          <AnimalCard key={animal._id} animal={animal} />
        ))}
      </div>
    </div>
  );
}

export default App;
