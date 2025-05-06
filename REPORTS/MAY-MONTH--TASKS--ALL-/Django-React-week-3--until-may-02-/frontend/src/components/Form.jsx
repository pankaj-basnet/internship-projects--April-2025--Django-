import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css"
import LoadingIndicator from "./LoadingIndicator";

function Form({ route, method }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const name = method === "login" ? "Login" : "Register";

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();

        try {
            const res = await api.post(route, { email, password })
            if (method === "login") {
                localStorage.setItem(ACCESS_TOKEN, res.data.access); // isn= 
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh); // isn=
                // localStorage.setItem(ACCESS_TOKEN, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1ODQxNDU3LCJpYXQiOjE3NDU4Mzk2NTcsImp0aSI6ImI5ZmY0OWE5ZmEwOTQzNDhhNzU4NGViYjhiNGRlNTMyIiwidXNlcl9pZCI6NH0.3geNxKszucaVGnDMawDcOuyqz86kiDK5wUKBQ4AGlYs" ); // sn= 
                // localStorage.setItem(REFRESH_TOKEN, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTkyNjA1NywiaWF0IjoxNzQ1ODM5NjU3LCJqdGkiOiJiNzI4OTU4NjU4OTg0M2Y2OWRlODM0ZTNiZjQ2ZjdkOCIsInVzZXJfaWQiOjR9.VD1Ap9JtFUa16lgf6xsMHnqkffTTuo0JJZmnnZ1iUFc"); // sn=
                navigate("/")
            } else {
                navigate("/login")
            }
        } catch (error) {
            alert(error)
        } finally {
            setLoading(false)
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{name}</h1>
            <input
                className="form-input"
                type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="email"
            />
            <input
                className="form-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
            />
            {loading && <LoadingIndicator />}
            <button className="form-button" type="submit">
                {name}
            </button>
        </form>
    );
}

export default Form