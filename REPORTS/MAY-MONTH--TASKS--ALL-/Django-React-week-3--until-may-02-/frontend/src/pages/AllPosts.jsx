import { useEffect, useState } from "react";
import api from "../api";
import PostCard from "../components/PostCard";

function AllPosts() {
    const [posts, setPosts] = useState([]);

    useEffect(() => {
        fetchPosts();
    }, []);

    const fetchPosts = async () => {
        await api.get("/api/blog/posts/")
            .then((res) => {
                console.log("----------------------")
                console.log(res.data)
                setPosts(res.data);
            })
            .catch((err) => alert("Error fetching posts: " + err));
    };

 
    const deletePost = async (id) => {
        await api.delete(`/api/blog/posts/${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Post deleted!");
                fetchPosts();
            })
            .catch((err) => alert("Delete failed: " + err));
    };

    return (
        <div>
            <h2>All Posts</h2>
            {posts.map((post) => (
                // <PostCard post={post} onDelete={deletePost} key={post.id} />
                <PostCard post={post} onDelete={deletePost} key={post.id} />
            ))}
        </div>
    );
}

export default AllPosts;
