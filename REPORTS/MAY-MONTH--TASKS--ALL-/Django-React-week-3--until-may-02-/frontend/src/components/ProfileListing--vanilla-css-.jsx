import React, { useState } from 'react';
import { FaEnvelope } from 'react-icons/fa';
import { Link } from 'react-router-dom';

const SingleProfilePage = ({ profile }) => {

  return (
    <div style={{
      backgroundColor: '#ffffff',
      borderRadius: '0.75rem',
      boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      position: 'relative',
    }}>
      <div style={{
        padding: '1rem',
      }}>
        <div style={{
          marginBottom: '1.5rem',
        }}>
          <h3 style={{
            fontSize: '1.25rem',
            fontWeight: 'bold',
          }}>
            {profile.name}
            {/* {profile.name} {profile.last_name} */}
          </h3>
        </div>
        <div style={{
          marginBottom: '1.5rem',
        }}>
          <h3 style={{
            fontSize: '1.25rem',
            fontWeight: 'bold',
          }}>
            {profile.bio}
          </h3>
        </div>

        <div style={{
          marginBottom: '1.25rem',
          display: 'flex',
          alignItems: 'center',
        }}>
          <FaEnvelope style={{
            fontSize: '1rem',
            marginBottom: '0.25rem',
            marginRight: '0.5rem',
            color: '#6b7280',
            display: 'inline-block'
          }} />
          <span>{emailDisplay}</span>
        </div>


        <div style={{
          border: '1px solid #e5e7eb',
          marginBottom: '1.25rem',
        }}>
          {profile.username}
        </div>
        <div style={{
          border: '1px solid #e5e7eb',
          marginBottom: '1.25rem',
        }}>
          {profile.id}
        </div>

        <div style={{
          display: 'flex',
          flexDirection: 'column',
          '@media (min-width: 1024px)': {
            flexDirection: 'row',
            justifyContent: 'space-between',
          },
          marginBottom: '1rem',
        }}>
          <Link
            to={`/profiles/${profile.id}`}
            style={{
              height: '2.25rem',
              backgroundColor: '#6366f1',
              color: '#ffffff',
              padding: '0.5rem 1rem',
              borderRadius: '0.375rem',
              textAlign: 'center',
              fontSize: '0.875rem',
              textDecoration: 'none',
              transition: 'background-color 0.2s ease-in-out',
            }}
          >
            Go to Profile
          </Link>
        </div>
      </div>
    </div>
  );
};

export default SingleProfilePage;
