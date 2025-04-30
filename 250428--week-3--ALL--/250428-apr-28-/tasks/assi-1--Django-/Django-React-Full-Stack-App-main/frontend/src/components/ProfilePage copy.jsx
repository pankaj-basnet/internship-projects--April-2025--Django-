// D:\GROW_CTS\PANKAJ-PROJECTS-\250428--week-3--ALL--\250428-apr-28-\tasks\assi-1--Django-\Django-React-Full-Stack-App-main\frontend\src\components\ProfilePage copy.jsx
// not as per traversy react jobsApp project
// updated code in ProfilePage.jsx

import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ProfilePage() {
    const [userData, setUserData] = useState({
        first_name: '',
        last_name: '',
        email: '',
    });

    const [loading, setLoading] = useState(true);
    const [message, setMessage] = useState('');

    // Fetch user profile when component mounts
    useEffect(() => {
        axios.get('/api/profile/', {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('access_token')}`
            }
        })
        .then(response => {
            setUserData(response.data);
            setLoading(false);
        })
        .catch(error => {
            console.error(error);
            setLoading(false);
        });
    }, []);

    // Handle form input change
    const handleChange = (e) => {
        setUserData({
            ...userData,
            [e.target.name]: e.target.value
        });
    };

    // Handle form submit
    const handleSubmit = (e) => {
        e.preventDefault();
        axios.put('/api/profile/', userData, {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('access_token')}`
            }
        })
        .then(response => {
            setMessage('Profile updated successfully!');
        })
        .catch(error => {
            console.error(error);
            setMessage('Failed to update profile.');
        });
    };

    if (loading) return <p>Loading...</p>;

    return (
        <div>
            <h2>Edit Profile</h2>
            {message && <p>{message}</p>}
            <form onSubmit={handleSubmit}>
                <div>
                    <label>First Name:</label>
                    <input 
                        type="text" 
                        name="first_name" 
                        value={userData.first_name}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Last Name:</label>
                    <input 
                        type="text" 
                        name="last_name" 
                        value={userData.last_name}
                        onChange={handleChange}
                    />
                </div>
                <div>
                    <label>Email:</label>
                    <input 
                        type="email" 
                        name="email" 
                        value={userData.email}
                        onChange={handleChange}
                    />
                </div>
                <button type="submit">Save Changes</button>
            </form>
        </div>
    );
}

export default ProfilePage;
