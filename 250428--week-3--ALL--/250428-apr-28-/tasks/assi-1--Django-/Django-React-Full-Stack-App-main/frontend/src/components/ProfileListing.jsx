import { useState } from 'react';
import { FaEnvelope } from 'react-icons/fa';
import { Link } from 'react-router-dom';

const SingleProfilePage = ({ profile}) => {
  
  return (
    <div className='bg-white rounded-xl shadow-md relative'>
      <div className='p-4'>
        <div className='mb-6'>
          <h3 className='text-xl font-bold'>
            {/* {profile.first_name} {profile.last_name} */}
          </h3>
        </div>

        <div className='mb-5 flex items-center'>
          <FaEnvelope className='inline text-lg mb-1 mr-2 text-gray-600' />
          {/* <span>{emailDisplay}</span> */}
        </div>

        <button
          onClick={() => setShowFullEmail((prevState) => !prevState)}
          className='text-indigo-500 mb-5 hover:text-indigo-600'
        >
          {/* {showFullEmail ? 'Hide Email' : 'Show Full Email'} */}
        </button>
{/* 
        <div className='border border-gray-100 mb-5'>
        {profile.email}
        </div> */}

        <div style={{
    border: '1px solid #e0e0e0', /* Refined border color */
    borderRadius: '0.5rem',       /* Slightly rounded corners */
    marginBottom: '1.25rem',
    padding: '0.75rem',         /* Added padding for better spacing */
    backgroundColor: '#fafafa',  /* Very light background color */
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)', /* Subtle shadow */
    fontFamily: 'Roboto, Arial, sans-serif',  /* Modern font */
    color: '#3c4043',             /* Darker, more readable text */
    fontSize: '0.9rem',
    lineHeight: '1.4rem'
}}>
    {profile.id}
</div>

{/* <h1> ------------------------------------- </h1> */}


{/* <h1> ------------------------------------- </h1> */}

<div style={{
    border: '1px solid #e0e0e0', /* Refined border color */
    borderRadius: '0.5rem',       /* Slightly rounded corners */
    marginBottom: '1.25rem',
    padding: '0.75rem',         /* Added padding for better spacing */
    backgroundColor: '#fafafa',  /* Very light background color */
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)', /* Subtle shadow */
    fontFamily: 'Roboto, Arial, sans-serif',  /* Modern font */
    color: '#3c4043',             /* Darker, more readable text */
    fontSize: '0.9rem',
    lineHeight: '1.4rem'
}}>
    {profile.email}
</div>
{/* <h1> ------------------------------------- </h1> */}

<div style={{
    border: '1px solid #e0e0e0', /* Refined border color */
    borderRadius: '0.5rem',       /* Slightly rounded corners */
    marginBottom: '1.25rem',
    padding: '0.75rem',         /* Added padding for better spacing */
    backgroundColor: '#fafafa',  /* Very light background color */
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)', /* Subtle shadow */
    fontFamily: 'Roboto, Arial, sans-serif',  /* Modern font */
    color: '#3c4043',             /* Darker, more readable text */
    fontSize: '0.9rem',
    lineHeight: '1.4rem'
}}>
    {profile.bio}
</div>
{/* <h1> ------------------------------------- </h1> */}

        {/* <div style={{
    border: '1px solid #e5e7eb',
    marginBottom: '1.25rem',
}}>
    {profile.email}
</div>

        <div className='border border-gray-100 mb-5'>
        {profile.id}
        </div> */}

        <div className='flex flex-col lg:flex-row justify-between mb-4'>
          <Link
            // to={`/profiles/${profile.id}`}
            to={`/profiles/open`}
            className='h-[36px] bg-indigo-500 hover:bg-indigo-600 text-white px-4 py-2 rounded-lg text-center text-sm'
          >
            Go to Profile
          </Link>
        </div>
      </div>
    </div>
  );
};

export default SingleProfilePage;
