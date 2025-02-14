import React, { useState, useEffect } from 'react';
import api from './api';

const App = () => {
  const [Mensagens, setMensagens] = useState([]);
  const [formData, setFormData] = useState({
    title: '',
    content: '',
    isPublished: true
  });

  const fetchMensagens = async () => {
    const response = await api.get('/mensagens');
    setMensagens(response.data);
  };

  useEffect(() => {
    fetchMensagens();
  }, []);

  const handleInputChange = (event) => {
    const value = event.target.type === 'checkbox' ? event.target.checked : event.target.value;
    setFormData({
      ...formData,
      [event.target.name]: value
    });
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    await api.post('/create', formData); // Envia o JSON na estrutura correta
    fetchMensagens();
    setFormData({
      title: '',
      content: '',
      isPublished: true
    });
  };

  return (
    <div>
      <nav className="navbar navbar-dark bg-primary">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            Mensagens APP
          </a>
        </div>
      </nav>
      <div className="container">
        <form onSubmit={handleFormSubmit}>
          <div className="mb-3 mt-3">
            <label htmlFor="title" className="form-label">
              Título
            </label>
            <input
              type="text"
              className="form-control"
              id="title"
              name="title"
              onChange={handleInputChange}
              value={formData.title}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="content" className="form-label">
              Conteúdo
            </label>
            <input
              type="text"
              className="form-control"
              id="content"
              name="content"
              onChange={handleInputChange}
              value={formData.content}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="isPublished" className="form-label">
              Publicada?
            </label>
            <input
              type="checkbox"
              id="isPublished"
              name="isPublished"
              onChange={handleInputChange}
              checked={formData.isPublished}
            />
          </div>
          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </form>
        <table className="table table-striped table-bordered table-hover">
          <thead>
            <tr>
              <th>Título</th>
              <th>Conteúdo</th>
              <th>Publicada?</th>
            </tr>
          </thead>
          <tbody>
            {Mensagens.map((Mensagem) => (
              <tr key={Mensagem.id}>
                <td>{Mensagem.title}</td>
                <td>{Mensagem.content}</td>
                <td>{Mensagem.isPublished ? 'sim' : 'não'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default App;
