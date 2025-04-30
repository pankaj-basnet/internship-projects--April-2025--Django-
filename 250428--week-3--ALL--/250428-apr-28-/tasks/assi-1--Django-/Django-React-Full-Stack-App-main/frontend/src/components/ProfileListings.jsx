import { useState, useEffect } from 'react';
import SingleProfilePage from './ProfileListing';
import Spinner from './Spinner';

import api from "../api";


// const ProfileListings = ({ isHome = false }) => {
const ProfileListings = ({  }) => {
  const [profiles, setProfiles] = useState([]);
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

                        // output in console of browser (json)
                        // http://localhost:5173/profiles

                          //                         
                          // ProfileListings.jsx:30 
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
    <section className='bg-blue-50 px-4 py-10'>
      <div className='container-xl lg:container m-auto'>
        <h2 className='text-3xl font-bold text-indigo-500 mb-6 text-center'>
          {/* {isHome ? 'Recent Profiles sn=' : 'Browse Profiles sn='} */}
        </h2>

        {loading ? (
          <Spinner loading={loading} />
        ) : (
          <div className='grid grid-cols-1 md:grid-cols-3 gap-6'>
            <SingleProfilePage key= {3} profile={profiles}/>
            {/* {profiles.map((profile) => (
              <SingleProfilePage key={profile.id} profile={profile} />
            ))} */}
          </div>
        )}
      </div>
    </section>
  );
};

export default ProfileListings;
