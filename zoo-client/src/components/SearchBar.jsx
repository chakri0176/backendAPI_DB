// src/components/SearchBar.js
import React from "react";

const SearchBar = ({ searchTerm, setSearchTerm }) => {
  return (
    <div className="relative">
      <input
        type="text"
        placeholder="Search animals..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500"
      />
      <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none"></div>
    </div>
  );
};

export default SearchBar;
