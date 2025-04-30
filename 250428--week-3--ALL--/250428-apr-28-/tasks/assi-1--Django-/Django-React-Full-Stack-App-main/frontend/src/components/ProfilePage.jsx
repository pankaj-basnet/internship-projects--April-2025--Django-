// import { useState } from 'react';
// import { useLoaderData, useNavigate } from 'react-router-dom';
// import { toast } from 'react-toastify';

// const EditProfilePage = ({ updateProfileSubmit }) => {
//   const userData = useLoaderData(); // Load user data from backend
//   const [firstName, setFirstName] = useState(userData.first_name);
//   const [lastName, setLastName] = useState(userData.last_name);
//   const [email, setEmail] = useState(userData.email);

//   const navigate = useNavigate();

//   const submitForm = (e) => {
//     e.preventDefault();

//     const updatedProfile = {
//       first_name: firstName,
//       last_name: lastName,
//       email: email,
//     };

//     updateProfileSubmit(updatedProfile); // Function passed from props to handle backend update

//     toast.success('Profile Updated Successfully');

//     navigate('/profile'); // Redirect back to profile page
//   };

//   return (
//     <section className="bg-indigo-50">
//       <div className="container m-auto max-w-2xl py-24">
//         <div className="bg-white px-6 py-8 mb-4 shadow-md rounded-md border m-4 md:m-0">
//           <form onSubmit={submitForm}>
//             <h2 className="text-3xl text-center font-semibold mb-6">
//               Update Profile
//             </h2>

//             <div className="mb-4">
//               <label htmlFor="firstName" className="block text-gray-700 font-bold mb-2">
//                 First Name
//               </label>
//               <input
//                 type="text"
//                 id="firstName"
//                 name="firstName"
//                 className="border rounded w-full py-2 px-3"
//                 placeholder="First Name"
//                 value={firstName}
//                 onChange={(e) => setFirstName(e.target.value)}
//               />
//             </div>

//             <div className="mb-4">
//               <label htmlFor="lastName" className="block text-gray-700 font-bold mb-2">
//                 Last Name
//               </label>
//               <input
//                 type="text"
//                 id="lastName"
//                 name="lastName"
//                 className="border rounded w-full py-2 px-3"
//                 placeholder="Last Name"
//                 value={lastName}
//                 onChange={(e) => setLastName(e.target.value)}
//               />
//             </div>

//             <div className="mb-4">
//               <label htmlFor="email" className="block text-gray-700 font-bold mb-2">
//                 Email
//               </label>
//               <input
//                 type="email"
//                 id="email"
//                 name="email"
//                 className="border rounded w-full py-2 px-3"
//                 placeholder="Email Address"
//                 value={email}
//                 onChange={(e) => setEmail(e.target.value)}
//               />
//             </div>

//             <div>
//               <button
//                 className="bg-indigo-500 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-full w-full focus:outline-none focus:shadow-outline"
//                 type="submit"
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

// export default EditProfilePage;
