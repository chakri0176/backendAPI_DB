// src/App.js
import React, { useState } from 'react';
import AnimalCard from './components/AnimalCard';
import SearchBar from './components/SearchBar';
import useFetchAnimals from './hooks/useFetchAnimals';
import './App.css';
import Footer from './components/Footer';

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
    <div className="bg-gray-100 min-h-screen">
      <header className="bg-green-500 shadow-md py-4 sticky top-0 z-10">
        <div className="container mx-auto px-4 flex justify-between items-center">
          <h1 className="text-3xl font-bold text-white">Zoo Keeper</h1>
          <nav>
            <button
              onClick={() => window.location.href = '/add-animal'}
              className="bg-white text-green-500 px-4 py-2 rounded-full font-semibold hover:bg-green-100 transition-colors duration-300">Add Animals</button>
          </nav>
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
      <Footer />
    </div>
  );
}

export default App;