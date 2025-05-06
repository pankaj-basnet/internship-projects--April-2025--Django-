
import { useState, useEffect } from 'react';
import SingleProfilePage from '../components/ProfileListing';
import Spinner from '../components/Spinner';

import api from "../api";


// const ProfileListings = ({ isHome = false }) => {
const ProfilePageOpen = ({  }) => {
  const [profiles, setProfiles] = useState([]);
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
             
          </div>
        )}
      </div>
    </section>
  );
};

export default ProfilePageOpen;

