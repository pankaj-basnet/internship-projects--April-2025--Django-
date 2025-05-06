 
import { useState, useEffect } from 'react';
import { useParams, useLoaderData, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import api from "../api";

const EditProfilePage = ({ updateProfileSubmit }) => {
    const [profiles, setProfiles] = useState([]);
 
const [name, setName] = useState('');
const [email, setEmail] = useState('');
const [bio, setBio] = useState('');

  const navigate = useNavigate();
//   const { id } = useParams();
const id = profiles.id;

  const submitForm = (e) => {
    e.preventDefault();

    const updatedProfile = {
      id,
      name, 
      email , 
      bio, 
 
    };

    updateProfileSubmit(updatedProfile);

    toast.success('Pefile Updated Successfully');

    // return navigate(`/jobs/${id}`);
    return navigate(`/profiles/open`);
  };

  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProfiles = async () => {
    //   const apiUrl = isHome ? '/api/profile' : '/api/profiles'; // isn=
      const apiUrl =  '/api/profile' ; // sn=

      try {
 
        const getNotes = () => {
                api
                    .get("/api/profile/")
                    .then((res) => res.data)
                    .then((data) => {
                        setProfiles(data);
                        console.log(data);

 

      setName(data.name || '');
      setEmail(data.email || '');
      setBio(data.bio || '');
                    })
                    .catch((err) => alert(err));
            };
 
        getNotes()

      } catch (error) {
        console.log('Error fetching data', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProfiles();
  }, []);

  return (
    <section style={sectionStyle}>
      <div style={containerStyle}>
        <div style={formCardStyle}>
          <form onSubmit={submitForm}>
            <h2 style={formTitleStyle}>
              Update Profile
            </h2>


            <div style={formGroupStyle}>
              <label style={formLabelStyle}>
                Profile Name
              </label>
              <input
                type='text'
                id='name'
                name='name'
                style={formInputStyle}
                placeholder='eg. Beautiful Apartment In Miami'
                required
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </div>

            <div style={formGroupStyle}>
              <label style={formLabelStyle}>
                Profile Email
              </label>
              <input
                type='email'
                id='email'
                name='email'
                style={formInputStyle}
                placeholder='eg. Beautiful Apartment In Miami'
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </div>

            <div style={formGroupStyle}>
              <label style={formLabelStyle}>
                Profile Bio
              </label>
              <input
                type='text'
                id='bio'
                name='bio'
                style={formInputStyle}
                placeholder='eg. Beautiful Apartment In Miami'
                required
                value={bio}
                onChange={(e) => setBio(e.target.value)}
              />
            </div>


            <div>
              <button
                style={formButtonStyle}
                type='submit'
              >
                Update Profile
              </button>
            </div>
          </form>
        </div>
      </div>
    </section>

    
  );
};



const sectionStyle = {
    backgroundColor: '#e0f2f7', 
  };
  
  const containerStyle = {
    marginLeft: 'auto',
    marginRight: 'auto',
    maxWidth: '44rem', 
    paddingTop: '6rem', 
    paddingBottom: '6rem', 
  };
  
  const formCardStyle = {
    backgroundColor: '#ffffff', 
    paddingLeft: '1.5rem', 
    paddingRight: '1.5rem', 
    paddingTop: '2rem', 
    paddingBottom: '2rem', 
    marginBottom: '1rem', 
    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
    borderRadius: '0.375rem', 
    borderWidth: '1px', 
    marginLeft: '1rem', 
    marginRight: '1rem', 
  };
  
  const formTitleStyle = {
    fontSize: '1.875rem', 
    textAlign: 'center', 
    fontWeight: 600, 
    marginBottom: '1.5rem', 
  };
  
  const formGroupStyle = {
    marginBottom: '1rem', 
  };
  
  const formLabelStyle = {
    display: 'block', 
    color: '#4a5568', 
    fontWeight: 700, 
    marginBottom: '0.5rem', 
  };
  
  const formInputStyle = {
    borderWidth: '1px', 
    borderRadius: '0.25rem', 
    width: '100%', 
    paddingTop: '0.5rem', 
    paddingBottom: '0.5rem', 
    paddingLeft: '0.75rem', 
    paddingRight: '0.75rem', 
    marginBottom: '0.5rem', 
  };
  
  const formButtonStyle = {
    backgroundColor: '#667eea', 
    color: '#ffffff', 
    fontWeight: 700, 
    paddingTop: '0.5rem', 
    paddingBottom: '0.5rem', 
    paddingLeft: '1rem', 
    paddingRight: '1rem', 
    borderRadius: '9999px', 
    width: '100%', 
    outline: '2px solid transparent', 
    outlineOffset: '2px', 
    boxShadow: '0 0 0 0 rgba(0, 0, 0, 0)', 
    transition: 'background-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out',
    cursor: 'pointer',
    border: 'none',
  };
  
  formButtonStyle[':hover'] = {
    backgroundColor: '#5a67d8', // Equivalent to hover:bg-indigo-600
  };
  
  formButtonStyle[':focus'] = {
    boxShadow: '0 0 0 3px rgba(102, 126, 234, 0.5)', // Basic focus outline
  };

export default EditProfilePage;


