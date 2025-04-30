import { useParams, useLoaderData, useNavigate } from 'react-router-dom';
import { FaArrowLeft, FaMapMarker } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import { toast } from 'react-toastify';

const ProfilePageOpen = ({ deleteProfile }) => {
  const navigate = useNavigate();
  const { id } = useParams();
  const profile = useLoaderData();

  const onDeleteClick = (profileId) => {
    const confirm = window.confirm(
      'Are you sure you want to delete this listing?'
    );

    if (!confirm) return;

    deleteProfile(profileId);

    toast.success('Profile deleted successfully');

    navigate('/profiles');
  };

  return (
    <>
      <section>
        <div className='container m-auto py-6 px-6'>
          <Link
            to='/profiles'
            className='text-indigo-500 hover:text-indigo-600 flex items-center'
          >
            <FaArrowLeft className='mr-2' /> Back to Profile Main
          </Link>
        </div>
      </section>

      <section className='bg-indigo-50'>
        <div className='container m-auto py-10 px-6'>
          <div className='grid grid-cols-1 md:grid-cols-70/30 w-full gap-6'>
            <main>
              <div className='bg-white p-6 rounded-lg shadow-md text-center md:text-left'>
                <div className='text-gray-500 mb-4'>{profile.id}</div>
                <h1 className='text-3xl font-bold mb-4'>{profile.uuid}</h1>
                <div className='text-gray-500 mb-4 flex align-middle justify-center md:justify-start'>
                  <FaMapMarker className='text-orange-700 mr-1' />
                  <p className='text-orange-700'>{profile.location}</p>
                </div>
              </div>

              <div className='bg-white p-6 rounded-lg shadow-md mt-6'>
                <h3 className='text-indigo-800 text-lg font-bold mb-6'>
                  Profile Description
                </h3>

                <p className='mb-4'>{profile.bio}</p>

                <h3 className='text-indigo-800 text-lg font-bold mb-2'>
                  Last Login ...
                </h3>

                {/* <p className='mb-4'>{job.salary} / Year</p> */}
              </div>
            </main>

            {/* <!-- Sidebar --> */}
            <aside>
              <div className='bg-white p-6 rounded-lg shadow-md'>
                <h3 className='text-xl font-bold mb-6'>Profile Info</h3>

                {/* <h2 className='text-2xl'>{job.company.name}</h2> */}

                {/* <p className='my-2'>{job.company.description}</p> */}

                <hr className='my-4' />

                {/* <h3 className='text-xl'>Contact Email:</h3> */}

                <p className='my-2 bg-indigo-100 p-2 font-bold'>
                  {/* {job.company.contactEmail} */}
                </p>

                {/* <h3 className='text-xl'>Contact Phone:</h3> */}

                <p className='my-2 bg-indigo-100 p-2 font-bold'>
                  {' '}
                  {/* {job.company.contactPhone} */}
                </p>
              </div>

              <div className='bg-white p-6 rounded-lg shadow-md mt-6'>
                <h3 className='text-xl font-bold mb-6'>Manage Profile</h3>
                <Link
                  to={`/edit-job/${profile.id}`}
                  className='bg-indigo-500 hover:bg-indigo-600 text-white text-center font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline mt-4 block'
                >
                  Edit Job
                </Link>
                <button
                  onClick={() => onDeleteClick(profile.id)}
                  className='bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline mt-4 block'
                >
                  Delete Profile
                </button>
              </div>
            </aside>
          </div>
        </div>
      </section>
    </>
  );
};

// const jobLoader = async ({ params }) => {
// //   const res = await fetch(`/api/jobs/${params.id}`);
// console.log("-------- ProfilePageOpen.jsx ----- --- ---");
//   const res = await fetch(`/api/profile`);
//   const data = await res.json();
// // const 
//   console.log("-------- ProfilePageOpen.jsx ----- --- ---");
//   console.log(data);
//   return data;
// };

export { ProfilePageOpen as default, jobLoader };
