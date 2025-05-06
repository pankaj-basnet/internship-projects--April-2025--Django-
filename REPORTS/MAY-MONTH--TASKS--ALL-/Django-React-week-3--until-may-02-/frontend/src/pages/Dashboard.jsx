


import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import api from "../api";

import "../styles/dashboard.css";

function Dashboard() {
    const [postCount, setPostCount] = useState(0);
    const [commentCount, setCommentCount] = useState(0);
    const [recentDrafts, setRecentDrafts] = useState([]);
    const [createPostUrl, setCreatePostUrl] = useState("");

    const getAuthorDashboard = async () => {
        await api.get("/api/blog/author/dashboard/")
            .then((res) => {
                console.log(res.data)

                setPostCount(res.data.post_count);
                setCommentCount(res.data.comment_count);
                setRecentDrafts(res.data.recent_unpublished_posts);
                setCreatePostUrl(res.data.create_post_url);
            })
            .catch((err) => alert("Failed to load dashboard data"));
    }

    const deletePost = async (id) => {
        await api.delete(`/api/blog/posts/${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Post deleted!");
                getAuthorDashboard();
            })
            .catch((err) => alert("Delete failed: " + err));
    };

    // useEffect(async () => { # error sn=
    //      getAuthorDashboard()
    // }, []);

    useEffect(() => {
        const fetchData = async () => {
            await getAuthorDashboard();
        };
        fetchData();
    }, []);

    return (
        <div>
            <h2>Author Dashboard</h2>
            <p>Total Posts: {postCount}</p>
            <p>Total Comments: {commentCount}</p>

            <div >
                <p> <Link to={`${createPostUrl}`}>Create a new post</Link></p>

            </div>

            <h3>Recent Drafts</h3>
 

            {Array.isArray(recentDrafts) && recentDrafts.map((post) => (
                <div
                    key={post.id || `${post.title}-${post.author}`}
                    className="post-card"
                >
                    <h3 className="post-title">{post.title}</h3>
                    <p className="post-author">
                        <strong>Author:</strong> {post.author}
                    </p>
                    <p className="post-content">{post.content}</p>
                </div>
            ))}

        </div>
    );
}

export default Dashboard;