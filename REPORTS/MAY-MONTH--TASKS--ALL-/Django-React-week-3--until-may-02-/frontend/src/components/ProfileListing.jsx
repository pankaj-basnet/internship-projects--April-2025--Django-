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
        </button>


        <div style={{
    border: '1px solid #e0e0e0', 
    borderRadius: '0.5rem',       
    marginBottom: '1.25rem',
    padding: '0.75rem',         
    backgroundColor: '#fafafa',  
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)', 
    fontFamily: 'Roboto, Arial, sans-serif',  
    color: '#3c4043',             
    fontSize: '0.9rem',
    lineHeight: '1.4rem'
}}>
    {profile.id}
</div>


<div style={{
    border: '1px solid #e0e0e0', 
    borderRadius: '0.5rem',       
    marginBottom: '1.25rem',
    padding: '0.75rem',         
    backgroundColor: '#fafafa',  
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)', 
    fontFamily: 'Roboto, Arial, sans-serif',  
    color: '#3c4043',             
    fontSize: '0.9rem',
    lineHeight: '1.4rem'
}}>
    {profile.email}
</div>


<div style={{
    border: '1px solid #e0e0e0', 
    borderRadius: '0.5rem',       
    marginBottom: '1.25rem',
    padding: '0.75rem',         
    backgroundColor: '#fafafa',  
    boxShadow: '0 1px 3px rgba(0, 0, 0, 0.1)', 
    fontFamily: 'Roboto, Arial, sans-serif',  
    color: '#3c4043',             
    fontSize: '0.9rem',
    lineHeight: '1.4rem'
}}>
    {profile.bio}
</div>


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
