
// D:\GROW_CTS\Django-React-Full-Stack-App-main\frontend\src\pages\SearchFilter.jsx


import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import api from "../api";
import '../styles/SinglePost.css'; // Import your CSS file

import PostCard from '../components/PostCard';

const SearchFilter = () =>  {
  const [tags, setTags] = useState([]);
  const [search, setSearch] = useState("");
  const [tag, setTag] = useState("");

  // separately done for tags search
  const getTags = () => {
      let url = `/api/blog/posts/tag/?`;

      // if (search) url += `tags__name=${search}`;

      // for tags
      if (tag) url += `tags__name=${tag}`;

      // if (search) url += `search=${search}&`;
      // if (tag) url += `tags__name=${tag}&`;

      api.get(url)
          .then((res) => setTags(res.data.results))
          .catch((err) => alert(err));
  };
 

  const deletePost = async (id) => {
    await api.delete(`/api/blog/posts/${id}/`)
        .then((res) => {
            if (res.status === 204) alert("Post deleted!");
            getPosts();
        })
        .catch((err) => alert("Delete failed: " + err));
};


  useEffect(() => {
      // getPosts();
      getTags();
  // }, [search, tag]);
  }, [ tag]);

  return (
      <div>
          <h2>Posts</h2>

          <input
              type="text"
              placeholder="Search by title or content"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
          />
          <input
              type="text"
              placeholder="Filter by tag name"
              value={tag}
              onChange={(e) => setTag(e.target.value)}
          />

          <div>
            {/* for search posts only */}
              {/* {posts.map((post) => ( */}

              {/* // for tags */}
              {tags.map((post) => (
      
                  <PostCard post={post} onDelete={deletePost} key={post.id} />
              ))}
          </div>
      </div>
  );
}
;

export default SearchFilter;


