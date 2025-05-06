import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from "../api";
import '../styles/SinglePost.css'; // Import your CSS file

const SinglePost = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [post, setPost] = useState(null);
  const [likeCount, setLikeCount] = useState(100);
  const [userHasLiked, setUserHasLiked] = useState(false);
  const [comments, setComments] = useState([]);
  const [newComment, setNewComment] = useState('');

  const fetchPost = async () => {
    try {
      const res = await api.get(`/api/blog/posts/${id}/`);
      console.log(res.data)
      setPost(res.data);
    } catch (err) {
      alert("Error getting single post.");
    }
  };

  const fetchLikes = async () => {
    const res = await api.get(`/api/blog/likes/`);
    setLikeCount(res.data.like_count);
  };

  const fetchComments = async () => {
    const res = await api.get(`/api/blog/comments/`);
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
    await api.post('/api/blog/comments/', { post: id, content: newComment });
    setNewComment('');
    fetchComments();
  };

  if (!post) return <p className="loading-text">Loading...</p>;

  return (
    <div className="post-container">
      <h2 className="post-title">Title of the post : {post.title}</h2>
      <p className="post-content1">Post Created By :</p>

      <p className="post-author"> <span> -- {post.author?.username}</span></p>
      <p className="post-content1">CONTENT :</p>
      <p className="post-content">{post.content}</p>

      <div className="post-meta">
        <span>Status: <strong>{post.status}</strong></span>
        <button onClick={handleLikeToggle} className={`like-button ${userHasLiked ? 'liked' : ''}`}>
          {userHasLiked ? '❤️ Unlike' : '🤍 Like'} ({likeCount})
        </button>
      </div>

 

      {post.status === 'published' && (
        <div className="comments-section">
          <h3 className="comments-title">Comments</h3>

          {comments.map((c) => (
            <div key={c.id} className="comment-card">
              <p>{c.sentences}</p>
            </div>
          ))}

 
        </div>
      )}
    </div>
  );
};

export default SinglePost;
