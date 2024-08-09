// src/components/Footer.js

import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white py-4">
      <div className="container mx-auto flex flex-col items-center md:flex-row justify-between px-4">
        <div className="text-center md:text-left">
          <h2 className="text-xl font-semibold">Animal Zoo</h2>
          <p className="text-sm mt-1">Your one-stop solution for zoo management.</p>
        </div>
        <div className="mt-4 md:mt-0">
          <ul className="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-4">
            <li><a href="#" className="hover:underline">Home</a></li>
            <li><a href="#" className="hover:underline">About</a></li>
            <li><a href="#" className="hover:underline">Contact</a></li>
            <li><a href="#" className="hover:underline">Privacy Policy</a></li>
          </ul>
        </div>
      </div>
      <div className="bg-gray-900 py-2 text-center text-sm">
        <p>&copy; {new Date().getFullYear()} Animal Zoo. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;