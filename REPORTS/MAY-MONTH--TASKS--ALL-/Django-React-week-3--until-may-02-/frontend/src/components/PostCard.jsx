
import { Link } from "react-router-dom";

function PostCard({ post, onDelete }) {

    return (
        <div className="post-container">
            <h3>{post.title}</h3>
            <p>{post.content.substring(0, 100)}...</p>

            {/* changed for all posts  and searchFilter.jsx----- post.author */}
            <p><strong>Author:</strong> {post.author.name}</p>
            
            {/* changed for searchFilter.jsx */}
            {/* <p><strong>Author:</strong> {post.author}</p> */}

            {/* <p className="post-date">{formattedDate}</p> */}
            <Link to={`/posts/${post.id}`}>Read More</Link>
            <button onClick={() => onDelete(post.id)}>Delete</button>
        </div>
    );
}

export default PostCard;
