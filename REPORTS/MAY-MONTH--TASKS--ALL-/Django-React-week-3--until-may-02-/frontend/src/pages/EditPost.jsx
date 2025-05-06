// D:\GROW_CTS\Django-React-Full-Stack-App-main\frontend\src\pages\EditPost.jsx
import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";

import api from "../api";


function EditPost() {
    const { id } = useParams();
    const [title, setTitle] = useState("");
    const [content, setContent] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        api.get(`/api/blog/posts/${id}/`)
            .then((res) => {
                setTitle(res.data.title);
                setContent(res.data.content);
            })
            .catch((err) => alert("Error loading post."));
    }, [id]);

    const handleUpdate = (e) => {
        e.preventDefault();
        api.put(`/api/blog/posts/${id}/`, { title, content })
            .then(() => {
                alert("Post updated!");
                navigate(`/posts/${id}`);
            })
            .catch((err) => alert("Failed to update."));
    };

    return (
        <div>
            <h2>Edit Post</h2>
            <form onSubmit={handleUpdate}>
                <label htmlFor="title">Title:</label><br />
                <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                /><br />
                <label htmlFor="content">Content:</label><br />
                <textarea
                    id="content"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    required
                ></textarea><br />
                <button type="submit">Update</button>
            </form>
        </div>
    );
}

export default EditPost;
