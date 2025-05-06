// D:\GROW_CTS\Django-React-Full-Stack-App-main\frontend\src\App.jsx

import react from "react"
// import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"

import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from 'react-router-dom';

import MainLayout from './layouts/MainLayout';

import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"

import ProfilePageOpen  from "./pages/ProfilePageOpen"

import api from "./api";

// import EditProfilePage from "./components/ProfilePage"
import ProfilesPage from "./components/ProfilesPage"
// import ProfilePage from "./components/ProfilePage"

import EditProfilePage from "./pages/EditProfilePage";

import SearchFilter  from "./pages/SearchFilter";

//
import AllPosts from "./pages/AllPosts";

// import SinglePost from "./pages/SinglePost-copy";
import SinglePost from "./pages/SinglePostView";

import EditPost from "./pages/EditPost";
import Dashboard from "./pages/Dashboard";


//

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {

   // Delete Job
   const deleteProfile = async (id) => {
    // const res = await fetch(`/api/jobs/${id}`, {
    //   method: 'DELETE',
    // });
    console.log("deleteProfile() in App()")
    return;
  };



  // Update Profile

  const updateProfile = async (profile) => {
    
    // const res = await api.post("api/user/3/update", { profile.name, profile.email, profile.bio })
    const res = await api.put(`api/user/${profile.id}/update/`, profile)
    console.log("updateProfile going on in App()")
    console.log("---------------------------")
    // console.log(profile)
    console.log(res)
    console.log("---------------------------")
    return;
  };

  

  // // Update Profile

  // const updateProfile = async (profile) => {
  //   // const res = await fetch(`/api/user/${profile.id}/update`, {
  //   //   method: 'PUT',
  //   //   headers: {
  //   //     'Content-Type': 'application/json',
  //   //   },
  //   //   body: JSON.stringify(profile),
  //   // });
  //   console.log("updateProfile going on in App()")
  //   console.log("---------------------------")
  //   console.log(profile)
  //   console.log("---------------------------")
  //   return;
  // };

  
  const router = createBrowserRouter(
    createRoutesFromElements(
      <Route path='/' element={<MainLayout />}>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
              {/* <Route path='/profiles' element={<ProfilesPage />} /> // sn= */}

            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />

        <Route path='/profiles' element={<ProfilesPage />} />
        {/* <Route
          path='/edit-profile/:id'
          element={<EditProfilePage updateProfileSubmit={updateJob} />}
          loader={jobLoader}

        /> */}
        <Route
          path='/edit-profile/:id'
          element={<EditProfilePage updateProfileSubmit={updateProfile} />}
          
        />
        <Route
          path='/profiles/open'
          element={<ProfilePageOpen deleteProfile={deleteProfile} />}
          // loader={jobLoader}
        />

        {/* Post Routes */}
      <Route path="/posts" element={<AllPosts />} />
      <Route path="/posts/:id" element={<SinglePost />} />
      <Route path="/posts/edit/:id" element={<EditPost />} />

      <Route path="/search/" element={<SearchFilter />} />

      <Route path="/dashboard/" element={<Dashboard />} />


      {/* Catch all */}

        <Route path="*" element={<NotFound />}></Route>
      </Route>
    )
  );

  return <RouterProvider router={router} />;

 
}

export default App


//  // ============= absolete ------ no needed below
//  return (






//   <BrowserRouter>
//     <Routes>
//       <Route
//         path="/"
//         element={
//           <ProtectedRoute>
//             <Home />
//             {/* <Route path='/profiles' element={<ProfilesPage />} /> // sn= */}

//           </ProtectedRoute>
//         }
//       />
//       <Route path="/login" element={<Login />} />
//       <Route path="/logout" element={<Logout />} />
//       <Route path="/register" element={<RegisterAndLogout />} />

//       <Route path='/profiles' element={<ProfilesPage />} />
//       {/* <Route
//         path='/edit-profile/:id'
//         element={<EditProfilePage updateProfileSubmit={updateJob} />}
//         loader={jobLoader}

//       /> */}
//       <Route
//         path='/profiles/:id'
//         element={<ProfilePage deleteProfile={deleteProfile} />}
//         loader={jobLoader}
//       />
//       <Route path="*" element={<NotFound />}></Route>
//     </Routes>
//   </BrowserRouter>
// )