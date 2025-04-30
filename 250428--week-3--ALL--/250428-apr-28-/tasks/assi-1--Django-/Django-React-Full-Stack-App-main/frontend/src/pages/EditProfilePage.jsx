





// ========================================================================
// ========================================================================
// ========================================================================
// ========================================================================


// EditProfilePage

import { useState, useEffect } from 'react';
import { useParams, useLoaderData, useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import api from "../api";

const EditProfilePage = ({ updateProfileSubmit }) => {
    const [profiles, setProfiles] = useState([]);

  
//   const [name, setName] = useState([profiles.name]);
//   const [email, setEmail] = useState([profiles.email]);
//   const [bio, setBio] = useState([profiles.bio]);

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
      name, // title,
      email , // type,
      bio, //location,
    //   description,
    //   salary,
    //   company: {
    //     name: companyName,
    //     description: companyDescription,
    //     contactEmail,
    //     contactPhone,
    //   },
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
        // const res = await fetch(apiUrl);
        // const data = await res.json();
        // setProfiles(data);

        // --------------------------
        const getNotes = () => {
                api
                    .get("/api/profile/")
                    .then((res) => res.data)
                    .then((data) => {
                        setProfiles(data);
                        console.log(data);

                        // D:\GROW_CTS\PANKAJ-PROJECTS-\250428--week-3--ALL--\250428-apr-28-\tasks\assi-1--Django-\Django-React-Full-Stack-App-main\frontend\src\pages\EditProfilePage.jsx
                        // D:\GROW_CTS\PANKAJ-PROJECTS-\250428--week-3--ALL--\250428-apr-28-\tasks\assi-1--Django-\Django-React-Full-Stack-App-main\backend\api\views.py

                        
                        // output in console of browser (json)--- data from django backend

                          // EditProfilePage.jsx:81 
                          // {id: 3, uuid: '158fdefd-c305-42c2-819e-4cfdc3298287', name: 'pratham Bhuje999l', bio: 'Pratham is clas999s 11 student studing computer sc…in playing football.He is excellent in his study.', email: 'pratham@gmail.com'}
                          // bio
                          // : 
                          // "Pratham is clas999s 11 student studing computer science.He is also good in playing football.He is excellent in his study."
                          // email
                          // : 
                          // "pratham@gmail.com"
                          // id
                          // : 
                          // 3
                          // name
                          // : 
                          // "pratham Bhuje999l"
                          // uuid
                          // : 
                          // "158fdefd-c305-42c2-819e-4cfdc3298287"
                          

                        // Set form fields after profile is fetched
      setName(data.name || '');
      setEmail(data.email || '');
      setBio(data.bio || '');
                    })
                    .catch((err) => alert(err));
            };
        // --------------------------

        // const getNotes = () => {
        //     api
        //         .get("/api/notes/")
        //         .then((res) => res.data)
        //         .then((data) => {
        //             setNotes(data);
        //             console.log(data);
        //         })
        //         .catch((err) => alert(err));
        // };
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
    backgroundColor: '#e0f2f7', // Equivalent to bg-indigo-50
  };
  
  const containerStyle = {
    marginLeft: 'auto',
    marginRight: 'auto',
    maxWidth: '44rem', // Equivalent to max-w-2xl (32rem) + some extra for padding if needed
    paddingTop: '6rem', // Equivalent to py-24 / 2
    paddingBottom: '6rem', // Equivalent to py-24 / 2
  };
  
  const formCardStyle = {
    backgroundColor: '#ffffff', // Equivalent to bg-white
    paddingLeft: '1.5rem', // Equivalent to px-6
    paddingRight: '1.5rem', // Equivalent to px-6
    paddingTop: '2rem', // Equivalent to py-8
    paddingBottom: '2rem', // Equivalent to py-8
    marginBottom: '1rem', // Equivalent to mb-4
    boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)', // Equivalent to shadow-md
    borderRadius: '0.375rem', // Equivalent to rounded-md
    borderWidth: '1px', // Equivalent to border
    marginLeft: '1rem', // Equivalent to m-4
    marginRight: '1rem', // Equivalent to m-4
  };
  
  const formTitleStyle = {
    fontSize: '1.875rem', // Equivalent to text-3xl
    textAlign: 'center', // Equivalent to text-center
    fontWeight: 600, // Equivalent to font-semibold
    marginBottom: '1.5rem', // Equivalent to mb-6
  };
  
  const formGroupStyle = {
    marginBottom: '1rem', // Equivalent to mb-4
  };
  
  const formLabelStyle = {
    display: 'block', // Equivalent to block
    color: '#4a5568', // Equivalent to text-gray-700
    fontWeight: 700, // Equivalent to font-bold
    marginBottom: '0.5rem', // Equivalent to mb-2
  };
  
  const formInputStyle = {
    borderWidth: '1px', // Equivalent to border
    borderRadius: '0.25rem', // Equivalent to rounded
    width: '100%', // Equivalent to w-full
    paddingTop: '0.5rem', // Equivalent to py-2
    paddingBottom: '0.5rem', // Equivalent to py-2
    paddingLeft: '0.75rem', // Equivalent to px-3
    paddingRight: '0.75rem', // Equivalent to px-3
    marginBottom: '0.5rem', // Equivalent to mb-2
  };
  
  const formButtonStyle = {
    backgroundColor: '#667eea', // Equivalent to bg-indigo-500
    color: '#ffffff', // Equivalent to text-white
    fontWeight: 700, // Equivalent to font-bold
    paddingTop: '0.5rem', // Equivalent to py-2
    paddingBottom: '0.5rem', // Equivalent to py-2
    paddingLeft: '1rem', // Equivalent to px-4
    paddingRight: '1rem', // Equivalent to px-4
    borderRadius: '9999px', // Equivalent to rounded-full
    width: '100%', // Equivalent to w-full
    outline: '2px solid transparent', // Equivalent to focus:outline-none
    outlineOffset: '2px', // For better focus ring
    boxShadow: '0 0 0 0 rgba(0, 0, 0, 0)', // Equivalent to focus:shadow-outline (remove default browser focus)
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



// ========================================================================
// ========================================================================
// ========================================================================
// ========================================================================



// // EditProfilePage

// import { useState } from 'react';
// import { useParams, useLoaderData, useNavigate } from 'react-router-dom';
// import { toast } from 'react-toastify';

// const EditJobPage = ({ updateProfileSubmit }) => {
//     const [profiles, setProfiles] = useState([]);

  
//   const [name, setName] = useState(profiles.name);
//   const [email, setEmail] = useState(profiles.email);
//   const [bio, setBio] = useState(profiles.bio);
//   const navigate = useNavigate();
//   const { id } = useParams();

//   const submitForm = (e) => {
//     e.preventDefault();

//     const updatedJob = {
//       id,
//       name, // title,
//       email , // type,
//       bio, //location,
//     //   description,
//     //   salary,
//     //   company: {
//     //     name: companyName,
//     //     description: companyDescription,
//     //     contactEmail,
//     //     contactPhone,
//     //   },
//     };

//     updateProfileSubmit(updatedJob);

//     toast.success('Pefile Updated Successfully');

//     // return navigate(`/jobs/${id}`);
//     return navigate(`/profiles/open`);
//   };

//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     const fetchProfiles = async () => {
//     //   const apiUrl = isHome ? '/api/profile' : '/api/profiles'; // isn=
//       const apiUrl =  '/api/profile' ; // sn=

//       try {
//         // const res = await fetch(apiUrl);
//         // const data = await res.json();
//         // setProfiles(data);

//         // --------------------------
//         const getNotes = () => {
//                 api
//                     .get("/api/profile/")
//                     .then((res) => res.data)
//                     .then((data) => {
//                         setProfiles(data);
//                         console.log(data);
//                     })
//                     .catch((err) => alert(err));
//             };
//         // --------------------------

//         // const getNotes = () => {
//         //     api
//         //         .get("/api/notes/")
//         //         .then((res) => res.data)
//         //         .then((data) => {
//         //             setNotes(data);
//         //             console.log(data);
//         //         })
//         //         .catch((err) => alert(err));
//         // };
//         getNotes()

//       } catch (error) {
//         console.log('Error fetching data', error);
//       } finally {
//         setLoading(false);
//       }
//     };

//     fetchProfiles();
//   }, []);

//   return (
//     <section className='bg-indigo-50'>
//       <div className='container m-auto max-w-2xl py-24'>
//         <div className='bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0'>
//           <form onSubmit={submitForm}>
//             <h2 className='text-3xl text-center font-semibold mb-6'>
//               Update Profile
//             </h2>

//             {/* <div className='mb-4'>
//               <label
//                 htmlFor='name'
//                 className='block text-gray-700 font-bold mb-2'
//               >
//                 Profile email
//               </label>
//               <select
//                 id='name'
//                 name='name'
//                 className='border rounded w-full py-2 px-3'
//                 required
//                 value={name}
//                 onChange={(e) => setName(e.target.value)}
//               >
//                 <option value='Full-Time'>Full-Time</option>
//                 <option value='Part-Time'>Part-Time</option>
//                 <option value='Remote'>Remote</option>
//                 <option value='Internship'>Internship</option>
//               </select>
//             </div> */}

//             <div className='mb-4'>
//               <label className='block text-gray-700 font-bold mb-2'>
//                 Profile Listing Name  ... title
//               </label>
//               <input
//                 type='text'
//                 id='name'
//                 name='name'
//                 className='border rounded w-full py-2 px-3 mb-2'
//                 placeholder='eg. Beautiful Apartment In Miami'
//                 required
//                 value={name}
//                 onChange={(e) => setName(e.target.value)}
//               />
//             </div>

//             <div className='mb-4'>
//               <label className='block text-gray-700 font-bold mb-2'>
//                 Profile Listing Email  ... title
//               </label>
//               <input
//                 type='email'
//                 id='email'
//                 name='email'
//                 className='border rounded w-full py-2 px-3 mb-2'
//                 placeholder='eg. Beautiful Apartment In Miami'
//                 required
//                 value={email}
//                 onChange={(e) => setEmail(e.target.value)}
//               />
//             </div>

//             <div className='mb-4'>
//               <label className='block text-gray-700 font-bold mb-2'>
//                 Profile Listing Bio  ... title
//               </label>
//               <input
//                 type='text'
//                 id='bio'
//                 name='bio'
//                 className='border rounded w-full py-2 px-3 mb-2'
//                 placeholder='eg. Beautiful Apartment In Miami'
//                 required
//                 value={bio}
//                 onChange={(e) => setBio(e.target.value)}
//               />
//             </div>
// {/* 
//             <div className='mb-4'>
//               <label
//                 htmlFor='description'
//                 className='block text-gray-700 font-bold mb-2'
//               >
//                 Description
//               </label>
//               <textarea
//                 id='description'
//                 name='description'
//                 className='border rounded w-full py-2 px-3'
//                 rows='4'
//                 placeholder='Add any job duties, expectations, requirements, etc'
//                 value={description}
//                 onChange={(e) => setDescription(e.target.value)}
//               ></textarea>
//             </div>

//             <div className='mb-4'>
//               <label
//                 htmlFor='type'
//                 className='block text-gray-700 font-bold mb-2'
//               >
//                 Salary
//               </label>
//               <select
//                 id='salary'
//                 name='salary'
//                 className='border rounded w-full py-2 px-3'
//                 required
//                 value={salary}
//                 onChange={(e) => setSalary(e.target.value)}
//               >
//                 <option value='Under $50K'>Under $50K</option>
//                 <option value='$50K - 60K'>$50K - $60K</option>
//                 <option value='$60K - 70K'>$60K - $70K</option>
//                 <option value='$70K - 80K'>$70K - $80K</option>
//                 <option value='$80K - 90K'>$80K - $90K</option>
//                 <option value='$90K - 100K'>$90K - $100K</option>
//                 <option value='$100K - 125K'>$100K - $125K</option>
//                 <option value='$125K - 150K'>$125K - $150K</option>
//                 <option value='$150K - 175K'>$150K - $175K</option>
//                 <option value='$175K - 200K'>$175K - $200K</option>
//                 <option value='Over $200K'>Over $200K</option>
//               </select>
//             </div>

//             <div className='mb-4'>
//               <label className='block text-gray-700 font-bold mb-2'>
//                 Location
//               </label>
//               <input
//                 type='text'
//                 id='location'
//                 name='location'
//                 className='border rounded w-full py-2 px-3 mb-2'
//                 placeholder='Company Location'
//                 required
//                 value={location}
//                 onChange={(e) => setLocation(e.target.value)}
//               />
//             </div>

//             <h3 className='text-2xl mb-5'>Company Info</h3>

//             <div className='mb-4'>
//               <label
//                 htmlFor='company'
//                 className='block text-gray-700 font-bold mb-2'
//               >
//                 Company Name
//               </label>
//               <input
//                 type='text'
//                 id='company'
//                 name='company'
//                 className='border rounded w-full py-2 px-3'
//                 placeholder='Company Name'
//                 value={companyName}
//                 onChange={(e) => setCompanyName(e.target.value)}
//               />
//             </div>

//             <div className='mb-4'>
//               <label
//                 htmlFor='company_description'
//                 className='block text-gray-700 font-bold mb-2'
//               >
//                 Company Description
//               </label>
//               <textarea
//                 id='company_description'
//                 name='company_description'
//                 className='border rounded w-full py-2 px-3'
//                 rows='4'
//                 placeholder='What does your company do?'
//                 value={companyDescription}
//                 onChange={(e) => setCompanyDescription(e.target.value)}
//               ></textarea>
//             </div>

//             <div className='mb-4'>
//               <label
//                 htmlFor='contact_email'
//                 className='block text-gray-700 font-bold mb-2'
//               >
//                 Contact Email
//               </label>
//               <input
//                 type='email'
//                 id='contact_email'
//                 name='contact_email'
//                 className='border rounded w-full py-2 px-3'
//                 placeholder='Email address for applicants'
//                 required
//                 value={contactEmail}
//                 onChange={(e) => setContactEmail(e.target.value)}
//               />
//             </div>
//             <div className='mb-4'>
//               <label
//                 htmlFor='contact_phone'
//                 className='block text-gray-700 font-bold mb-2'
//               >
//                 Contact Phone
//               </label>
//               <input
//                 type='tel'
//                 id='contact_phone'
//                 name='contact_phone'
//                 className='border rounded w-full py-2 px-3'
//                 placeholder='Optional phone for applicants'
//                 value={contactPhone}
//                 onChange={(e) => setContactPhone(e.target.value)}
//               />
//             </div> */}

//             <div>
//               <button
//                 className='bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline'
//                 type='submit'
//               >
//                 Update Profile
//               </button>
//             </div>
//           </form>
//         </div>
//       </div>
//     </section>
//   );
// };
// export default EditJobPage;
