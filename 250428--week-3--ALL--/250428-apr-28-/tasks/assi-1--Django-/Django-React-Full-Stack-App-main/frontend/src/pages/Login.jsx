import Form from "../components/Form"

function Login() {
    return <Form route="/api/token/" method="login" /> // isn=
    // return <Form route="localhost:8000/api/token/" method="login" /> // sn=
    // return <Form route="http://127.0.0.1:8000/api/token" method="login" /> // sn=
}

export default Login