import { useEffect, useState } from "react";
import { login } from "../utils/auth";
import { useNavigate } from "react-router-dom";
import { useAuthStore } from "../store/auth";

import "./homepage.css";

const HomePage = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const isLoggedIn = useAuthStore((state) => state.isLoggedIn);

  useEffect(() => {
    if (!isLoggedIn()) {
      navigate("/login");
    }
  }, []);

  const resetForm = () => {
    setUsername("");
    setPassword("");
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    const { error } = await login(username, password);
    if (error) {
      alert(error);
    } else {
      navigate("/");
      resetForm();
    }
  };

  return (
    <div id="card">
      <div id="card-content">
        <div id="card-title">
          <h2>ACCESSO</h2>
          <div className="underline-title"></div>
        </div>
        <form onSubmit={handleLogin}>
          <label htmlFor="username" style={{ paddingTop: 13 }}>
            Nombre de usuario:
          </label>
          <input
            id="username"
            className="form-content"
            type="text"
            name="username"
            autoComplete="on"
            placeholder="Ingrese su nombre de usuario"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
          <div className="form-border"></div>
          <label htmlFor="password" style={{ paddingTop: 22 }}>
            Contraseña:
          </label>
          <input
            id="password"
            className="form-content"
            type="password"
            name="password"
            required
            placeholder="Ingrese su contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <div className="form-border"></div>
          <input
            id="submit-btn"
            type="submit"
            name="submit"
            value="Continuar"
          />
        </form>
      </div>
    </div>
  );
};

export default HomePage;
