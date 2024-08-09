// src/hooks/useFetchAnimals.js
import { useState, useEffect } from 'react';

const useFetchAnimals = () => {
    const [animals, setAnimals] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

    useEffect(() => {
        const fetchAnimals = async () => {
            try {
                const response = await fetch(BACKEND_URL + '/animals');
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setAnimals(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchAnimals();
    }, [BACKEND_URL]);

    return { animals, loading, error };
};

export default useFetchAnimals;
