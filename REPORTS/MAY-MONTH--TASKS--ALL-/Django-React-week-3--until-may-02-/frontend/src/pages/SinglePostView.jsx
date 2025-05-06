// D:\GROW_CTS\Django-React-Full-Stack-App-main\frontend\src\pages\SinglePostView.jsx

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';
import api from "../api";
import '../styles/SinglePost.css'; // Import your CSS file

const SinglePost = () => {
  const { id } = useParams(); // UUID of the post
  const navigate = useNavigate();

  const [post, setPost] = useState(null);
  const [likeCount, setLikeCount] = useState(100);
  const [userHasLiked, setUserHasLiked] = useState(false);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState('');

 
  const fetchPost = async () => {
 


    await api.get(`/api/blog/posts/${id}/`)
      .then((res) => {
        console.log(" -----  await api.get(`/api/blog/posts/ ----- ")
        setPost(res.data);
      })
      .catch((err) => alert("Error getting single post."));

  };

  const fetchLikes = async () => {
     const countRes = await api.get(`/api/blog/posts/${id}/likes/count/`);
    setLikeCount(countRes.data.like_count);
 
  };

  const fetchComments = async () => {
 
    const res = await api.get(`/api/blog/comments/?post=${id}`);
    setComments(res.data);

  };

  useEffect(() => {
    fetchPost();
    fetchLikes();
    fetchComments();
  }, []);

 

  const handleLikeToggle = async () => {
    await api.post('/api/blog/likes/', { post: id });
    fetchLikes();
  };

  const handleDelete = async () => {
    await api.delete(`/api/blog/posts/${id}/`);
    navigate('/');
  };

  const handleAddComment = async () => {
    // await api.post('/api/blog/comments/', { post: id, content: newComment });
    await api.post('/api/blog/comments/', { post: id, sentences: newComment });
    setNewComment('');
    fetchComments();
  };

  if (!post) return <p>Loading...</p>;

  return (
    <div className="p-4">
      <h2 className="post-title">Title of the post : {post.title}</h2>
      {/* <p className="post-content1">Post Created By :</p> */}

      <p className="post-author"> <span> {post.author?.username}</span></p>
      <h3 className="post-content1">CONTENT :</h3>
      <p className="post-content">{post.content}</p>

      <p>Status: <strong>{post.status}</strong></p>

      <button onClick={handleLikeToggle}>
        {userHasLiked ? '❤️ Unlike' : '🤍 Like'} ({likeCount})
      </button>

      {post.status === 'published' && (
        <div className="mt-6">
          <h3 className="text-xl font-semibold">Comments</h3>
          {comments.map(c => (
            <div key={c.id} className="border-b py-2">
              {/* <p className="text-sm font-semibold">{c.user_name}</p> */}
              <p>{c.sentences}</p>
            </div>
          ))}
           

          <div className="comment-form">
              <textarea
                value={newComment}
                onChange={e => setNewComment(e.target.value)}
                placeholder="Add a comment..."
                className="w-full p-2 border"
              />
              <button onClick={handleAddComment}  className="submit-comment-button">Post Comment</button>
            </div>
        </div>
      )}
    </div>
  );
};

export default SinglePost;
